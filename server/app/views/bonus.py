from flask import Blueprint, render_template, url_for, request, abort, redirect, current_app
import random

from ..models import db


bonus = Blueprint('bonus', __name__)


@bonus.route('/bonus/draw')
def draw():
    try:
        seed = request.args.get('seed', type=int)
    except ValueError:
        return abort(401)  # When argument failed casting
    if not seed:
        rand = random.randint(100000, 999999)
        return redirect(url_for('.draw', seed=rand))

    winners = db.draw(n=1, seed=seed, instagram=True)
    current_app.logger.info(winners)
    if winners.empty:
        return abort(403)  # When no one can be drawn

    link = url_for('.draw', seed=seed)
    instagram = '@%s' % winners.iloc[0].INST
    return render_template('bingo.pug', link=link, name=instagram)


@bonus.route('/bonus/idle')
def idle():
    link = url_for('.draw')
    return render_template('bingo.pug', link=link)


@bonus.route('/bonus')
def wait():
    link = url_for('.idle')
    return render_template('bingo.pug', link=link)
