from app.parse import Parse
import app.constants as c
"""class that is going to test the class Parse and see to potential errors"""


class Test_parse:
    def test_cleaning(self):
        sentence = Parse("pff Papy, je suis perdu.")
        assert sentence.clean() == "papy perdu"
