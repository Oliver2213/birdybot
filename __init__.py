"""
Birdybot
----------------------------------
A set of scripts to make a twitter bot easier. One example is included in birdybot.py.
"""
import tweepy
import os
from secureconfig import SecureConfigParser
conffile = 'birdybot.conf'
confkey = 'birdybot.key'
#Checking if we have a key to open up the configuration file and extract sensitive values
if os.path.isfile(confkey)==False:
	#A key file isn't in current directory
	print "Error! No keyfile found in current directory! This means you won't be able to decrypt needed authorization information to access web services."
	sys.exit()
#If this is still running, it must exist
#So Enstantiate a config parser object with our key
config = SecureConfigParser.from_file(confkey)
# Check if we've got a config file
if os.path.isfile(conffile)==False:
	# No configuration files in current directory.
	print "Error! No configuration file found in current directory. Necessary API and access keys are not available. Exeting."
	sys.exit()
else: # Since it exists, load it
	config.read(conffile)
#Check if we've got API keys for Twitter:
if config.get('APIKeys', 'key') and config.get('APIKeys', 'secret'):
	if config.get('tokens','access') and config.get('tokens','secret'):


