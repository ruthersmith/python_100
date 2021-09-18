import datetime as dt
import random
import smtplib

# the day of the week to send motivational, 0==mon 1 ==tues 2 ==wed ...
day_of_week = 0
send_email_today = dt.datetime.now().weekday() == day_of_week


def get_random_quote():
    try:
        with open('quotes.txt', 'r') as file:
            rand_quote = random.choice(file.readlines())
            print(rand_quote)
    except:
        print('An error occurred reading quotes file')
    else:
        return rand_quote


def read_secret_email_info():
    try:
        file = open('secret.txt', 'r')
    except:
        print('Error reading file')
    else:
        secret = {}
        secret['from_addr'] = file.readline().strip()
        secret['password'] = file.readline().strip()
        secret['to_addr'] = file.readline().strip()
        file.close()
        return secret


def send_motivational_email():
    rand_quote = get_random_quote()
    secret = read_secret_email_info()
    connection = smtplib.SMTP("smtp.gmail.com", 587)
    connection.starttls()
    connection.login(user=secret['from_addr'], password=secret['password'])
    connection.sendmail(from_addr=secret['from_addr'],
                        to_addrs=secret['to_addr'],
                        msg=f"Subject:Motivation\n\n{rand_quote}")
    connection.close()


if __name__ == '__main__':
    if send_email_today:
        print('Sending email')
        send_motivational_email()
