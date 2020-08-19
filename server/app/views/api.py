from flask import Blueprint, request, jsonify, abort, redirect, url_for
import random

from ..models import db


api = Blueprint('api', __name__)


@api.route('/api/draw')
def draw():
    kwargs = {key: request.args.get(key)
              for key in ['n', 'seed', 'prefix']}
    if not kwargs['seed']:
        kwargs['seed'] = random.randint(100000, 999999)
        return redirect(url_for('.draw', **kwargs))
    try:
        kwargs['n'] = int(kwargs['n']) if kwargs['n'] else 1
        kwargs['seed'] = int(kwargs['seed'])
    except ValueError:
        return abort(401)  # When argument failed casting
    result = db.draw(**kwargs).to_dict(orient='records')
    return jsonify(result)


@api.route('/api/lookup')
def lookup():
    kwargs = {key: request.args.get(key)
              for key in ['prefix']}
    result = db.lookup(**kwargs).to_dict(orient='records')
    return jsonify(result)


@api.route('/api/lookup/<card>')
def lookup_card(card):
    result = db.lookup(card).to_dict(orient='records')
    return jsonify(result)
