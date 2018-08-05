import os
import sys
import operator
import requests
import re

video_extensions = ['webm', 'mpg', 'mp2', 'mpeg', 'mpe', 'mpv', 'ogg', 'mp4', 'm4p', 'm4v', 'mkv', 'mov', 'flv', 'avi']
regular_exp = re.compile(r", | \. | - | ")
base = 'http://www.omdbapi.com/?t={}'
movies, errors, files = [], [], []

if len(sys.argv) < 1: 
    exit('* Error: No path to movies provided.')

dir = sys.argv[1]
# skips dotfiles
files = [file for file in os.listdir(dir) if not file.startswith('.')]

if not files:
    exit('* Error: Empty directory.')

for f in files:
    movie = re.split(regular_exp,f)
    if movie[-1].lower() not in video_extensions:
        continue

    url = base.format('+'.join(f[:-1]))
    r = requests.get(url)

    if r.json().get('Response') == 'False':
        errors.append('Failed attempt with "{}"'.format(f))
    else:
        title = r.json().get('Title')
        rating = r.json().get('imdbRating')
        movies.append({'title': title, 'rating': rating})

movies.sort(key=operator.itemgetter('rating'), reverse=True)

for movie in movies:
    print('* {}: {}'.format(movie['title'], movie['rating']))

for error in errors:
    print('* {}'.format(error))
