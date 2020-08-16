from flask import Blueprint, request, jsonify, abort, redirect, url_for
import random

from ..models import db


api = Blueprint('api', __name__)


@api.route('/api/draw')
def draw():
    n = request.args.get('n')
    seed = request.args.get('seed')
    if not seed:
        seed = random.randint(100000, 999999)
        return redirect(url_for('.draw', n=n, seed=seed))
    try:
        n = int(n) if n else 1
        seed = int(seed)
    except ValueError:
        abort(401)  # When argument failed casting
    result = db.draw(n=n, seed=seed).to_dict(orient='records')
    return jsonify(result)


@api.route('/api/lookup')
def lookup():
    result = db.lookup().to_dict(orient='records')
    return jsonify(result)


@api.route('/api/lookup/<card>')
def lookup_card(card):
    result = db.lookup(card).to_dict(orient='records')
    return jsonify(result)
