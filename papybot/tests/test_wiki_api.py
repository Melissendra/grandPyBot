from papybot.backend.wiki_api import Wikipedia

"""Here we test the response we get from Wikipedia api"""


class TestWikipedia:
    """
        Method to test the first requests to get the pageid from Wikipedia
    """
    def test_get_info_by_gps_coordinates(self, monkeypatch):
        """Method to test the first request to get the pageid"""
        response = {
            'query': {
                'geosearch': [{
                    'pageid': 348682
                }]
            }
        }

        class MockGetResponse:
            def __init__(self, url, params=None):
                self.status_code = 200
            
            @staticmethod
            def json():
                return response

        monkeypatch.setattr('requests.get', MockGetResponse)
        wiki_id_test = Wikipedia(45.6460494, -0.7911047999999999)
        page_id = wiki_id_test.get_info_by_gps_coordinates()
        page_id_result = response['query']['geosearch'][0]['pageid']
        assert page_id == page_id_result

    def test_get_info_by_id(self, monkeypatch):
        """Method to test the method to get the wiki information by id"""
        response = {
            'query': {
                'pages': {
                    '348682': {
                        'title': 'Meursac',
                        'extract': "résumé Meursac",
                        'fullurl': 'https://fr.wikipedia.org/wiki/Meursac'
                    }
                }
            }
        }
        """Mock of the requests.get method"""
        class MockGetResponse:
            def __init__(self, url, params=None):
                self.status_code = 200

            @staticmethod
            def json():
                return response

        def mock_get_info_by_coordinates(self):
            return 348682

        monkeypatch.setattr('requests.get', MockGetResponse)
        monkeypatch.setattr('papybot.backend.wiki_api.Wikipedia.get_info_by_gps_coordinates', mock_get_info_by_coordinates)
        wiki_test = Wikipedia(45.6460494, -0.7911047999999999)
        title_result, extract_result, url_result = wiki_test.get_info_by_id()
        result = response["query"]["pages"]['348682']
        title = result["title"]
        url = result["fullurl"]
        extract = result["extract"]
        
        assert title_result == title
        assert url_result == url
        assert extract_result == extract
