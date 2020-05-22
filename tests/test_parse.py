from app.parse import Parse

"""class that is going to test the class Parse and see to potential errors"""


class Test_parse:
    def test_cleaning(self):
        sentence = Parse("Bonjour Papy, l'été est chaud")
        assert sentence.clean() == "bonjour papy l ete est chaud"
