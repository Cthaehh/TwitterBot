import tweepy
import time


#RTWEET ACCOUNT MENTIONS

from Authentication import client_auth

client_a = client_auth()

def tweet():
    tw = client_a.get_users_mentions(id='ID ACCOUNT',user_auth=True).data
    termos = ['TERMS', 'FILTER',]

    rt = str(tw)
    rt = rt.split('>')
    for t in rt:
        lista = []
        try:
            t = t.split(' ')
            id = t[2]
            id_tt = id.removeprefix('id=')
            tt = t[4:]
            for word in tt:
                word = word.replace("'","")
                lista.append(word)

            prov = set(lista) & set(termos)
            prov = str(prov)

            if prov == 'set()':
                client_a.retweet(tweet_id=id_tt, user_auth=True)
                print('Retweet efetuado com sucesso')
            else:
                print('Esse tweet não segue as regras')
        except:
            pass









