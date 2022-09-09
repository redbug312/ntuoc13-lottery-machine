# ntuoc13-lottery-machine

Lottery machine web app for National Taiwan University Orientation Camp.

Been presented in the semester opening ceremony 2020.

![Demo](media/demo.gif)

## Quickstart

```
$ make start
$ firefox http://0.0.0.0:5000/bonus/idle
```

Click the middle box to draw a winner.

The lottery comes with other sessions:

1. `lottery/undergrad/idle`
2. `lottery/grad/idle`
3. `bonus/idle`
4. `fifty/idle`

`server/app/instance/default.py` specifies the csv
storing the attendee lists, where
[petname](http://manpages.ubuntu.com/manpages/bionic/man1/petname.1.html)
generates the exmaple names.

## Credits

- [Flask](https://flask.palletsprojects.com/), the Python micro framework for building web applications.
- [Anime.js](https://animejs.com/), the JavaScript animation engine.
