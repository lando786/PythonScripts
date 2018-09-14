import tweepy as tw
import time
import os

access_token = ''
access_secret = ''
consumer_key = ''
consumer_secret = ''
mins = 10 * 60
auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tw.API(auth)

os.chdir('images')
for img in os.listdir('.'):
    api.update_with_media(img)
    time.sleep(mins)