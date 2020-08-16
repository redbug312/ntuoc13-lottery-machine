from flask import Flask, render_template
from werkzeug.exceptions import HTTPException

from .models import db


app = Flask(__name__, template_folder='templates')
app.jinja_env.add_extension('pypugjs.ext.jinja.PyPugJSExtension')
app.config.from_pyfile('instance/default.py')


@app.route('/')
def index():
    winner = db.draw(n=1, seed=None).iloc[0]
    return render_template('lottery.pug', winner=winner)


@app.errorhandler(HTTPException)
def handle_exception(error):
    title = 'Error %d' % error.code
    return render_template('error.pug', title=title, error=error), error.code


@app.before_first_request
def init():
    db.init_app(app)
