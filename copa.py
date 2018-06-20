#!/usr/bin/env python2.7

import requests
import time
import telepot

telegram=telepot.Bot('TOKEN_BOT_TELEGRAM')
destiny='CHATID_RECEIVER'
ultim_jogo=''
flag=''
if destiny == 'CHATID_RECEIVER':
    print ("Change variable 'destiny' with CHATID and 'telegram' with TOKEN_BOT in code.")
    exit()    

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

def flag_check(ultim_jogo):
    flag=ultim_jogo
    return flag;

while True:
    flag=flag_check(ultim_jogo)
    ultim_jogo=(str(check()).decode('utf-8').replace(',','').replace('(','').replace(')','').replace("'","").replace('x u', 'x '))
    ultim_jogo=("xs %s" %ultim_jogo).replace('xs u', '')

    if flag != ultim_jogo:
    	print ("Goool!!!")
    	print (ultim_jogo)
        telegram.sendMessage(destiny, ultim_jogo, disable_web_page_preview=True)
    else:
    	print ("Nothing... Sleep 15...")
    	print (ultim_jogo)
    	time.sleep(15)
