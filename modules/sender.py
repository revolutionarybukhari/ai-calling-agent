from twilio.rest import Client
from config import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN

twilio_client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

def send_whatsapp_message(recipient, message):
    number="whatsapp:"+recipient
    twilio_client.messages.create(
        body=message,
        from_='whatsapp:+14155238886',  # Your Twilio WhatsApp number
        to=number
    )
