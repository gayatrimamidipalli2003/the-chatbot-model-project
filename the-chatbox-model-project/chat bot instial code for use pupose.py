import os
from twilio.rest import Client
from flask import Flask, request

app = Flask(__name__)

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

@app.route('/bot', methods=['POST'])
def bot():
    incoming_message = request.values.get('Body', '').lower()
    response = 'Hi there! Thanks for messaging me.'
    message = client.messages.create(
        body=response,
        from_='whatsapp:+14155238886',
        to=request.values.get('From')
    )
    return str(message.sid)

if __name__ == '__main__':
    app.run()
