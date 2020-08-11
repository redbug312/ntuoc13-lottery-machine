from flask import Flask, render_template
from werkzeug.exceptions import HTTPException
import pandas as pd


app = Flask(__name__, template_folder='templates')
app.jinja_env.add_extension('pypugjs.ext.jinja.PyPugJSExtension')
app.config.from_pyfile('instance/default.py')


dataframe = pd.read_csv(app.config['ATTENDEES_CSV'])


@app.route('/')
def index():
    title = dataframe.sample(n=1).iloc[0, 1]
    return render_template('welcome.pug', title=title)


@app.errorhandler(HTTPException)
def handle_exception(error):
    title = 'Error %d' % error.code
    return render_template('error.pug', title=title, error=error), error.code
