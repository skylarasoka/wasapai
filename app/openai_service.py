# This file contains functions to interact with OpenAI breakpoint

import openai
from flask import current_app

def get_openai_response(prompt);
    openai.api_key = current_app.config['OPENAI_API_KEY']

    # Generate a response from OpenAI based on the prompt.
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    return response.choice[0].text.strip()

