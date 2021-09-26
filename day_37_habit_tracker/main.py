import requests
import os
from datetime import datetime


class HabitTracker:
    """
        Makes a habit tracker using the pixela API
    """

    pixela_endpoint = "https://pixe.la/v1/users"

    try:
        file = open('secret.txt')
        TOKEN = file.readline().strip()
        USERNAME = file.readline().strip()
        file.close()
    except:
        print("Missing secret.txt file that contains TOKEN AND USERNAME")

    def __init__(self):
        if os.path.exists('response.txt'):
            self.log_file = open('response.txt', 'a')
        else:
            self.log_file = open('response.txt', 'w')

        self.headers = {
            "X-USER-TOKEN": HabitTracker.TOKEN
        }

    def create_user(self):
        params = {
            "token": HabitTracker.TOKEN,
            "username": HabitTracker.USERNAME,
            "agreeTermsOfService": "yes",
            "notMinor": "yes"
        }
        response = requests.post(url=HabitTracker.pixela_endpoint, json=params)
        self.log_response(response)

    def create_graph(self):
        endpoint = f"{HabitTracker.pixela_endpoint}/{HabitTracker.USERNAME}/graphs"
        graph_config = {
            "id": "graph1",
            "name": "Meditation Time",
            "unit": "min",
            "type": "int",
            "color": "momiji",
            "timezone": "America/New_York"

        }

        response = requests.post(url=endpoint, json=graph_config, headers=self.headers)
        self.log_response(f"response for graph creation {response.text}")

    def modify_pixel(self, http_method, graph_id, p_date, p_quantity=0):
        endpoint = f"{HabitTracker.pixela_endpoint}/{HabitTracker.USERNAME}/graphs/{graph_id}"
        graph_data = {"quantity": f"{p_quantity}"}
        if http_method.__name__ == 'put' or http_method.__name__ == 'delete':
            endpoint += f'/{p_date}'
        elif http_method.__name__ == 'post':
            graph_data["date"] = p_date
        response = http_method(url=endpoint, json=graph_data, headers=self.headers)
        self.log_response(f"response for modifying pixel using {http_method.__name__} method: {response.text}\n")

    def log_response(self, response):
        self.log_file.write(response)
        print(response)


if __name__ == '__main__':
    tracker = HabitTracker()
    tracker.modify_pixel(http_method=requests.post,
                         graph_id="graph1",
                         p_date=datetime.now().strftime('%Y%m%d'),
                         p_quantity=10
                         )
    tracker.log_file.close()