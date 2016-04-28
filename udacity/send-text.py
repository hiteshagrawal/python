#!/usr/bin/python

from twilio.rest import TwilioRestClient
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC990fe190c75cef2c26f6119be458d87d"
auth_token  = "8733198d5b7d95ea6419871a042fb5c7"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.sms.messages.create(body="Hitesh please?! this is a test message <3",
    to="+12018905439",    # Replace with your phone number
    from_="+12018905439") # Replace with your Twilio number
print message.sid