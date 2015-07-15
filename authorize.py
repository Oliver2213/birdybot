# Birdybot authorization thing.
import tweepy
from secrets import *
print "Obtaining authorization URL..."

auth = tweepy.OAuthHandler(c_key, c_secret)
authURL = auth.get_authorization_url()
print "URL retrieved!"
print "Please use the following URL to get Birdybot authorized:"
print authURL