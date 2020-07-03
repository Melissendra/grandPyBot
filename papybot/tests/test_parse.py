from papybot.backend.parser import Parser

# class that is going to test the class Parse and see to potential errors


class TestParse:
    def test_cleaning(self):
        """method to test the clean method in the parser class"""
        sentence = Parser("pff, où se situe Meursac?")
        assert sentence.clean() == "meursac"
