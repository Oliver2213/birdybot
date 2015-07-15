# Birdybot authorization thing.
import tweepy
from secrets import *
print "Obtaining authorization URL..."

auth = tweepy.OAuthHandler(c_key, c_secret)
authURL = auth.get_authorization_url()
print "URL retrieved!"
print "Please use the following URL to get Birdybot authorized:"
print authURL
print "Once you have verifyed Birdybot, please return here and enter the pin twitter gives you."
print "Pin:"
pin = raw_input().strip()
tokens = auth.get_access_token(verifier=pin)
tokenfile= open("keys.py","w")
tokenfile.write(tokens[0]+'\n')
tokenfile.write(tokens[1]+'\n')
tokenfile.close()
print "The tokens should now be saved in secrets.py"