ramone
======

Choose which movie to watch first.

```bash
$ python main.py '/Users/josh/Movies/'

=> The Godfather: 9.2
=> Pulp Fiction: 8.9
=> Star Wars: Episode V - The Empire Strikes Back: 8.8
=> Goodfellas: 8.7
=> Saving Private Ryan: 8.6
=> Se7en: 8.6
=> The Silence of the Lambs: 8.6
=> Psycho: 8.5
=> The Departed: 8.5
=> The Green Mile: 8.5
=> A Clockwork Orange: 8.4
=> Aliens: 8.4
=> Citizen Kane: 8.4
...
```

Every time someone recommends a movie to me I download it and save it
to a folder, and then I never get around to watching it because I have extreme self conflict
on which movie is the best and which one I should get to first. I wrote this to fix that
problem, ironically killing a few hours which I could've been using to watch some of those movies.

ramone will use [omdb](http://www.omdbapi.com) to check the IMDB rating for every file
in your specified directory, then present itself to you so you can make your decision with
this new and helpful information.

By no means is this an extensive tool, I basically made it for myself. If you want to add
features or fix any issues, etc, feel free to submit a PR and I'll check it out.

Usage
-----

Clone, install dependencies, run.

```bash
git clone https://github.com/trmml/ramone

cd ramone && pip install -r requirements.txt
python main.py "/Users/josh/Movies" # argument is the path to your movies
```

LICENSE
-------

[MIT](LICENSE).