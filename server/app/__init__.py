from flask import Flask, render_template, abort
from werkzeug.exceptions import HTTPException

from .models import db
from .views.api import api
from .views.lottery import lottery


app = Flask(__name__, template_folder='templates')
app.jinja_env.add_extension('pypugjs.ext.jinja.PyPugJSExtension')
app.config.from_pyfile('instance/default.py')
app.register_blueprint(api)
app.register_blueprint(lottery)


@app.route('/')
def index():
    return abort(401)


@app.errorhandler(HTTPException)
def handle_exception(error):
    title = 'Error %d' % error.code
    return render_template('error.pug', title=title, error=error), error.code


@app.before_first_request
def init():
    db.init_app(app)
