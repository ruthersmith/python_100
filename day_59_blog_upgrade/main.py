from flask import Flask, render_template
from blog_data import data

app = Flask(__name__)


@app.route('/')
def index():
    blogs = data
    return render_template("index.html", blogs=blogs)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/post/<int:post_id>')
def post(post_id):
    return render_template('post.html', blog=data[post_id-1])


if __name__ == '__main__':
    app.run(debug=True)
