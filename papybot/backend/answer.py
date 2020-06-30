from papybot.backend.google_api import GoogleMaps
from papybot.backend.wiki_api import Wikipedia
from papybot.backend.parser import Parser
import papybot.backend.error_messages as err


def answers(question):
    clean_question = Parser(question).clean()
    if clean_question != "":
        gmaps = GoogleMaps().get_address(clean_question)
        if gmaps != "no result":
            address, latitude, longitude = gmaps
            media_wiki_coord = Wikipedia(latitude, longitude)
            wiki_info = media_wiki_coord.get_info_by_id()
            title = wiki_info[0]
            wiki_article = wiki_info[1]
            url = wiki_info[2]
            return {
                "address": address,
                "latitude": float(latitude),
                "longitude": float(longitude),
                "wiki_article": wiki_article,
                "url": url,
                "title": title,
            }
        else:
            failed_message = err.get_failed_msg()
            return {
                "failed_message": failed_message
            }
    else:
        empty_message = err.get_random_empty_message()
        return {
            "empty_message": empty_message
        }

if __name__ == "__main__":
    answer = answers("")
    print(answer)
    
