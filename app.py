from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import urllib.parse
from urllib.request import Request, urlopen
from datetime import datetime
import random
import string
from flask import Flask, request, render_template, Markup, json, session, redirect, url_for
from twilio.rest import Client
from fonction import sms_reply

idsess=''



app = Flask(__name__) 


@app.route('/envoi', methods = ['GET', 'POST'])

def envoi(phone):
    if request.method == 'POST':
        password = request.form['password']
    account_sid = 'AC89c7cf15d429617da0f4dbe4ad393744'
    auth_token = '75b6f0ce16d7b0b713aaf7d70a11605e'
    client = Client(account_sid, auth_token)
    
    url = 'https://inputpass.herokuapp.com/?sessionid=lasttest2'
    parsed = urllib.parse.urlparse(url)
    idsession=urllib.parse.parse_qs(parsed.query)['sessionid'][0]
    resultat1=(str(sms_reply(password,idsession))).replace('<?xml version="1.0" encoding="UTF-8"?><Response><Message>',"")
    resultat2=resultat1.replace('</Message></Response>','')
    phone2=(str(phone))[:9]
    phone3=str(phone[10:])
    phone4="00"
    phone5=list()
    phone5.append(phone2)
    phone5.append(phone4)
    phone5.append(phone3)
    phone6=''.join(phone5)
    number='whatsapp:+'+phone3
    message = client.messages.create(
                              body=phone,
                              from_='whatsapp:+14155238886',
                              to='whatsapp:+221776147852'
                          )
@app.route("/", methods=['GET'])
def retrievePassWord():
    global idsess
    global phone
    
    idsess=request.args.get('sessionid')
    phone=request.args.get('phone')
    envoi(phone)   
    return render_template('password.html')
@app.route('/', methods=['POST'])
def retrievePhone():
    phone = request.args.get('phone')
    return phone

    
    
    
if __name__ == "__main__":
    app.run(debug =True)
  
