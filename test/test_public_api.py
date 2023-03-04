

class TestPublicApi:
    """


    # """
    # # def test_create_booking(self):
    # #     """
    # #
    # #     :return:
    # #     """
    # #
    import requests
    import json

    url = "https://restful-booker.herokuapp.com/booking"

    payload = json.dumps({
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.json())
    assert response.json()['booking'],['firstname'] == 'TestName'

    def test_update_booking(self):
        """

        :return:
        """
        import requests
        import json

        url = "https://restful-booker.herokuapp.com/booking/1"

        payload = json.dumps({
            "firstname": "James",
            "lastname": "Brown",
            "totalprice": 111,
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2018-01-01",
                "checkout": "2019-01-01"
            },
            "additionalneeds": "Breakfast"
        })
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Cookie': 'token=abc123'
        }

        response = requests.request("PUT", url, headers=headers, data=payload)
        assert response.status_code == 403
