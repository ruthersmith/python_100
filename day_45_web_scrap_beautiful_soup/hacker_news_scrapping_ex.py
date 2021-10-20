"""
    Trying beautiful soup web scrapping for fun
"""
from bs4 import BeautifulSoup
import requests

url = "https://news.ycombinator.com/news"
response = requests.get(url=url)

soup = BeautifulSoup(response.text, "html.parser")
titles = soup.select(".titlelink")
article_list = []
for title in titles:
    tile = title.getText()
    link = title.get('href')
    upvote = title.find_next(name='span', class_='score').getText()
    article_list.append((title, link, upvote))

for article in article_list:
    print(article[2])

print('----------')
article_list = sorted(article_list, key=lambda point: int(point[2].split()[0]))

for article in article_list:
    print(article[2])

# This was a test using a local html file
# with open('website.html', 'r', encoding='utf-8' ) as file:
#     html_markup = file.read()
# soup = BeautifulSoup(html_markup, "html.parser")
# print(soup)

