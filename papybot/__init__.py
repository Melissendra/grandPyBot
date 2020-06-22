from flask import Flask

app = Flask(__name__)

from papybot import routes
