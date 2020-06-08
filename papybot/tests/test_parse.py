from papybot.app.parser import Parser

"""class that is going to test the class Parse and see to potential errors"""


class TestParse:
    def test_cleaning(self):
        sentence = Parser("pff, où se situe Meursac?")
        assert sentence.clean() == "meursac"
