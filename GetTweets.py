#!/usr/bin/python
# -*- coding: utf-8 -*-
try:
    import json
except ImportError:
    import simplejson as json
import tweepy
from httplib import IncompleteRead

consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""
MAXTWEETS  = 30
MaxFreqHindiWords_filename = "F:\MainDesktop\Text mining\MostFreqHindiWords.txt"
response_filename = "F:\MainDesktop\Text mining\response_GetFreWords_final.json"


class MyStreamListner(tweepy.StreamListener):

    def __init__(self, api=None):
        super(MyStreamListner, self).__init__()
        self.num_tweets = 0

    def on_data(self, data):
        
        #try:
        with open(response_filename.encode('string-escape'), 'a') as f:
            f.write(data)
        #except BaseException as e:
           # print str(e)
        
        
        dec = json.loads(data)

        
        if self.num_tweets < MAXTWEETS:
            
            if 'text' in dec:
                str_text = dec['text'].encode("utf-8")
                index = self.num_tweets+1
                print "[" + str(index) + "]" + str_text+"\n*************************"
                self.num_tweets+=1
                return True

        else:
            return False

    def on_error(self, status):
        print status



#public_tweets = api.home_timeline( count = 50)
#vir = api.user_timeline(screen_name = "thevirdas", count=5)

#for tweet in vir:
#    print tweet.text
#    print "\n\n"

def StartStreamming():
    lis = MyStreamListner()
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    #api = tweepy.API(auth)

    

    cord_UP = [77.09,23.87,84.67,30.41]
    cord_Ind = [68.1,6.46,97.39,35.5]
    
    Max_Freq_hindi_words_file = open(MaxFreqHindiWords_filename.encode('string-escape'),'r') 
    
    
    words = [word.strip("\n").decode('utf-8') for word in  Max_Freq_hindi_words_file]
    
    
    stream = tweepy.Stream(auth, lis)
    
    while True:   
        try:
            stream.filter(track = words, languages = ["hi"])
    
        except Exception, e:
            print "Error. Restarting Stream.... Error: "
            print e.__doc__
            print e.message
        #except KeyboardInterrupt:
#            print "Stopping streamming"
#            break

if __name__ == '__main__':
    
    
    StartStreamming()
        
        
        

#    lis = MyStreamListner()
#    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
#    auth.set_access_token(access_token, access_token_secret)
#
#    #api = tweepy.API(auth)
#
#    
#
#    cord_UP = [77.09,23.87,84.67,30.41]
#    cord_Ind = [68.1,6.46,97.39,35.5]
#    
#    Max_Freq_hindi_words_file = open(MaxFreqHindiWords_filename.encode('string-escape'),'r') 
#    
#    
#    words = [word.strip("\n").decode('utf-8') for word in  Max_Freq_hindi_words_file]
#    
#    
#    while True:
#        
#        try:
#            stream = tweepy.Stream(auth, lis)
#            stream.filter(track = words, languages = ["hi"])
#        
#        except from http.client import IncompleteRead:
#            continue 
        #except KeyboardInterrupt:
#            print "Stopping streamming"
#            break
        
    
        

    #count=10

    #for twt in tweets:
    #   print twt.text
    #   print "\n\n"
    #   if count == 0:
    #       break
    #   count = count-1
