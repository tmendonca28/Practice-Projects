import twilio
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC7f7a3a378ad249d600b49711d1287e77e"
# Your Auth Token from twilio.com/console
auth_token = "51379ec1b6efde7cf6f35093c04da9fex"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+2547227153433",
    from_="+142430400343",
    body="Hello!!")


print(message.sid)
