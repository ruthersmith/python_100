import requests
import logging

ENDPOINT = "https://api.sheety.co/8c735dfc3ff89e0ee9eb1e39412a38db/flightDeals/prices"


class DataManager:
    """
        This class is responsible for talking to the Google Sheet.
    """

    def get_data(self, endpoint=ENDPOINT):
        respone = requests.get(url=endpoint)
        logging.info(f"Getting Data")
        return respone

    def update_data(self, row_id, update):
        endpoint = f"{ENDPOINT}/{row_id}"
        response = requests.put(url=endpoint, json=update)
        logging.info(f"Updating Data, update => {update}")
        return response

    def post_data(self, body):
        endpoint = 'https://api.sheety.co/8c735dfc3ff89e0ee9eb1e39412a38db/flightDeals/users'
        response = requests.post(url=endpoint,json=body)
        return response
