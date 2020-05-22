import unicodedata
import re

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

    def _strip_punctuation(self):
        punctuations = re.sub(r"[.!,;?\"\']", " ", self.sentence)
        return punctuations

    def _strip_stop_words(self):
        pass

    def _keywords(self):
        pass

    def clean(self):
        self.sentence = self._lowercase()
        self.sentence = self._strip_accents()
        self.sentence = self._strip_punctuation()
        return self.sentence


if __name__ == "__main__":
    sentence = Parse("Bonjour Papy, l'été est chaud")
    new_sentence = sentence.clean()
    print(new_sentence)