"""
Birdybot
----------------------------------
A set of scripts to make a twitter bot easier. One example is included in birdybot.py.
"""
import tweepy
import os
from secrets import c_key, c_secret
from keys import token, token_secret

def get_api():
    """authenticates the user. Returns a twitter.API instance."""
    auth = tweepy.OAuthHandler(c_key, c_secret)
    auth.set_access_token(token, token_secret)
    api = tweepy.API(auth)
    return api
def get_auth():
    """function to get the tweepy auth object for the keys imported."""
    auth = tweepy.OAuthHandler(c_key, c_secret)
    auth.set_access_token(token, token_secret)
    return auth
