from flask import Flask, render_template
from blog_data import data

app = Flask(__name__)

@app.route('/')
def home():
    blogs = data
    return render_template("index.html", blogs=blogs)

@app.route('/<int:post_id>')
def post(post_id):
    current_post = data[post_id - 1]
    return render_template("post.html", post=current_post)


if __name__ == "__main__":
    app.run(debug=True)
