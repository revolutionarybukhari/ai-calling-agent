from flask import Flask, request, url_for
from modules.twilio_api import handle_incoming_call
from modules.twilio_api import initiate_call
from flask import jsonify
from twilio.twiml.voice_response import VoiceResponse, Gather
from config import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN , NGROK_URL
from twilio.rest import Client
from modules.chatbot import get_chatbot_response_agent,get_chatbot_response
from modules.tts import synthesize_speech
import os
from datetime import datetime
from flask_cors import cross_origin
from flask_cors import CORS
twilio_client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
static_dir = os.path.join(os.getcwd(), './static')

app = Flask(__name__)
ngrok_url=NGROK_URL
CORS(app, resources={r"/*": {"origins": "*", "methods": ["GET", "POST", "OPTIONS"], "allow_headers": ["Authorization", "Content-Type"]}})

@app.route('/', methods=['GET'])
def index():
    response_data = {
        "message": "Welcome to the AI calling agent Bot API Ver-1.2.2",
        "status": "success",
    }
    return jsonify(response_data)

@app.route('/voice', methods=['POST'])
@cross_origin(origin='*', headers=['Content-Type', 'Authorization'])

def voice():
    return handle_incoming_call(request.values)

@app.route('/response_audio', methods=['POST', 'GET'])
@cross_origin(origin='*', headers=['Content-Type', 'Authorization'])

def response_audio():
    response = VoiceResponse()
    response.play(url_for('static', filename='response.mp3', _external=True))
    return str(response)

@app.route('/make_call', methods=['GET'])
@cross_origin(origin='*', headers=['Content-Type', 'Authorization'])

def make_call():
    phone_number = request.args.get('phone_number')
    if phone_number:
        call_status = initiate_call(phone_number)
        return jsonify({"message": "Call initiated to " + phone_number, "status": call_status})
    else:
        return jsonify({"error": "Phone number is required"}), 400

@app.route('/handle_speech', methods=['POST','GET'])
@cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
def handle_speech():
    request_body = request.values
    response = VoiceResponse()
    if 'SpeechResult' in request_body:
        user_speech = request_body['SpeechResult']
        user_phone = request_body.get('To') 
        # Now call get_chatbot_response with both arguments
        chat_response = get_chatbot_response(user_speech, user_phone)
        audio_filename = synthesize_speech(chat_response, f"response_{datetime.now().timestamp()}")
        print("Audio generated")
        # Play the audio file
        try:
            response.play(url_for('static', filename=f'{audio_filename}.mp3', _external=True))
            if 'goodbye' in user_speech.lower():
                # If the user says "goodbye," end the call
                response.say("Thank you for using us. Goodbye!")
                response.hangup()
        except Exception as e:
            print(f"Error in playing audio file: {e}")
        # Use Twilio's Say verb for TTS
        # response.say(chat_response)
        if 'goodbye' in user_speech.lower():
            # If the user says "goodbye," end the call
            response.say("Thank you for using us. Goodbye!")
            response.hangup()
        
        gather = Gather(input='speech', action=f'https://{ngrok_url}/handle_speech', timeout=10, speechTimeout='auto')
        # response.say(chat_response, voice='Polly.Olivia-Neural')
        response.append(gather)
        # try:
        #     os.remove(f'{static_dir}/{audio_filename}.mp3')
        # except Exception as e:
        #     print(f"Error in deleting audio file: {e}")

    return str(response)

@app.route('/handle_speech1', methods=['POST','GET'])
@cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
def handle_speech1():
    request_body = request.values
    response = VoiceResponse()
    if 'SpeechResult' in request_body:
        user_speech = request_body['SpeechResult']
        user_phone = request_body.get('From') 
        # Now call get_chatbot_response with both arguments
        chat_response = get_chatbot_response(user_speech, user_phone)
        audio_filename = synthesize_speech(chat_response, f"response_{datetime.now().timestamp()}")
        print("Audio generated")
        # Play the audio file
        try:
            response.play(url_for('static', filename=f'{audio_filename}.mp3', _external=True))

        except Exception as e:
            print(f"Error in playing audio file: {e}")
        # Use Twilio's Say verb for TTS
        # response.say(chat_response)
        if 'goodbye' in user_speech.lower():
            # If the user says "goodbye," end the call
            response.say("Thank you for using us. Goodbye!")
            response.hangup()
        
        gather = Gather(input='speech', action=f'https://{ngrok_url}/handle_speech1', timeout=10, speechTimeout='auto')
        # response.say(chat_response, voice='Polly.Olivia-Neural')
        response.append(gather)
        # try:
        #     os.remove(f'{static_dir}/{audio_filename}.mp3')
        # except Exception as e:
        #     print(f"Error in deleting audio file: {e}")

    return str(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True, threaded=True)
