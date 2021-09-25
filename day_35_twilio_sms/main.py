from twilio.rest import Client


# account_sid = os.environ['TWILIO_ACCOUNT_SID']
# auth_token = os.environ['TWILIO_AUTH_TOKEN']

try:
    file = open('secret.txt')
    account_sid = file.readline()
    auth_token = file.readline()
except :
    print("Missing account_sid or auth_token because error with secret.txt file")
else:
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                         body="You are getting this message from Ruthersmith's program",
                         from_='+18722393155',
                         to='7743601056'
                     )
    print(message)
