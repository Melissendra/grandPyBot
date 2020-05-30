import os
import requests
import app.constants as c

"""Class to get information from googlemaps Api"""
class GoogleMaps:
    def __init__(self):
        self.url = c.URL

    def get_address(self, search):
        """get the result of the user input"""
        parameters = {
            "address": search,
            "key": os.getenv("GOOGLE_API")
        }

        try:
            request = requests.get(self.url, parameters)
            data = request.json()['results'][0]
            address = data["formatted_address"]
            latitude = data["geometry"]["location"]["lat"]
            longitude = data["geometry"]["location"]["lng"]
            return address, latitude, longitude
            
        except IndexError:
            return "No result"

if __name__ == "__main__":
    google = GoogleMaps()
    request = google.get_address("35b rue du petit pont, Meursac")
    print(request)
