from twilio.rest import TwilioRestClient
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC67bfac383205f80320f28b84da3e27d8"
auth_token  = "306c260d8b7edbb78bdcac729c5d1849"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(body="My name is Dilnawaz",
    to="+918609276876",    # Replace with your phone number
    from_="+13345138303") # Replace with your Twilio number
print message.sid