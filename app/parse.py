import unicodedata
import re
import random
import app.constants as c

""" Class to normalize the user's sentences"""


class Parse:

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

    def _strip_punctuation_stop_words(self):
        self.sentence = re.sub(r"[\W]", " ", self.sentence).split()
        self.sentence = [n for n in self.sentence if n not in c.STOP_WORDS]
        self.sentence = ' '.join(self.sentence)
        return self.sentence

    def _keywords(self):
        pass

    def _empty_input(self):
        if self.sentence == "":
            random_nb = random.randint(0,3)
            self.sentence = c.FUNNY_SENTENCES[random_nb]
            return self.sentence

    def clean(self):
        self.sentence = self._lowercase()
        self.sentence = self._strip_accents()
        self.sentence = self._strip_punctuation_stop_words()
        # self.sentence = self._empty_input()
        return self.sentence


if __name__ == "__main__":
    sentence = Parse("")
    new_sentence = sentence.clean()
    print(new_sentence)
