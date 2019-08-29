#Charlie Ansell 
#K00203841
#This file extracts tweets and all subsets of the tweets and stores them in a csv file in  a readable dataframe format, the tweets are analysed and read back using the JSON
#format, the top 10 sorted tweets are then printed to stdout

import pandas as pd
import numpy as np
import tweepy
import json
import csv

consumer_key = 'Enter your twitter consumer_key here'
consumer_secret = 'Enter your twitter consumer_key here'  #Authentication keys
access_token = 'Enter your twitter access_token here'
access_secret = 'Enter your twitter access_secret here'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret) #create authentcation handler

auth.set_access_token(access_token, access_secret) #set access tokens to connect to twitter dev account

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True) #consume tweepy api function, 

tweets = api.user_timeline('kingdomhearts', count=100) #get users timeline name 

collected_tweets_list = [] #create an empty list structure to hold collected tweets
for each_tweet in tweets:
    collected_tweets_list.append(each_tweet._json) #loop through tweets, store each json tweet in our list 
with open('tweets.csv', 'w') as file:
 file.write(json.dumps(collected_tweets_list, indent=4)) #write the json format of the tweets to an excel file

tweet_list = [] #list to hold processed tweets from json
sortedValues = [] #array to hold sorted data 

with open('tweets.csv', encoding='utf-8') as csvFile:  
  all_data = json.load(csvFile)  #we open the json file and loop through it
  for json_tweet_data in all_data: #we assign identifiers to variables so json knows what to parse into these variables when looking through the tweets excel file
   tweet_id = json_tweet_data['id']
   text = json_tweet_data['text']
   favorite_count = json_tweet_data['favorite_count']
   retweet_count = json_tweet_data['retweet_count']
   created_at = json_tweet_data['created_at']
   lang= json_tweet_data['lang']
   user=json_tweet_data['user']
   place = json_tweet_data['place']
   coordinates = json_tweet_data['coordinates']
   geo = json_tweet_data['geo']
   favorited = json_tweet_data['favorited']
   retweeted = json_tweet_data['retweeted']
   entities = json_tweet_data['entities']
   in_reply_to_user_id = json_tweet_data['in_reply_to_user_id']
   in_reply_to_user_status_id = json_tweet_data['in_reply_to_status_id_str']
   tweet_list.append({'tweet_id': str(tweet_id), #add our processed values to our tweets_list along with identifiers
                             'text': str(text),
                             'favorite_count': int(favorite_count),
                             'retweet_count': int(retweet_count),
                             'created_at': created_at,
							 'lang':str(lang),
							 'user':str(user),
							 'place':str(place),
							 'coordinates':str(coordinates),
							 'geo':str(geo),
							 'favorited':str(favorited),
							 'retweeted':str(retweeted),
							 'entities':str(entities),
							 'in_reply_to_user_id':str(in_reply_to_user_id),
							 'in_reply_to_user_status_id_str':str(in_reply_to_user_status_id)
                            })
   sortedValues.append({ #add our processed values to our tweets_list along with identifiers
                     'text': str(text),
                     'favorite_count': int(favorite_count), 
                     'retweet_count': int(retweet_count)					 
                            })	
   print(tweet_list) # print our list of data gathered & processed 
   tweet_json = pd.DataFrame(tweet_list, columns =  #create pandas dataframe and insert our processed tweet_list in order with identifiers for ease of readiness
                                  ['tweet_id', 'text', 
                                   'favorite_count', 'retweet_count', 
                                   'created_at','language','user','place','coordinates','geo','favorited','retweeted','entities','in_reply_to_user_id','in_reply_to_user_status_id'])	
outputFileName = 'tweetsOutput.csv' #set our ouput file name for ouputting processed dataframe to excel file 
tweet_json = tweet_json.sort_values(by=['favorite_count','retweet_count']) #sort datafame by fav count and retweet count and update dataframe with this sorted model
tweet_json.to_csv(outputFileName, encoding='utf-8', index=False)	#write dataframe to excel file	


print(sortedValues)						
sortedDf = pd.DataFrame(sortedValues, columns =   # create a dataframe to store sorted data values
['text', 'favorite_count' , 'retweet_count'])
sortedDf = sortedDf.sort_values(by=['favorite_count','retweet_count']) #sort datafame by fav count and retweet count and update dataframe with this sorted model
print(sortedDf.head(10)) #print top 10 sorted values out of tweets in dataframe
