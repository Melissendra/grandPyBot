from app.google_api import GoogleMaps


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

        def mock_get_response(self, search):
            return response

        city = "Meursac"
        monkeypatch.setattr(GoogleMaps, 'requests.get', mock_get_response)
        google_test = GoogleMaps()
        result = google_test.get_address(city)
        address = result['results'][0]["formatted_address"]
        assert address == "Meursac, France"

            





