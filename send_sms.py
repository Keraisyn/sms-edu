# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'ACa24dbdea10c742297100c3269f8f777c'
auth_token = 'b906b3924ea39ae373f1b315ad969376'
client = Client(account_sid, auth_token)

message = client.messages.create(
    body="Join Earth's mightiest heroes. Like Kevin Bacon.",
    from_='+13656504161',
    to='+16472875887'
)

print(message.sid)