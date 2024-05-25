# This file defines the routes for handling incoming webhooks and processing messages.

from flask import Blueprint, request, jsonify
from .openai_service.py import get_openai_response
from .twilio_service import send_whatsapp_message
from .models import db, Message

bp = Blueprint('routes', __name__)

@bp.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()

    #Check if the 'messages' key exists in the payload
    if data.get('messages'):
        message = data['messages'][0]

        if message.get('type') == 'text':
            user_message = message['text']['body']
            sender = message['from']
            prompt = generate_prompt(user_message)
            response = get_openai_response(prompt)
            send_whatsapp_message(sender, response)

            # Save the message to the database.
            msg = Message(sender=sender, message=user_message, response=response)
            db.session.add(msg)
            db.session.commit()

    return jsonify({'status': 'received'})
  

def generate_prompt(user_message):
    # Generates a response prompt based on the user's message.
    if "price" in user_message or "cost" in user_message:
        if "Island A" in user_message:
            price = boat_info["routes"]["Island A"]["price"]
            return f"The price to Island A is MYR{price}."
        elif "Island B" in user_message:
            price = boat_info["routes"]["Island B"]["price"]
            return f"The price to Island B is MYR{price}."
    return f"The user asked: {user_message}\nRespond as a helpful assistant for a boat booking service:" 
