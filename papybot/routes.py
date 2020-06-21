from flask import render_template, jsonify,request
from .app.parser import Parser
from . import app




@app.route('/')
def index():
    user = {"username": "Gaelle"}
    return render_template('index.html', title='Grandpy bot', user=user)

@app.route("/ajax", methods=["POST"])
def ajax():
    user_text= request.form["grandPyBot"]
    response = Parser(user_text).clean()
    print(response)
    return jsonify(response)