#you need to pip install twilio to work and create an account in twilio
from twilio.rest import Client

account_sid = "<your acc id>"
auth_token = "[<auth_token>]"

client = Client(account_sid , auth_token)

message = client.messages.create(

									from_ ="<twilio generated mobile number>",
									body = "Your message",
									to = "to number"

									 )

print(message.sid)
