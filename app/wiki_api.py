import requests
import app.constants as c


"""Here we'll use Mediawiki to get informations about the address's results"""


class Wikipedia:
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude
        self.url = c.URL_WIKI

    def get_info_by_gps_coordinates(self):
        parameters = {
            "format": "json",  # answer format
            "action": "query",  # what action we ask
            "list": "geosearch",  # search method
            "gsradius": 10000,  # search zone around the address
            "gscoord": f"{self.latitude}| {self.longitude}"  # gps address
        }

        results = requests.get(self.url, parameters)
        if results.status_code == 200:
            data = results.json()["query"]["geosearch"][0]["pageid"]
            return data


        else:
            data = {
                'query': {
                    'geosearch': []
                }
            }
            return "no value"

    def get_info_by_id(self):
        page_id = self.get_info_by_gps_coordinates()
        parameters = {
            "format": "json",
            "action": "query",
            "prop": "extracts|info",
            "inprop": "url",
            "exchars": 1200,
            "explaintext": 1,
            "pageids": page_id
        }

        results = requests.get(self.url, parameters)
        if results.status_code == 200:
            data = results.json()["query"]["pages"][str(page_id)]
            url_page = data["fullurl"]
            title_page = data["title"]
            extract_page = data["extract"]
            return title_page, extract_page, url_page


if __name__ == '__main__':
    wiki = Wikipedia(45.6460494, -0.7911047999999999)
    results_info = wiki.get_info_by_gps_coordinates()
    page_info = wiki.get_info_by_id()

    print(results_info)
    print(page_info)


