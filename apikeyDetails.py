import tweepy
import twitter

def keyDetails():
    api = twitter.Api(consumer_key='XXXX',
                  consumer_secret='XXXX',
                  access_token_key='XXXX',
                  access_token_secret='XXXX')
    return (api)
