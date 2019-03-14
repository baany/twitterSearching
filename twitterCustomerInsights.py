import csv
import tweepy
import twitter
from apikeyDetails import keyDetails

api = keyDetails()

results = api.GetSearch(raw_query="q=Artificial%20Intelligence%20&result_type=recent&count=1000")
#public_tweets = api.home_timeline()
with open("GeneratedDoc.txt", "a") as myFile:
    for tweet in results:
        print (tweet.text)
        myFile.write(tweet.text+"\n")
myFile.close()
