#! /usr/bin/env python

import tweepy

# consumer_key = "YOUR CONSUMER KEY"
# consumer_secret = "YOUR CONSUMER SECRET"
# access_secret = "YOUR ACCESS SECRET"
# access_token = "YOUR ACCESS TOKEN"

consumer_key = ""
consumer_secret = ""

access_token = ""
access_secret = ""

if not all((consumer_key, consumer_secret, access_token, access_secret)):
    print "[-] The Keys and Tokens must not be empty."
    exit()

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)

uids = []
user = []

for tweet in tweepy.Cursor(
    api.search,
    
    # Hashtag looking for in tweets
    q = "#",
    
    # Country code
    lang = "",
    
    # Geo data i.e. "38.8976760,-77.0365300,10km"
    geocode = "",    
    ).items():
    uids.append(tweet.author.id)

for uid in uids:
    tuser = api.get_user(uid)
    tuser = tuser.screen_name
    user.append(tuser)

# Remove duplicates
user = set(user)

if len(user) > 0:
    print "[*] Found {0} Twitter user: ".format(len(user))
    for e in user:
        print e