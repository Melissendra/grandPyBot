from papybot.app.google_api import GoogleMaps
from papybot.app.wiki_api import Wikipedia
from papybot.app.parser import Parser


def answers(question):
    clean_question = Parser(question).clean()
    gmaps = GoogleMaps().get_address(clean_question)
    address, latitude, longitude = gmaps
    media_wiki_coord = Wikipedia(latitude, longitude)
    wiki_info = media_wiki_coord.get_info_by_id()

    return wiki_info
    

if __name__ == "__main__":
    answer = answers("Où se situe Meursac")
    print(answer)
    
