from twilio.twiml.voice_response import VoiceResponse, Gather
from .mongodb import has_interacted_before
from config import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN
from twilio.rest import Client
from config import TWILIO_PHONE_NUMBER,NGROK_URL
twilio_client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
from flask import Flask, request, url_for
ngrok_url = NGROK_URL
import os
# static_dir = os.path.join(os.getcwd(), './static')

def handle_incoming_call(request_body):
    response = VoiceResponse()

    if not has_interacted_before(request_body['From']):
        # response.play("Welcome to Jorvana, AI therapist. Please register your phone number on our website.")
        response.play(url_for('static', filename=f'incomming_alert.mp3', _external=True))

        return str(response)

    # First, play the pre-recorded response
    response.play(url_for('static', filename=f'response.mp3', _external=True))
    gather = Gather(input='speech', action=f'https://{ngrok_url}/handle_speech1', timeout=10, speechTimeout='auto')
    response.append(gather)
    return str(response)

def initiate_call(phone_number):
    to_number = phone_number

    stat_url=url_for('static', filename=f'response.mp3', _external=True)
    # Initiate the call with correct TwiML
    call = twilio_client.calls.create(
        twiml=f'<Response><Play>https://{ngrok_url}/static/response.mp3</Play><Gather action="https://{ngrok_url}/handle_speech" input="speech" timeout="10" speechTimeout="auto"></Gather></Response>',
        to=to_number,
        from_=TWILIO_PHONE_NUMBER
    )

    return "Call initiated."



