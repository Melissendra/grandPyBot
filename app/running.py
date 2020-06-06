from app.google_api import GoogleMaps
from app.wiki_api import Wikipedia
from app.parser import Parser


class Running:
    def __init__(self, question):
        self.question = question
        
