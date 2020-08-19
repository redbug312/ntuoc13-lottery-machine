from flask import Blueprint, render_template, abort

from ..models import db


lottery = Blueprint('lottery', __name__)


@lottery.route('/draw/<role>')
def draw(role):
    prefixes = {'undergrad': 'B', 'grad': 'RD'}
    try:
        prefix = prefixes[role]
    except KeyError:
        return abort(401)  # Invalid role found
    winner = db.draw(n=1, seed=None, prefix=prefix).iloc[0]
    return render_template('lottery.pug', winner=winner)
