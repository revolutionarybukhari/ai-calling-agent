from openai import OpenAI
from config import OPENAI_API_KEY,NGROK_URL
ngrok_url=NGROK_URL
import requests
client = OpenAI(api_key=OPENAI_API_KEY)

# def synthesize_speech(text, filename="answer"):
#     """
#     Converts text to speech using OpenAI's TTS and saves it as an MP3 file.

#     :param text: Text to be converted to speech.
#     :param filename: Name of the file to save the audio to.
#     :return: Path to the saved audio file.
#     """
#     try:
#         response = client.audio.speech.create(
#             model="tts-1",
#             voice="alloy",
#             input=text,
#         )
#         response.stream_to_file(f"./static/{filename}.mp3")
#         return filename
#     except Exception as e:
#         print(f"Error in generating speech: {e}")
#         return None

def synthesize_speech(text, filename="answer"):
    """
    Converts text to speech using OpenAI's TTS and saves it as an MP3 file.

    :param text: Text to be converted to speech.
    :param filename: Name of the file to save the audio to.
    :return: Path to the saved audio file.
    """
    try:
        CHUNK_SIZE = 1024
        url = "https://api.elevenlabs.io/v1/text-to-speech/EXAVITQu4vr4xnSDxMaL"

        headers = {
        "Accept": "audio/mpeg",
        "Content-Type": "application/json",
        "xi-api-key": "5a35---4a178"
        }

        data = {
        "text": text,
        "model_id": "eleven_turbo_v2",
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.5
        }
        }

        response = requests.post(url, json=data, headers=headers)
        with open(f"./static/{filename}.mp3", 'wb') as f:
            for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
                if chunk:
                    f.write(chunk)
        return filename
    except Exception as e:
        print(f"Error in generating speech: {e}")
        return None
