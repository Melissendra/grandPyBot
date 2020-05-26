import os
import envkey
import googlemaps


"""Class to get information from googlemaps Api"""
api_key = os.environ()

class GoogleMaps:
    def __init__(self, api_key):
        self.api_key = api_key

    def get_address(self, search):
        """get the result of the user input"""
        gmaps = googlemaps.Client(key=self.api_key)
        gmap_result = gmaps.geocode(search, region='fr')

