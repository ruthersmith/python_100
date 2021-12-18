# Link to form -> https://docs.google.com/forms/d/e/1FAIpQLSf7ZPDw_7SDcjNonZ5EDTcL_BJvibNIFrDMO5_ajnvEBzTQNg/viewform?usp=sf_link
"""
 This program uses beautiful to scrape some housing data
 and uses selenium to fill out a form with this information
"""
import requests
from bs4 import BeautifulSoup

URL = "https://www.zillow.com/brockton-ma/house,condo,multifamily,mobile," \
      "townhouse_type/3-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A" \
      "%22Brockton%2C%20MA%22%2C%22mapBounds%22%3A%7B%22west%22%3A-71.13340590820312%2C%22east%22%3A-70" \
      ".92191909179687%2C%22south%22%3A42.02194123669889%2C%22north%22%3A42.146793162288425%7D%2C" \
      "%22regionSelection%22%3A%5B%7B%22regionId%22%3A44328%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22" \
      "%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A500000%7D%2C%22mp%22%3A%7B%22max%22" \
      "%3A1654%7D%2C%22beds%22%3A%7B%22min%22%3A3%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22land%22%3A%7B" \
      "%22value%22%3Afalse%7D%2C%22apa%22%3A%7B%22value%22%3Afalse%7D%2C%22apco%22%3A%7B%22value%22%3Afalse" \
      "%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D "

# This exist to prove that I am a human
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
                  " (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}


class DataGatherer:

    def __init__(self):
        self.properties = {}

    def get_data(self):
        response = requests.get(URL, headers=HEADERS)
        soup = BeautifulSoup(response.text, "html.parser")
        result_list = soup.select("article")

        property_num = 1
        for r in result_list:
            curr_property = {}
            curr_property['address'] = r.select('.list-card-addr')[0].text if r.select('.list-card-addr') else False
            curr_property['price'] = r.select('.list-card-price')[0].text if r.select('.list-card-price') else False
            bed_bath = r.select('.list-card-details li')
            curr_property['bedroom'] = bed_bath[0].text if bed_bath else False
            curr_property['bathroom'] = bed_bath[1].text if bed_bath else False

            link = r.select('.list-card-link')
            if link:
                if link[0].text:
                    curr_property['link'] = link[0]['href']
            # I don't want any input without a adress and a price
            if not curr_property['address'] or not curr_property['price']:
                continue
            else:
                self.properties[f'property_{property_num}'] = curr_property
                property_num += 1
        print(self.properties)


if __name__ == '__main__':
    worker = DataGatherer()
    worker.get_data()
