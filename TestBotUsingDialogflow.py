from flask import Flask, request
from datetime import datetime
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

today = datetime.now()

@app.route('/') # this is the home page route
def hello_world(): # this is the home page function that generates the page code
    ret_str = str(today) + "      Hello World"
    return ret_str

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    print (req)
    fulfillmentText = ''
    sum = 0
    query_result = req.get('queryResult')
    print(query_result)
    user_response=req['queryResult']['queryText']
    bot_response=req['queryResult']['fulfillmentText']
    print(user_response)
    print(bot_response)
    return "Done!"


if __name__ == '__main__':
    app.run(debug=True) # This line is required to run Flask on repl.it