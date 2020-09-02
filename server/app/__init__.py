from flask import Flask, render_template
from werkzeug.exceptions import HTTPException

from .models import db, ig
from .views.api import api
from .views.lottery import lottery
from .views.bonus import bonus
from .views.fifty import fifty


app = Flask(__name__, template_folder='templates')
app.jinja_env.add_extension('pypugjs.ext.jinja.PyPugJSExtension')
app.config.from_pyfile('instance/default.py')
app.register_blueprint(api)
app.register_blueprint(lottery)
app.register_blueprint(bonus)
app.register_blueprint(fifty)


@app.route('/')
def index():
    return render_template('index.pug')


@app.errorhandler(HTTPException)
def handle_exception(error):
    title = 'Error %d' % error.code
    return render_template('error.pug', title=title, error=error), error.code


@app.before_first_request
def init():
    db.init_app(app)
    ig.init_app(app)
