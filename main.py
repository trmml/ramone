import os
import sys
import operator

import requests

base = 'http://www.omdbapi.com/?t={}'
movies, errors, files = [], [], []

try:
    dir = sys.argv[1]
    files = os.listdir(dir)
except IndexError:
    print('* Error: No path to movies provided')

for f in files:
    f = f.replace(' ', '+').split('.', 1)[0]
    url = base.format(f)

    r = requests.get(url)

    if r.json().get('Response') == 'False':
        errors.append('Failed attempt with "{}"'.format(f))
    else:
        title = r.json().get('Title')
        rating = r.json().get('imdbRating')
        runtime = r.json().get('Runtime')
        movies.append({'title': title, 'rating': rating, 'runtime': runtime})

movies.sort(key=operator.itemgetter('rating'), reverse=True)

for movie in movies:
    print('* {title} ({runtime}): {rating}/10'.format(**movie))

for error in errors:
    print('* {}'.format(error))
