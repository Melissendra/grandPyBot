from flask import render_template
from papybot import app


@app.route('/')
@app.route('/index')
def index():
    user = {"username": "Gaelle"}
    return render_template('index.html', title = 'Grandpy bot', user=user)
