import requests
from flask import Flask, render_template
import random
from datetime import date

app = Flask(__name__)


@app.route('/')
def index():
    random_number = random.randint(1, 10)
    this_year = date.today().year
    return render_template('index.html', rando=random_number, year=this_year)


@app.route('/guess/<name>')
def guess(name: str):
    data = {
        'name': name.title(),
        'gender': query(url='https://api.genderize.io', params={'name': name})['gender'],
        'age': query(url='https://api.agify.io/', params={'name': name})['age']
    }
    return render_template('guess.html', data=data)


def query(url, params):
    """makes get request and return the json"""
    response = requests.get(url, params)
    return response.json()


if __name__ == '__main__':
    app.run(debug=True)
