# small utility to post tweets
import sys
from secrets import * # import app keys
from keys import * #import our user keys
auth = tweepy.OAuthHandler(c_key, c_secret) 
auth.set_access_token(key, secret)
api = tweepy.API(auth)
api.update_status()