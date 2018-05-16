import twilio
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = ""
# Your Auth Token from twilio.com/console
auth_token = ""

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+2547227153433",
    from_="+142430400343",
    body="Hello!!")


print(message.sid)
