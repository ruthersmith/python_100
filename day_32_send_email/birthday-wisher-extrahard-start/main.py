import pandas
import datetime as dt
import random
import smtplib

with open('../secret.txt') as file:
    secret = {
        'from_addr': file.readline().strip(),
        'password': file.readline().strip(),
        'to_addr': file.readline().strip()
    }


def send_birthday_email(message, to):
    subject = "Subject:Happy Birthday!\n\n"
    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(user=secret['from_addr'], password=secret['password'])
        connection.sendmail(from_addr=secret['from_addr'],
                            to_addrs=to,
                            msg=subject + message)


# 2. Check if today matches a birthday in the birthdays.csv
birthday_data = pandas.read_csv('birthdays.csv')
today = dt.datetime.now()
birthday_today = birthday_data[(birthday_data['month'] == today.month) & (birthday_data['day'] == today.day)]

for index, row in birthday_today.iterrows():
    # 3. If step 2 is true, pick a random letter from letter templates and
    # replace the [NAME] with the person's actual name from birthdays.csv
    random_letter = "letter_" + str(random.randint(1, 3)) + ".txt"
    with open(f'letter_templates/{random_letter}') as file:
        letter = file.readlines()
        letter = "".join(letter)

    print(f'sending email to {row["name"]}')
    letter = letter.replace("[NAME]", row['name'])
    print(letter)
    send_birthday_email(message=letter, to=row['email'])
