"""
    Simple script, wanted to know how scrapping amazon would go
    for checking the price and emailing myself if the price of the item is less than a predetermined price
"""
import requests
from bs4 import BeautifulSoup
import json
import smtplib

PREDEFINED_PRICE = 26  # hard coded for testing purposes
file = open('../secret.json')
API_KEYS = json.load(file)
file.close()

# Make a request to Amazon url
url = "https://www.amazon.com/GANSANRO-Mens-Joggers-Sweatpants-Slim-Fit-Mens-Athletic-Jogger-Pants-" \
      "Dark-Grey-Sweatpants-for-Men-with-Zipper-Pockets-Medium/dp/B08C5141TT/" \
      "ref=pd_ybh_a_211?_encoding=UTF8&psc=1&refRID=BMQVRHRX5R9VTR2W4XSS"

# Had to add the headers to the request, otherwise amazon was returning an error
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
                  " (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

response = requests.get(url=url, headers=headers)
# Getting the price of the item
soup = BeautifulSoup(response.text, "html.parser")
price = float(soup.select_one("#priceblock_ourprice").getText().replace('$', ''))

# Sending email if the price is below a predefined_price
if price < PREDEFINED_PRICE:
    message = f"Drop in Price for\n{url}\nCurrent price {price} smaller than {PREDEFINED_PRICE}"
    connection = smtplib.SMTP(host='smtp.gmail.com', port=587)
    connection.starttls()
    connection.login(user=API_KEYS['TEST_GMAIL'], password=API_KEYS['TEST_GMAIL_PASSWORD'])
    connection.sendmail(from_addr=API_KEYS['TEST_GMAIL'],
                        to_addrs=API_KEYS['TEST_GMAIL'],
                        msg=f"Subject:Price Drop Alert\n\n{message}")
else:
    print('not smaller')  # exist for testing purposes
