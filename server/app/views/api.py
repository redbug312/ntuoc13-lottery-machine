from flask import Blueprint, request, jsonify, abort, redirect, url_for
import random

from ..models import db


api = Blueprint('api', __name__)


@api.route('/api/draw')
def draw():
    try:
        n = request.args.get('n', default=3, type=int)
        seed = request.args.get('seed', type=int)
        prefix = request.args.get('prefix', default='B')
    except ValueError:
        return abort(401)  # When argument failed casting
    if not seed:
        rand = random.randint(100000, 999999)
        return redirect(url_for('.draw', n=n, seed=rand, prefix=prefix))

    result = db.draw(n=n, seed=seed, prefix=prefix) \
               .to_dict(orient='records')
    return jsonify(result)


@api.route('/api/lookup')
def lookup():
    prefix = request.args.get('prefix')
    result = db.lookup(prefix=prefix).to_dict(orient='records')
    return jsonify(result)


@api.route('/api/lookup/<card>')
def lookup_card(card):
    result = db.lookup(card).to_dict(orient='records')
    return jsonify(result)
