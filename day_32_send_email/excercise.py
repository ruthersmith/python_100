import smtplib
import datetime as dt

file = open('secret.txt', 'r')
email_1 = file.readline().strip()
password_1 = file.readline().strip()
to_email = file.readline().strip()
file.close()


class BirthdayWisher:

    def __init__(self):
        self.connection = smtplib.SMTP('smtp.gmail.com', 587)
        # tls == transport layer security
        self.connection.starttls()
        self.connection.login(user=email_1, password=password_1)
        self.connection.sendmail(from_addr=email_1,
                                 to_addrs=to_email,
                                 msg="Subject:hello buddy\n\n Hello just saying hi!")
        self.connection.close()


if __name__ == '__main__':
   # BirthdayWisher()
    print(dt.datetime.now().weekday())
