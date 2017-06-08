#!/usr/bin/python
# -*- coding: utf-8 -*-

# Import the necessary package to process data in JSON format
import codecs
try:
    import json
except ImportError:
    import simplejson as json

# We use the file saved from last step as example
tweets_filename = 'twitter_stream_1000tweetsEN.txt'
tweets_filename2 = 'twitter_stream_1000tweetsEN2.txt'
tweets_file = codecs.open(tweets_filename, 'r', encoding = "utf-8")
tweets_file2 = codecs.open(tweets_filename2, 'w', encoding = "utf-8")

for line in tweets_file:
    try:
        # Read in one line of the file, convert it into a json object 
        tweet = json.loads(line.strip())
        if 'text' in tweet: # only messages contains 'text' field is a tweet
            print "\n\n\n"
            print tweet['id'] # This is the tweet's id
            tweets_file2.write(unicode(str(tweet['id'])+'\n','utf-8'))
            
            print tweet['created_at'] # when the tweet posted
            tweets_file2.write(unicode(str(tweet['created_at'])+'\n','utf-8'))
            
            print tweet['text'] # content of the tweet
            tweets_file2.write(unicode(tweet['text']+'\n','utf-8'))

            print tweet['user']['id'] # id of the user who posted the tweet
            tweets_file2.write(unicode(str(tweet['user']['id'])+'\n','untf-8'))
            
            print tweet['user']['name'] # name of the user, e.g. "Wei Xu"
            tweets_file2.write(unicode(str(tweet['user']['name'])+'\n','utf-8'))
            
            print tweet['user']['screen_name'] # name of the user account, e.g. "cocoweixu"
            tweets_file2.write(unicode(str(tweet['user']['screen_name'])+'\n','utf=8'))

            hashtags = []
            for hashtag in tweet['entities']['hashtags']:
            	hashtags.append(hashtag['text'])
            
            print hashtags
            tweets_file2.write(unicode(str(hashtags)+'\n','utf-8'))

            tweets_file2.write("\n\n\n")
    except:
        # read in a line is not in JSON format (sometimes error occured)
        continue