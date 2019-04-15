from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import urllib.parse
from urllib.request import Request, urlopen
from datetime import datetime
import random
import string


sessionid="lasttest2"#datetime.now().strftime("%d-%b-%Y-%H:%M:%S.%f") 


def sms_reply():
    
    
     
    phone_no = request.form.get('From')
    msg = request.form.get('Body')
    resp = MessagingResponse()
    global sessionid
    
    
    
   
    headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) ' 
                      'AppleWebKit/537.11 (KHTML, like Gecko) '
                      'Chrome/23.0.1271.64 Safari/537.11',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding': 'none',
        'Accept-Language': 'en-US,en;q=0.8',
        'Connection': 'keep-alive'
        }
    req = Request('https://cg-bgfimobileussd.chakamobile.com/mtncg/requests', headers=headers)
    params={
    "sessionid":sessionid,
    "msisdn":"242055565990",
    "input":msg
            }
    
    query_string=urllib.parse.urlencode(params)
    data=query_string.encode("ascii")
    with urllib.request.urlopen(url=req,data=data) as response:
        
        response_text=response.read()
        header=response.headers
        
            
   
        response_text_str=str(response_text)
        liste=response_text_str.split("\\n")
    
    
        liste.remove("'")
        chaine=""
        for i in range(len(liste)):
            chaine+=liste[i]+"\n"
        
        
        resp.message(str(chaine.replace("b'","")))
        if(str(resp).__contains__("-Nouveau Solde")):
            return str(resp)+str("\n\n 00: MENU PRINCIPAL")
        

    
   
        return str(resp)
    


        
    
        


    
