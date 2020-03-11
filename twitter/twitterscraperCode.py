# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 12:45:02 2019

@author: babas
"""
from twitterscraper import query_tweets
import pandas as pd
import csv
csvFile = open('getiphone.txt', 'a')
csvWriter = csv.writer(csvFile)

for tweet in query_tweets(["iphone And sustainability"]):
    print(tweet.text.encode('utf-8'))
    csvWriter.writerow([tweet.text.encode('utf-8')])
