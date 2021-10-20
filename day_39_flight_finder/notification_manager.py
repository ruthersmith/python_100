import logging
from twilio.rest import Client
from data_manager import DataManager
import smtplib


class NotificationManager:
    """
        This class is responsible for sending notifications with the deal flight details.
    """

    def __init__(self, api_keys):
        self.api_keys = api_keys

    def send_notification(self, message_body):
        account_sid = self.api_keys['TWILIO_ACCOUNT_SID']
        auth_token = self.api_keys['TWILIO_AUTH_TOKEN']
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            body=message_body,
            from_=f'+1{self.api_keys["TWILIO_NUMBER"]}',
            to=f"{self.api_keys['MY_PHONE_NUMBER']}"
        )

        print(message.sid)

    def send_email(self, user, message):
        connection = smtplib.SMTP('smtp.gmail.com', 587)
        try:
            # tls == transport layer security
            connection.starttls()
            connection.login(user=self.api_keys['TEST_GMAIL'], password=self.api_keys['TEST_GMAIL_PASSWORD'])
            connection.sendmail(from_addr=self.api_keys['TEST_GMAIL'],
                            to_addrs=user['email'],
                            msg=f"Subject:Cheap Flight\n\n{message}")
            logging.info(f"sending message to {user}")
        except KeyError:
            logging.warning(f"failed to send message to {user}")
        finally:
            connection.close()

    def send_emails(self, message):
        dm = DataManager()
        endpoint = 'https://api.sheety.co/8c735dfc3ff89e0ee9eb1e39412a38db/flightDeals/users'
        users = dm.get_data(endpoint=endpoint).json()['users']
        for user in users:
            self.send_email(user, message)
