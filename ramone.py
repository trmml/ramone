"""
If you have a folder full of movies and don't know where to start. Use this
script to obtain a list of the movies sorted by their IMDB rating.
"""
import operator
import os
import re
import sys
import requests

VIDEO_EXTENSIONS = ['webm', 'mpg', 'mp2', 'mpeg', 'mpe', 'mpv', 'ogg', 'mp4',
                    'm4p', 'm4v', 'mkv', 'mov', 'flv', 'avi']
REGEX = re.compile(r",|\.|-| ")
# you must obtain an API key from omdapi.com
# example: API_URL = '' http://www.omdbapi.com/?i=XXXXXXXXX&apikey=XXXXXXXX
API_URL = ''

def get_ratings(path):
    """
    Iterates through every movie in the folder and appends its rating to
    a list. It then returns the movies sorted by their ratings (from high)
    to low.
    """
    # skips dotfiles
    files = [file for file in os.listdir(path) if not file.startswith('.')]

    if not files:
        exit('* Error: Empty directory.')
        # exits if directory is empty
    for file in files:
    # uses regular expressions to split file name
        movie = re.split(REGEX, file)
        # skips file if it's not a movie
        if movie[-1].lower() not in VIDEO_EXTENSIONS:
            continue

        # creates and requests URL
        url = f"{API_URL}&t={('+'.join(movie[:-1]))}"
        req = requests.get(url)

        # appends movie to correct list depending on response
        movies, errors = [], []
        if req.json().get('Response') == 'False':
            errors.append(file)
        else:
            title = req.json().get('Title')
            rating = req.json().get('imdbRating')
            movies.append({'title': title, 'rating': rating})

    # iterates through rating-sorted movies
    for movie in sorted(movies, key=operator.itemgetter('rating'), reverse=True):
        print('\033[31m*\033[0m {}: {}'.format(movie['title'], movie['rating']))

    # iterates through errors
    for error in errors:
        print('\033[31m*\033[0m Failed attempt with "{}"'.format(error))

# exits if no path is provided
if len(sys.argv) < 2:
    exit('* Error: No path to movies provided.')

PATH = sys.argv[1]

get_ratings(PATH)
