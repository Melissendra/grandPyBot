import unicodedata
import re
import random
import json
import app.constants as c

""" Class to normalize the user's sentences"""


class Parser:

    """Initialization of the class"""

    def __init__(self, sentence):
        self.sentence = sentence

    """method to put all the sentence in lower case"""

    def _lowercase(self):
        new_sentence = self.sentence.lower()
        return new_sentence

    def _strip_accents(self):
        new_sentence = ''.join(c for c in unicodedata.normalize('NFD', self.sentence) if unicodedata.category(c) != 'Mn')
        return new_sentence

    def _keywords(self):
        pass

    def _clean_stop_words(self):
        clean_stop_words = set()
        with open('app.stop_words.json') as f:
            data = json.load(f)

            for word in data:
                clean_word = word.self._lowercase()._strip_accents()
                clean_stop_words.add(clean_word)
            
        return clean_stop_words

    def _strip_punctuation_stop_words(self):
        stop_words = self._clean_stop_words()
        self.sentence = re.sub(r"[\W]", " ", self.sentence).split()
        self.sentence = [n for n in self.sentence if n not in stop_words]
        self.sentence = ' '.join(self.sentence)
        return self.sentence

    def clean(self):
        self.sentence = self._lowercase()
        self.sentence = self._strip_accents()
        self.sentence = self._strip_punctuation_stop_words()
        return self.sentence


if __name__ == "__main__":
    sentence = Parser("")
    new_sentence = sentence.clean()
    print(new_sentence)
