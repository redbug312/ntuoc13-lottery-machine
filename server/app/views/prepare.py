from flask import Blueprint, render_template


prepare = Blueprint('prepare', __name__)


@prepare.route('/prepare')
def index():
    return render_template('prepare.pug')
