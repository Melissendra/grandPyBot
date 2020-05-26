from app.parse import Parse

"""class that is going to test the class Parse and see to potential errors"""


class TestParse:
    def test_cleaning(self):
        sentence = Parse("pff Papy, je suis perdu?")
        assert sentence.clean() == "papy perdu"
