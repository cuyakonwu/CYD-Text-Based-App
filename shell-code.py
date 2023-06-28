#Import Flask and Twilio Libraries
from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse

#Initialize the app in flask
app = Flask(__name__)


@app.route('/bot', methods=['POST'])
def bot():
    #Stores the incoming message as lower case
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    responded = False

    """
    Set a string of conditionals that access a website
    Once the message is answered, responded is set to True
    """

    if not responded:
        msg.body('I only know about famous quotes and cats, sorry!')
    return str(resp)


if __name__ == '__main__':
    app.run(port=4000)