from flask import Blueprint, request, jsonify, abort, redirect, url_for
import random

from ..models import db, ig


api = Blueprint('api', __name__)


@api.route('/api/db/draw')
def db_draw():
    try:
        n = request.args.get('n', default=3, type=int)
        seed = request.args.get('seed', type=int)
        prefix = request.args.get('prefix', default='B')
        instagram = request.args.get('instagram', default=False, type=bool)
    except ValueError:
        return abort(401)  # When argument failed casting
    if not seed:
        rand = random.randint(100000, 999999)
        return redirect(url_for('.db_draw', seed=rand, **request.args))

    result = (db.draw(n=n, seed=seed, prefix=prefix, instagram=instagram)
                .to_dict(orient='records'))
    return jsonify(result)


@api.route('/api/db/lookup')
def db_lookup():
    try:
        prefix = request.args.get('prefix', default='A-Z')
        instagram = request.args.get('instagram', default=False, type=bool)
    except ValueError:
        return abort(401)  # When argument failed casting

    result = (db.lookup(prefix=prefix, instagram=instagram)
                .to_dict(orient='records'))
    return jsonify(result)


@api.route('/api/db/lookup/<card>')
def db_lookup_card(card):
    result = db.lookup(card).iloc[0].to_dict()
    return jsonify(result)


@api.route('/api/ig/draw')
def ig_draw():
    try:
        n = request.args.get('n', default=50, type=int)
        seed = request.args.get('seed', type=int)
    except ValueError:
        return abort(401)  # When argument failed casting
    if not seed:
        rand = random.randint(100000, 999999)
        return redirect(url_for('.ig_draw', n=n, seed=rand))

    result = ig.draw(n=n, seed=seed).to_list()
    return jsonify(result)


@api.route('/api/ig/lookup')
def ig_lookup():
    result = ig.lookup().to_list()
    return jsonify(result)
