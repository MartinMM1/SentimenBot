import tweepy
from textblob import TextBlob

API_key='API_key'
API_secret='API_secret_key'

access_token='Access_key'
access_secret='Access_secret_key'

auth=tweepy.OAuthHandler(API_key,API_secret)
auth.set_access_token(access_token,access_secret)

api=tweepy.API(auth)

public_tweets=api.search_tweets('Desired Topic')

for tweet in public_tweets:
    print(tweet.text)
    analysis=TextBlob(tweet.text)
    print(analysis.sentiment)