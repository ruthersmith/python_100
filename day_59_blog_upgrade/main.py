from flask import Flask, render_template, request
from blog_data import data
import json
import smtplib

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

@app.post("/form-entry")
def receive_data():
    if request.method == 'POST':
        data = request.form
        send_email(data)
        return "<h1>Successfully Sent Message</h1>"


def read_secret_email_info():
    try:
        file_r = open('../secret.json', 'r')
        file = json.load(file_r)
    except:
        print('Error reading file')
    else:
        print(file)
        secret = {'from_addr': file['TEST_GMAIL'],
                  'password': file['TEST_GMAIL_PASSWORD'],
                  'to_addr': file['TEST_GMAIL']}

        file_r.close()
        return secret

def send_email(data):
    secret = read_secret_email_info()
    connection = smtplib.SMTP("smtp.gmail.com", 587)
    connection.starttls()
    connection.login(user=secret['from_addr'], password=secret['password'])
    connection.sendmail(from_addr=secret['from_addr'],
                        to_addrs=secret['to_addr'],
                        msg=f"Subject:New Message\n\n{data}")
    connection.close()

if __name__ == '__main__':
    app.run(debug=True)

