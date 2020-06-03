from app.wiki_api import Wikipedia

"""Here we test the response we get from Wikipedia api"""


class TestWikipedia:

    def test_get_info(self, monkeypatch):
        response = {
            'query': [{
                'pages': {
                    '348682': {
                        'title': 'Meursac',
                        'extract': 'Meursac (prononcé [mœʁ.sak]) est une commune du Sud-Ouest de la France située dans le département de la Charente-Maritime (région Nouvelle-Aquitaine).',
                        'fullurl': 'https://fr.wikipedia.org/wiki/Meursac'
                    }
                }
            }]
        }
        """Mock of the requests.get method"""
        class MockGetResponse:
            def __init__(self, url, params=None):
                self.status_code = 200

            @staticmethod
            def json():
                return response

        monkeypatch.setattr('requests.get', MockGetResponse)
        wiki_test = Wikipedia(45.6460494, -0.7911047999999999)
        wiki_result = wiki_test.get_info_by_id()
        result = response["query"]["pages"]['348682']
        title = result["title"]
        assert title == "Meursac"
