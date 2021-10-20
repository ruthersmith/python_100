from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager
import logging
import os
import json

'''
This file will need to uses the 
DataManager,
FlightSearch, 
FlightData, 
NotificationManager classes
to achieve the program requirements.
'''


with open("../secret.json") as file:
    API_KEYS = json.load(file)


# logging setups
# not planning on running script elsewhere for now
log_dir = os.getcwd() + os.sep + 'logs'
if not os.path.isdir(log_dir):
    os.mkdir(log_dir)
logging.basicConfig(filename=f'{log_dir}{os.sep}log_record.log',
                    level=logging.DEBUG,
                    format='%(asctime)s %(message)s')


data_manager = DataManager()
sheet_data = data_manager.get_data().json()
flight_searcher = FlightSearch()
notification_manager = NotificationManager(API_KEYS)

# Update the google sheet if a row does not have a iata code
for data_row in sheet_data['prices']:
    if len(data_row['iataCode']) == 0:
        logging.info(f"iataCode for {data_row['city']} was empty")
        location_query_result = flight_searcher.get_destination_code(data_row['city']).json()
        iata_code = location_query_result['locations'][0]['code']
        update = {"price": {'iataCode': iata_code}}
        data_manager.update_data(data_row['id'], update)

list_of_city_destination_code = [row['iataCode'] for row in sheet_data['prices']]
str_of_city_destination_code = ",".join(list_of_city_destination_code)

flight_param = FlightData(fly_to=str_of_city_destination_code)
flight_search_result = flight_searcher.search_flights(flight_param)

for flight in flight_search_result.keys():
    city_row = next((item for item in sheet_data['prices'] if item["city"] == flight), None)
    if city_row:
        if flight_search_result[flight]['price'] < city_row['lowestPrice']:
            message = f"Cheap Flight to {flight} found at {flight_search_result[flight]['price']} dollars " \
                      f"click on link:\n{flight_search_result[flight]['link']}"
            #notification_manager.send_notification(message)
            notification_manager.send_emails(message)
            print(message)
