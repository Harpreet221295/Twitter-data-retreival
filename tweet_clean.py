# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 17:14:09 2017

@author: HP
"""
import re
import hindi_stemmer as hs
import string
from collections import defaultdict

exclude1 = set([u'।',u'-',u',',u'ॽ',u'॥',u'(',u')',u'.',u'…'])
exclude2 = set(string.punctuation)
stopwords=[]
hindi_stop_words = open(r'F:\MainDesktop\Text mining\hindi_stopwords.txt','r')
for line in hindi_stop_words:
        stopwords.append(line.decode('utf-8').strip('\n'))
        
stopwords = set(stopwords)

emoji_pattern = re.compile(
    u"(\ud83d[\ude00-\ude4f])|"  # emoticons
    u"(\ud83c[\udf00-\uffff])|"  # symbols & pictographs (1 of 2)
    u"(\ud83d[\u0000-\uddff])|"  # symbols & pictographs (2 of 2)
    u"(\ud83d[\ude80-\udeff])|"  # transport & map symbols
    u"(\ud83c[\udde0-\uddff])"  # flags (iOS)
    "+", flags=re.UNICODE)


def clean_tweet(tweet):
    
    tweet_new = Remove_AlphaNumeric(tweet)
   
    tweet_new = Remove_Emoji(tweet_new)
    
    tweet_new = Remove_Punctuation(tweet_new)

    tweet_new = Remove_stopwords(tweet_new)
    
    tweet_new = Remove_stem(tweet_new)
 
    return tweet_new


def Remove_AlphaNumeric(tweet):
    tweet_new = re.sub("[a-zA-Z0-9@]","",tweet)
    tweet_new = re.sub("[\nEOF]"," ",tweet_new)
    
    return tweet_new

def Remove_Emoji(tweet):
    tweet_new = emoji_pattern.sub(r'', tweet) # no emoj
    return tweet_new

def Remove_Punctuation(tweet):
     ### Removing punctuations
    tweet_new = ''.join(ch for ch in tweet if ch not in exclude1)
    tweet_new = ''.join(ch for ch in tweet_new if ch not in exclude2)
    return tweet_new
    
def Remove_stopwords(tweet):
    tweet_new = " ".join([i for i in tweet.split() if i not in stopwords])
    return tweet_new

def Remove_stem(tweet):
    tweet_list = tweet.split()
    tweet_list = [hs.hi_stem(word) for word in tweet_list]
    tweet_new = " ".join(tweet_list)
    return tweet_new    

def clean_tweet_by_frequency(tweet_file_name, processed_tweets_file_name):
    
    frequency = defaultdict(int)
    tweet_file = open(tweet_file_name,'r')
    new_tweet_file = open(processed_tweets_file_name,'w')
    
    for tweet in tweet_file:
        for token in tweet.split():
            frequency[token] += 1
    
    tweet_file.seek(0)
    
    
    for tweet in tweet_file:
        text = [token for token in tweet.split() if frequency[token]>1]
        if text is not None:
            new_tweet_file.write(" ".join(text)+"\n")
        
        
    tweet_file.close()
    new_tweet_file.close()    


#for ch in str:
#    print ch