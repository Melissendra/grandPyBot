import os
import requests
import papybot.backend.constants as c

# Class to get information from Google Maps Api


class GoogleMaps:
    def __init__(self):
        """we initialize the class"""
        self.url = c.URL_GOOGLE_MAPS

    def get_address(self, search):
        """get the result of the user input"""
        parameters = {
            "address": search,
            "key": os.getenv("GOOGLE_API")
        }

        try:
            request = requests.get(self.url, parameters)
            if request.status_code == 200:
                data = request.json()['results'][0]
                address = data["formatted_address"]
                latitude = data["geometry"]["location"]["lat"]
                longitude = data["geometry"]["location"]["lng"]
                return address, latitude, longitude

        except IndexError:
            return "no result"

