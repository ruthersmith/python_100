'''
    re familiarizing myself with flask
    also playing with creating decorators
'''
from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def wrapper_function():
        return "<b>" + function() + "</b>"
    return wrapper_function


@app.route("/")
@make_bold
def hello_world():
    return "Hello, World!"


@app.route('/<name>')
def greet(name):
    return f"hello {name}"


if __name__ == "__main__":
    app.run(debug=True)
