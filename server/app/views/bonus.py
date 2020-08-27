from flask import Blueprint, render_template


bonus = Blueprint('bonus', __name__)


@bonus.route('/bonus/fifty')
def fifty():
    winners = ['redbug312'] * 50
    return render_template('fifty.pug', winners=winners)
