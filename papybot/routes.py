import os
from flask import render_template, jsonify, request
from papybot import app
from papybot.backend.answer import answers


@app.route('/')
def index():
    return render_template('index.html', title='Grandpy bot', google_key=os.getenv("GOOGLE_API_FRONT"))

@app.route("/ajax", methods=["POST"])
def ajax():
    user_text= request.data.decode()
    response = answers(user_text)
    return jsonify(response)
