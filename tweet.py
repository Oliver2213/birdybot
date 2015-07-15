# small utility to post tweets
import sys
import tweepy
from secrets import * # import app keys
from keys import * #import our user keys
# do auth stuff
auth = tweepy.OAuthHandler(c_key, c_secret) 
auth.set_access_token(token, token_secret)
api = tweepy.API(auth)
# form our tweet
tweet = sys.argv[1]
api.update_status("testing...")