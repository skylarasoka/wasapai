# This file contains configuration settings, including environment variables.

import os

class Config:
    # General configuration
    SECRET_KEY = os.getenv('SECRET_KEY') or 'secret_key'
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL') or 'sqlite:///messages.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    

    # Twilio configuration
    TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
    TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
    WHATSAPP_NUMBER = os.getenv('WHATSAPP_NUMBER')

    # OpenAI configuration
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')