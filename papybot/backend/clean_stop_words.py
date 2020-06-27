import json
import unicodedata


def clean_stop_words():
    clean_stop_words = set()
    with open('papybot/backend/stop_words.json') as f:
        data = json.load(f)

        for word in data:
            low_case_word = word.lower()
            low_case_strip_accents = ''.join(n for n in unicodedata.normalize('NFD', low_case_word) if unicodedata.category(n) != 'Mn')

            clean_stop_words.add(low_case_strip_accents)

    return clean_stop_words

