import requests
import logging
from flight_data import FlightData

# API_KEY = "bDiUD-w0_gEIOEvWZKZw9qCIUAWrzQFO"
API_KEY = "catuY37VBE19QFL5X21TBlE37U942FMN"


class FlightSearch:
    """
        This class is responsible for talking to the Flight Search API.
    """

    def __init__(self):
        self.header = {
            "apikey": API_KEY
        }

    def get_destination_code(self, location='london'):
        endpoint = "https://tequila-api.kiwi.com/locations/query"

        params = {
            "term": location,
            "locale": "en-US",
            "location_types": "city",
            "limit": "5",
            "active_only": "true"
        }
        response = requests.get(url=endpoint, headers=self.header, params=params)
        return response

    def search_flights(self, flight_data: FlightData):
        flight_search_result = {}
        endpoint = "https://tequila-api.kiwi.com/v2/search"

        response = requests.get(url=endpoint, headers=self.header, params=flight_data.__dict__)
        data = response.json()["data"]
        for result in data:
            print(f"{result['cityTo']}: {result['price']}") if True else False
            logging.info(f"{result['cityTo']}: {result['price']}")
            flight_search_result[result['cityTo']] =  { "price" : result['price'], "link" : result['deep_link']}

        return flight_search_result
