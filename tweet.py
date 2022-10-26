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

csvFile = open('result.csv', 'a')

#Use csv writer
csvWriter = csv.writer(csvFile)



client = tweepy.Client(auth.bearer_token)

query = "covid -is:retweet"

response = client.search_recent_tweets(query=query, max_results = 100)


for tweet in response.data:

    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
    print(tweet.text)

csvFile.close()
