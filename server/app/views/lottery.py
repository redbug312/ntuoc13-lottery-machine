from flask import Blueprint, request, render_template, abort, redirect, url_for
import random

from ..models import db


lottery = Blueprint('lottery', __name__)


@lottery.route('/draw/<role>')
def draw(role):
    prefixes = {'undergrad': 'B', 'grad': 'RD'}
    if role not in prefixes.keys():
        return abort(404)  # Invalid role found

    try:
        i = request.args.get('i', default=0, type=int)
        seed = request.args.get('seed', type=int)
    except ValueError:
        return abort(401)  # When argument failed casting
    if not seed:
        seed = random.randint(100000, 999999)
        return redirect(url_for('.draw', role=role, i=0, seed=seed))

    prefix = prefixes[role]
    winners = db.draw(n=3, seed=seed, prefix=prefix)
    if winners.empty:
        return abort(404)  # When no one can be drawn
    elif i >= winners.shape[0]:
        return redirect(url_for('.draw', role=role))

    link = url_for('.draw', role=role, i=(i + 1), seed=seed)
    winner = winners.iloc[i].to_dict()
    return render_template('lottery.pug', link=link, winner=winner)


@lottery.route('/idle/<role>')
def idle(role):
    link = url_for('.draw', role=role)
    return render_template('lottery.pug', link=link)
