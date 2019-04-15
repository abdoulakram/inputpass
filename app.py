from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import urllib.parse
from urllib.request import Request, urlopen
from datetime import datetime
import random
import string
from flask import Flask, jsonify, request, render_template, Markup, json, session, redirect, url_for
from twilio.rest import Client
from fonction import sms_reply
app = Flask(__name__)


@app.route("/", methods=['GET','POST'])

def retrievePassWord():
    return render_template('password.html')

@app.route('/envoi', methods = ['GET', 'POST'])

def envoi():
    if request.method == 'POST':
        password = request.form['password']
    account_sid = 'AC89c7cf15d429617da0f4dbe4ad393744'
    auth_token = '75b6f0ce16d7b0b713aaf7d70a11605e'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
                              body=str(sms_reply(password)),
                              from_='whatsapp:+14155238886',
                              to='whatsapp:+221776147852'
                          )
    
    
if __name__ == "__main__":
    app.run(debug =True)
  
