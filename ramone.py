import os, sys, operator, requests, re

video_extensions = ['webm', 'mpg', 'mp2', 'mpeg', 'mpe', 'mpv', 'ogg', 'mp4', 'm4p', 'm4v', 'mkv', 'mov', 'flv', 'avi']
regular_exp = re.compile(r",|\.|-| ")
# you must obtain an API key from omdapi.com
# example: api_url = '' http://www.omdbapi.com/?i=XXXXXXXXX&apikey=XXXXXXXX
api_url = ''
movies, errors = [], []

# exits if no path is provided
if len(sys.argv) < 2: 
    exit('* Error: No path to movies provided.')

dir = sys.argv[1]
# skips dotfiles
files = [file for file in os.listdir(dir) if not file.startswith('.')]

# exits if directory is empty
if not files:
    exit('* Error: Empty directory.')

for f in files:
    # uses regular expressions to split file name
    movie = re.split(regular_exp,f)
    # skips file if it's not a movie
    if movie[-1].lower() not in video_extensions:
        continue
    
    # creates and requests URL
    url = f"{api_url}&t={('+'.join(movie[:-1]))}"
    r = requests.get(url)

    # appends movie to correct list depending on response
    if r.json().get('Response') == 'False':
        errors.append(f)
    else:
        title = r.json().get('Title')
        rating = r.json().get('imdbRating')
        movies.append({'title': title, 'rating': rating})

# iterates through rating-sorted movies
for movie in sorted(movies, key=operator.itemgetter('rating'), reverse=True):
    print('* {}: {}'.format(movie['title'], movie['rating']))

# iterates through errors
for error in errors:
    print('* Failed attempt with "{}"'.format(error))
