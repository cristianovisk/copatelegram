#!/usr/bin/env python2.7

import requests
import time
import telepot

telegram=telepot.Bot('CODE_BOT_TELEGRAM')
destiny='YOUR_ID_CHAT'
ultim_jogo=''
flag=''

#CHECK WEBSERVER COPA ------------------------------------
def check():
    jogos = requests.get('http://worldcup.sfg.io/matches').json()
    resp=list
    flag=ultim_jogo
    for jogo in jogos:
        if jogo['status'] in ('completed', 'in progress'):
            resp=(jogo['home_team']['country'],
                   jogo['home_team']['goals'], 'x',
                   jogo['away_team']['country'],
                   jogo['away_team']['goals'])
    return resp;
while True:
    ultim_jogo=(str(check()).replace(',','').replace('(','').replace(')','').replace("'",""))
    if flag == ultim_jogo:
    	print ("Goool!!!")
    	print (ultim_jogo)
        telegram.sendMessage(destiny, ultim_jogo, disable_web_page_preview=True)
    else:
    	print ("Nothing... Sleep 15...")
    	print (ultim_jogo)
    	time.sleep(15)