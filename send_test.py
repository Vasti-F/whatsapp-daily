import csv
import os
from twilio.rest import Client

# 1. Pon tus credenciales aquí o créalas como variables de entorno
ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID', 'TU_ACCOUNT_SID')
AUTH_TOKEN  = os.getenv('TWILIO_AUTH_TOKEN', 'TU_AUTH_TOKEN')

client = Client(ACCOUNT_SID, AUTH_TOKEN)
FROM_WHATSAPP = os.getenv('TWILIO_FROM', 'whatsapp:+14155238886')  # tu número de Sandbox de Twilio

def send_messages():
    with open('clients.csv', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            to_whatsapp = f"whatsapp:+{row['phone']}"
            body = (
                f"¡Hola {row['name']}! 📦\n"
                f"Tu pedido está programado para las {row['schedule']} en {row['address']}.\n\n"
                "Por favor confirma:\n"
                "1️⃣ Pago en efectivo\n"
                "2️⃣ Transferencia\n"
                "3️⃣ Reagendar"
            )
            message = client.messages.create(
                from_=FROM_WHATSAPP,
                to=to_whatsapp,
                body=body
            )
            print(f"Enviado a {row['name']} ({row['phone']}), SID: {message.sid}")

if __name__ == '__main__':
    send_messages()
