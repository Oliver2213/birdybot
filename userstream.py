# Small utility to stream for the user that's authenticated
# Triggers and other stuff coming later
import tweepy
from secrets import * # import app keys
from keys import * #import our user keys
# do auth stuff
auth = tweepy.OAuthHandler(c_key, c_secret) 
auth.set_access_token(token, token_secret)
api = tweepy.API(auth) # Get our API object

class StdOutListener(tweepy.StreamListener):
    def on_connect( self ):
        print("Connection to twitter established!!")

    def on_disconnect( self, notice ):
        print("Connection to twitter lost!! : ", notice)

    def on_status( self, status ):
        print(status)
        return True

    def on_direct_message(self, status):
        print("Direct message received.")
        try:
            print(status.direct_message['sender_screen_name']+" says, \""+status.direct_message['text']+"\"")
            return True
        except BaseException as e:
            print("Failed on_direct_message()", str(e))

    def on_error( self, status ):
        print(status)


def main():

    try:
        print "Starting userstream for "+api.me().name
        stream = tweepy.Stream(auth, StdOutListener())
        stream.userstream()

    except KeyboardInterrupt:
        print('goodbye!')
if __name__ == '__main__':
    main    ()