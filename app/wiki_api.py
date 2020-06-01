import requests
import app.constants as c


"""Here we'll use Mediawiki to get informations about the address's results"""


class Wikipedia:
    def __init__(self):
        self.url = c.URL_WIKI

    def get_info(self, latitude, longitude):
        parameters = {
            "format": "json",  # answer format
            "action": "query",  # what action we ask
            "list": "geosearch",  # search method
            "gsradius": 10000,  # search zone around the address
            "gscoord": f"{latitude}| {longitude}"  # gps address
        }

        results = requests.get(self.url, parameters)
        if results.status_code == 200:
            data = results.json()["query"][""]
            return f"Voici votre résultat: {data}"

        else:
            data = {
                'query': {
                    'geosearch': []
                }
            }
            return "no value"


if __name__ == '__main__':
    wiki = Wikipedia()
    results = wiki.get_info(45.6460494, -0.7911047999999999)
    print(results)


