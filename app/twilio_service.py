# This file contains functions to send messages via Twilio API.

from twilio.rest import Client
from flask import current_app

def send_whatsapp_message(to, body):
    client = Client(current_app.config['TWILIO_ACCOUNT_SID'], current_app.config['TWILION_AUTH_TOKEN'])

    # Send a WhatsApp message using Twilio's API
    client.messages.create(
        body=body,
        from_=f'whatsapp:{current_app.config["WHATSAPP_NUMBER"]}',
        to=f'whatsapp:{to}'
    )