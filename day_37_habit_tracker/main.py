import requests
import os


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

    def add_pixel_to_graph(self, graph_id):
        params = {
            "date": "20210925",
            "quantity": "10"
        }
        endpoint = f"{HabitTracker.pixela_endpoint}/{HabitTracker.USERNAME}/graphs/{graph_id}"
        response = requests.post(url=endpoint,json=params, headers=self.headers)
        self.log_response(f"response for adding pixel to graph {response.text}\n")

    def log_response(self, response):
        self.log_file.write(response)
        print(response)


if __name__ == '__main__':
    tracker = HabitTracker()
   # tracker.add_pixel_to_graph("graph1")
    tracker.log_file.close()
