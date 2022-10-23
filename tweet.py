from urllib import response
import tweepy #for tweets mining
from tweepy import Cursor
from csv import writer #for writing csv files
import pandas as pd #for data manipulation and analysis
import numpy as np #for performing mathematical operations
import matplotlib as mpl
import matplotlib.pyplot as plt #for visualization
import seaborn as sns #for visualization
import plotly.express as px #to make express plots in Plotly
from plotly.subplots import make_subplots #for making sub_plots
import plotly.graph_objects as go
#from textblob import TextBlob
import csv #to read and write csv files
import requests #to send requests
import re #for text manipulation
#import nltk #for text manipulation
#from nltk.tokenize import sent_tokenize, word_tokenize
#from nltk import pos_tag
#from nltk.corpus import stopwords #to get stopwords
#from nltk.tag.perceptron import PerceptronTagger
#from nltk.corpus import words
import string
import inspect
from PIL import Image #to embed image
import auth




# auth = tweepy.OAuthHandler(auth.access_key, auth.access_secret_key)
# auth.set_access_token(auth.access_token, auth.access_token_secret)

client = tweepy.Client(auth.bearer_token)

# api = tweepy.API(auth, wait_on_rate_limit=True)

query = "covid -is:retweet"

response = client.search_recent_tweets(query=query, max_results = 100)

#tweets = client.get_users_tweets(id="RealDekings", tweet_fields=['context_annotations','created_at','geo'])

for tweet in response.data:
    print(tweet.id)



# tweets = api.user_timeline(screen_name = "@RealDekings",
#                             #Get number of tweets
#                             count = 200,
#                             #Include retweets
#                             include_rts = False,
#                             #Get all the full text
#                             tweet_mode = 'extended')

# print(tweets)

# auth = tweepy.OAuth1UserHandler(auth.access_key, auth.access_secret_key, auth.access_token, auth.access_Token_secret)