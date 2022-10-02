import tweepy
import pandas as pd
import json
from datetime import datetime
import auth





# Twitter Authentication
auth = tweepy.OAuth1UserHandler(auth.access_key, auth.access_secret_key, auth.access_token, auth.access_Token_secret)
#auth.set_access_token(access_token, access_Token_secret)

# Creating an API Object
api = tweepy.API(auth)

# user = api.get_user(screen_name = "@BBCSport")
# print(user.screen_name)
# print(user.followers_count)

tweets = api.user_timeline(screen_name = "@RealDekings",
                            #Get number of tweets
                            count = 200,
                            #Include retweets
                            include_rts = False,
                            #Get all the full text
                            tweet_mode = 'extended')

print(tweets)