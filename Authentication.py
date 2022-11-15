import tweepy
from dotenv import load_dotenv
import os

load_dotenv()


consumer_key = os.getenv("consumer_key")  #CONSUMER API TOKEN
consumer_secret = os.getenv("consumer_secret") #SECRET TOKEN API
access_token = os.getenv("access_token") #ACESS TOKEN
access_token_secret = os.getenv("access_token_secret") #ACESS TOKEN SECRET
bearer_token = os.getenv("bearer_token") #BEARER TOKEN

# Authenticate to Twitter

def client_auth():
    client = tweepy.Client(
        consumer_key=consumer_key,
        consumer_secret=consumer_secret,
        access_token=access_token,
        access_token_secret=access_token_secret,
        bearer_token=bearer_token
    )
    return client

client = client_auth()

#Autenticacao parametros

def autenticacao():
    autentication = {
    'consumer_key' : consumer_key,
    'consumer_secret' : consumer_secret,
    'access_token' : access_token,
    'access_token_secret' : access_token_secret,
    'bearer_token' : bearer_token,
}
    return autentication