import tweepy
import time
from Authentication import autenticacao,client_auth

auth_token = autenticacao()

client_a = client_auth()


auth = tweepy.OAuth1UserHandler(auth_token['consumer_key'],auth_token['consumer_secret'],
                                auth_token['access_token'],auth_token['access_token_secret'])
api = tweepy.API(auth)


termos = ['Python','Programming','Code']   #TERMOS PARA FILTRO

termo = 'Python'

class Streaming(tweepy.StreamingClient):
    def on_connect(self):
        print('Prontinho, meu patrão.')

    def on_tweet(self, tweet):
        if tweet.referenced_tweets == None:
            tweet_text = tweet.text
            print(tweet_text)
            tweet_id = tweet.id
            tt = tweet_text.split(' ')
            prv = set(tt) & set(termos)
            prv = str(prv)
            if prv == 'set()':
                client_a.retweet(tweet_id=tweet_id, user_auth=True)
                print('Retweet efetuado com sucesso')
            else:
                print('Esse tweet não segue as regras')


            time.sleep(0.2)

stream = Streaming(bearer_token=auth_token['bearer_token'])


#print(stream.get_rules()) #LIST ACTIVE RULES

#stream.delete_rules(id='id_rule') #DELETE RULE

#stream.add_rules(tweepy.StreamRule(termo)) #ADD NEW RULE

stream.filter(tweet_fields=['referenced_tweets'])


