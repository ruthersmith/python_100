"""
    Number guessing game and using flask to provide web interface
"""
from flask import Flask
import random

app = Flask(__name__)

rand_num = random.randint(0, 10)
counting_gif = "https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif"
too_high_gif = "https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif"
too_low_gif = "https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif"
correct_gif = "https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif"


@app.route('/')
def game_intro():
    return f"<h1>Guess a number between 0 and 9</h1> " \
           f"<img src='{counting_gif}'/>"


@app.route('/<guess>')
def receiver(guess):
    guess = int(guess)
    if guess < rand_num:
        return f"<h1>Guessed to low </h1> " \
               f"<img src='{too_low_gif}'/>"
    elif guess > rand_num:
        return f"<h1>Guessed to High </h1> " \
               f"<img src='{too_high_gif}'/>"
    else:
        return f"<h1>Correct </h1> " \
               f"<img src='{correct_gif}'/>"


if __name__ == '__main__':
    print(rand_num)
    app.run(debug=True)
