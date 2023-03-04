# import pytest
# from test.test_api import TestApi
#
#
# class TestDataFromApi(TestApi):
#     text = 'This data was produced from the CoinDesk Bitcoin Price Index (USD). Non-USD currency data converted using hourly conversion rate from openexchangerates.org'
#
#
#
#
#     @pytest.mark.api
#     def test_use_api(self):
#        data = self.test_call_get_api()
#
#     assert TestDataFromApi.text in data['disclaimer']

import pytest
import requests
class TestAPI:
    url = 'https://cat-fact.herouapp.com/facts'

    def test_api(self):
        response = requests.request("GET", TestAPI.url)
        assert response.status_code == 200
        response_dict = response.json()
        print(response_dict)
        assert response.status_code == 200