from flask import Blueprint, render_template, url_for, request, abort, redirect
import random

from ..models import db


lottery = Blueprint('lottery', __name__)


@lottery.route('/lottery/<role>/draw')
def draw(role):
    prefixes = {'undergrad': 'B', 'grad': 'RD'}
    if role not in prefixes.keys():
        return abort(404)  # Invalid role found

    try:
        seed = request.args.get('seed', type=int)
    except ValueError:
        return abort(401)  # When argument failed casting
    if not seed:
        rand = random.randint(100000, 999999)
        return redirect(url_for('.draw', role=role, seed=rand))

    prefix = prefixes[role]
    winners = db.draw(n=1, seed=seed, prefix=prefix)
    if winners.empty:
        return abort(403)  # When no one can be drawn

    link = url_for('.draw', role=role, seed=seed)
    name = winners.iloc[0].NAME
    desc = winners.iloc[0].STID
    return render_template('bingo.pug', link=link, name=name, desc=desc)


@lottery.route('/lottery/<role>/idle')
def idle(role):
    link = url_for('.draw', role=role)
    return render_template('bingo.pug', link=link)


@lottery.route('/lottery/<role>')
def wait(role):
    link = url_for('.idle', role=role)
    return render_template('bingo.pug', link=link)
