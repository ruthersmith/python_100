"""
    simple program to work with the twilio api to send a text message
    This works with an accompanying secret.txt file that contains the creditials
    or you could edit the script directly
"""

from twilio.rest import Client


# account_sid = os.environ['TWILIO_ACCOUNT_SID']
# auth_token = os.environ['TWILIO_AUTH_TOKEN']

try:
    file = open('secret.txt')
    account_sid = file.readline()
    auth_token = file.readline()
    twilio_num = file.readline().strip()
    text_num = file.readline().strip()
    file.close()
    
except :
    print("Missing account_sid or auth_token because error with secret.txt file")
else:
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                         body="You are getting this message from Ruthersmith's program",
                         from_=f'+1{twilio_num}',
                         to=f'{text_num}'
                     )
    print(message)
