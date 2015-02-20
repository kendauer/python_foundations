from twilio import rest
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "YOURACCOUNT_SID"
auth_token  = "YOURTOKEN"
client = rest.TwilioRestClient(account_sid, auth_token)

myNumber = "+1234567890"

message = client.messages.create(body="You are twice as awesome.",
    to=myNumber,   # Replace with your phone number
    from_="+1234567890"") # Replace with your Twilio number

print message.sid
