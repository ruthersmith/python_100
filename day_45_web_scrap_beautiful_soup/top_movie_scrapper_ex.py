"""
    Using web scrapping to get a list of the top 100 movies of all time
"""
import requests
from bs4 import BeautifulSoup
import json

url_to_scrape = "https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(url=url_to_scrape)
soup = BeautifulSoup(response.text, "html.parser")

print(soup.find_all(name="h3"))

# This returned one giant json object
data = soup.select("#__NEXT_DATA__")

data_text = data[0].getText()
data_dic = json.loads(data_text)['props']['pageProps']['data']['getArticleByFurl']['_layout']

for layout in data_dic:
    # find a layout with a title because that is where the list of json object
    # that have the information about the movie are found
    if layout['content']['title'] is not None:
        data_dic = layout['content']['images']
        break

file = open('movies.txt', 'w', encoding='utf-8')

for title in reversed(data_dic):
    file.write(f'{title["titleText"]}\n')

file.close()
