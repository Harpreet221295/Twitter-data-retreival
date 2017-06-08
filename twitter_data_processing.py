#!/usr/bin/python
# -*- coding: utf-8 -*-

# Import the necessary package to process data in JSON format
import io
import tweet_clean as tc
import codecs
try:
    import json
except ImportError:
    import simplejson as json

encoding = 'utf-8'

raw_tweet_file_name = "F:\MainDesktop\Text mining\response_GetFreWords.json"
intermediate_tweet_file_name = "F:\MainDesktop\Text mining\GetFreWords_text.txt"
processed_tweet_file_name = "F:\MainDesktop\Text mining\GetFreWords_processed_tweets_file.txt"

tweets_file = open(raw_tweet_file_name.encode('string-escape'), 'r')
tweets_file2 = open(intermediate_tweet_file_name.encode('string-escape'), 'w')

count=0

tweet_dataset=[]

for line in tweets_file:
    
    
    
    try:
        # Read in one line of the file, convert it into a json object 
        tweet = json.loads(line.strip())
        if 'text' in tweet: # only messages contains 'text' field is a tweet
#           
            processed_tweet = tc.Remove_AlphaNumeric(tweet['text'])
            processed_tweet = tc.Remove_Punctuation(processed_tweet)
            processed_tweet = tc.Remove_Emoji(processed_tweet)
            
            if processed_tweet is not None:
                processed_tweet = processed_tweet + "\n"
                tweets_file2.write(processed_tweet.encode('utf-8'))
#
#            tweets_file2.write("\n\n\n")
    except:
        # read in a line is not in JSON format (sometimes error occured)
        continue
    
    


tweets_file.close()
tweets_file2.close()



#tc.clean_tweet_by_frequency(intermediate_tweet_file_name, processed_tweet_file_name)
#tweet_corp = [twt.split() for twt in tweet_dataset]
#
#for twt in tweet_corp:
#    for word in twt:
#        print word.decode('utf-8')
        
        
