from flask import Blueprint, render_template, url_for, request, abort, redirect
import random

from ..models import ig


fifty = Blueprint('fifty', __name__)


@fifty.route('/fifty/draw')
def draw():
    try:
        n = request.args.get('n', default=50, type=int)
        seed = request.args.get('seed', type=int)
    except ValueError:
        return abort(401)  # When argument failed casting
    if not seed:
        seed = random.randint(100000, 999999)
        return redirect(url_for('.draw', seed=seed))

    winners = ig.draw(n=n, seed=seed).sort_values().to_list()
    return render_template('fifty.pug', winners=winners)


@fifty.route('/fifty/idle')
def idle():
    return render_template('fifty.pug')
