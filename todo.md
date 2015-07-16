#To Do list for BirdyBot

At this point, mainly suggest ideas.

Implement some sort of DM response method.
Maybe a regexp match on a dict... E.G. If a message received by userstream matches an entry in a dict, send one of the subresponses for that entry.

Possibly link birdybot with chatterbot (
https://github.com/gunthercox/ChatterBot), 
have anything that doesn't directly match the dict get sent to it.
The concept of chatterbot is pretty neat, would be cool to have an importable module that gets birdybot and chatterbot working together, twitterbot being the messenger and chatterbot providing the responses.

Set up an OSUsername2twitter function that checks if .config/birdybot/config.py exists for the username given, and if so, what twitter ID that account belongs to.
The idea behind this is that a user (in a python script or other job) can call something like dm(username, recipient, message) and have birdybot automatically map that username (which should be their name) to their twitter credentials.
Better yet, don't even let the caller spesify a username, just check to see if the user that's running the script has those credentials stored.
Implement some sort of optional timeline logging for individual Linux / Unix users, maybe a .config/birdybot/keys.py and .config/birdybot/config.py files.
