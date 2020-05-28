import googlemaps
import re
import app.constants as c

"""Class to get information from googlemaps Api"""


class GoogleMaps:
    def __init__(self, api_key):
        self.api_key = api_key

    def get_address(self, search):
        """get the result of the user input"""
        gmaps = googlemaps.Client(key=self.api_key)
        gmap_result = gmaps.geocode(search, region='fr')

        try:
            address = gmap_result[0]["formatted_address"]
            address = re.sub(r"[,]", "", address)
            latitude = gmap_result[0]["geometry"]["location"]["lat"]
            longitude = gmap_result[0]["geometry"]["location"]["lng"]
            return {
                address,
                latitude,
                longitude
            }
        except IndexError:
            return "No result"


if __name__ == "__main__":
    google = GoogleMaps(c.API_KEY)
    gmaps = google.get_address("35b rue du petit pont, Meursac")
    print(gmaps)
