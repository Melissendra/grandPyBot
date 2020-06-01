from app.google_api import GoogleMaps

"""Here we test the response we get from Google Maps api"""
class TestGoogleMaps:

    def test_get_address(self, monkeypatch):
        response = {
            'results': [{
                'formatted_address': 'Meursac, France',
                'geometry': {
                    'location':{
                        'lat': 45.6460494,
                        'lng': -0.7911047999999999
                    }
                }
            }]
        }
        """mock of the requests.get method"""
        class MockGetResponse:
            def __init__(self, url, params=None):
                self.status_code = 200

            def json(self):
                return response

        monkeypatch.setattr('requests.get', MockGetResponse)
        google_test = GoogleMaps()
        api_result = google_test.get_address("Meursac")
        result = response["results"][0]
        address = result["formatted_address"]
        latitude = result["geometry"]["location"]["lat"]
        longitude = result["geometry"]["location"]["lng"]
        assert address == "Meursac, France"
        assert latitude == 45.6460494
        assert longitude == -0.7911047999999999


            





