from flask import Blueprint, render_template, url_for, request, abort, redirect
import random

from ..models import db


bonus = Blueprint('bonus', __name__)


@bonus.route('/bonus/draw')
def draw():
    try:
        i = request.args.get('i', default=0, type=int)
        seed = request.args.get('seed', type=int)
    except ValueError:
        return abort(401)  # When argument failed casting
    if not seed:
        rand = random.randint(100000, 999999)
        return redirect(url_for('.draw', i=0, seed=rand))

    winners = db.draw(n=3, seed=seed, prefix='BRD')
    if winners.empty:
        return abort(404)  # When no one can be drawn
    elif i >= winners.shape[0]:
        return redirect(url_for('.draw'))

    link = url_for('.draw', i=(i + 1), seed=seed)
    name = winners.iloc[i].NAME
    desc = winners.iloc[i].STID
    return render_template('bingo.pug', link=link, name=name, desc=desc)


@bonus.route('/bonus/idle')
def idle():
    link = url_for('.draw')
    return render_template('bingo.pug', link=link)
