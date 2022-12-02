"""
Function to send SMS to a cellphone number from Twilio number.

Created on Thu Jul 30 14:10:02 2022
Written by Jonathan De Sousa
"""

import os
from twilio.rest import Client

def send_SMS(destination: str, message: str):
    # Find account SID and Auth Token at twilio.com/console and set
    # as environment variables. See http://twil.io/secure
    account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
    auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
    client = Client(account_sid, auth_token)
    
    message = client.messages \
        .create(
             body=message,
             from_='+11111111111',
             to=destination
         )
    
    print(message.sid)