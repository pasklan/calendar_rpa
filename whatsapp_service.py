import os
from dotenv import load_dotenv
from twilio.rest import Client


# Carrega variáveis de ambiente a partir do arquivo .env
load_dotenv()

TWILIO_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_WHATSAPP_FROM = os.getenv("TWILIO_WHATSAPP_NUMBER")
TWILIO_WHATSAPP_TO = os.getenv("MY_WHATSAPP_NUMBER")

def send_whatsapp_message(message):
    '''
    Envia uma mensagem via Whatsapp usando Twilio
    '''
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    message = client.messages.create(
        from_=TWILIO_WHATSAPP_FROM,
        body=message,
        to=TWILIO_WHATSAPP_TO
    )

    print(f"Mensagem enviada com sucesso: {message.sid}")

if __name__ == "__main__":
    send_whatsapp_message("Testando mensagem via Twilio!")

