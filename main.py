# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)


@app.route("/")
def index():
    ret_str = "Hello, World!\nThis is Tushar\n i am here!!! \n using Pycharm"
    return ret_str


@app.route("/sms1", methods=['POST'])
def reply():
    msg = request.form.get('Body')
    if msg.lower() == "hello":
        reply = "Hello! \n How can i help you?"
    else:
        reply = msg
    response = MessagingResponse()
    response.message(reply)

    return str(response)


if __name__ == "__main__":
    app.run(debug=True)
