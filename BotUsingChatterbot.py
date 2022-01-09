# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from datetime import datetime
from chatterbot.trainers import ChatterBotCorpusTrainer
from pyngrok import ngrok
from os.path import exists


today = datetime.now()


###############################################################
######  open http channel via ngrok
###############################################################
#http_channel = ngrok.connect()
#ssh_tunnel = ngrok.connect(4041,'http')
#
#tunnels=ngrok.get_tunnels()
#print("ngrok tunnel = " +str(tunnels))
#
###############################################################
######      Bot internal logic
###############################################################

###Create a new chat bot
chatbot = ChatBot("Tushar")

trainer = ChatterBotCorpusTrainer(chatbot)
#trainer.train(conversation)

##### Chatbot Training Through Local Corpus
##### Corpus github repo : https://github.com/gunthercox/chatterbot-corpus.git
trainer.train(
    "../../chatterbot-corpus/chatterbot_corpus/data/marathi/conversations.yml",
    "../../chatterbot-corpus/chatterbot_corpus/data/marathi/greetings.yml"
)

###############################################################
###############################################################


###############################################################
####         Messaging interface
###############################################################
app = Flask(__name__)


@app.route("/")
def index():
    ret_str = str(today) + "BotUsingChatterbot: Hello World!!!"
    return ret_str


@app.route("/sms1", methods=['POST'])
def reply():
    msg = request.form.get('Body')
    if msg.lower() == "hello":
        reply = "Hello! \n How can i help you?"
    else:
        reply=str(chatbot.get_response(msg))
    #else:
    #    reply = msg
    response = MessagingResponse()
    response.message(reply)

    return str(response)

###############################################################
###############################################################

if __name__ == "__main__":
    app.run(debug=True)
