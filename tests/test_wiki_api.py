from app.wiki_api import Wikipedia

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
        

    def test_get_info(self, monkeypatch):
        response = {
            'query': [{
                'pages': {
                    '348682': {
                        'title': 'Meursac',
                        'extract': "Meursac (prononcé [mœʁ.sak]) est une commune du Sud-Ouest de la France située dans le département de la Charente-Maritime (région Nouvelle-Aquitaine). Ses habitants sont appelés les Meursacais et les Meursacaises.\nCommune à dominante rurale, au cœur d'une région céréalière et viticole et à proximité des stations balnéaires de la côte de Beauté, Meursac est une commune appartenant à la région naturelle du Royannais. Elle se rattache au bassin de vie de Saujon et à la sphère d'influence urbaine de Royan. Sa relative proximité avec cette ville, important centre économique du département, explique la croissance constante de sa population et le développement du phénomène de périurbanisation, qui fait que de nombreux citadins, à la recherche d'une plus grande qualité de vie, partent s'installer dans les communes de la grande périphérie.\nLa commune se compose de deux centres principaux : Saint-Martin, qui correspond au centre-bourg, concentre la plus grande partie des commerces de proximité, les écoles et l'église Saint-Martin. Édifice majeur du village, il est une synthèse des styles roman saintongeais et gothique rayonnant (XIIe\u2009–\u2009XVe siècles). Les Épeaux, principal écart de la commune,…",
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
        url_result, title_result, extract_result = wiki_test.get_info_by_id(self.test_get_info_by_gps_coordinates)
        result = response["query"]["pages"]['348682']
        title = result["title"]
        url = result["fullurl"]
        extract = result["extract"]
        
        assert title_result == title_result
        assert url_result == url_result
        assert extract_result == extract
