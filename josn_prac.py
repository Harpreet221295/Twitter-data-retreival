# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 17:14:09 2017

@author: HP
"""
import re
import hindi_stemmer as hs
import string

exclude1 = set([u'।',u'-',u',',u'ॽ',u'॥',u'(',u')'])
exclude2 = set(string.punctuation)
stopwords=[]
hindi_stop_words = open(r'F:\MainDesktop\Text mining\hindi_stopwords.txt','r')
for line in hindi_stop_words:
        stopwords.append(line.decode('utf-8').strip('\n'))


def clean_tweet(tweet):
    tweet_new = re.sub("[a-zA-Z0-9]","",tweet)


    ### Removing punctuations
    tweet_new = ''.join(ch for ch in tweet_new if ch not in exclude1)
    tweet_new = ''.join(ch for ch in tweet_new if ch not in exclude2)

    ### Removing stopwords

    tweet_new = " ".join([i for i in tweet_new.split() if i not in stopwords])

    ### Stemming
    tweet_list = tweet_new.split()
    tweet_list = [hs.hi_stem(word) for word in tweet_list]

    tweet_new = " ".join(tweet_list)
    return tweet_new