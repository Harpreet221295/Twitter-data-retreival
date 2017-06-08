# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 13:01:22 2017

@author: HP
"""

from gensim import corpora


processed_tweet_file_name = "F:\MainDesktop\Text mining\GetFreWords_text.txt"
output_filename = "F:\MainDesktop\Text mining\Most_Freq_Hindi_words_on_Twitter.txt"

tweet_file = open(processed_tweet_file_name.encode('string-escape'), 'r')
output_file = open(output_filename.encode('string-escape'),'w')

tweet_dictionary = corpora.Dictionary(line.split() for line in tweet_file)
#tweet_dictionary.save(r'F:\MainDesktop\Text mining\MostFreqHindiWordsTwitter_dictionary.dict')  # store the dictionary, for future reference

            
#print len(new_dict)
    
most_frequent_ids = (v for v in tweet_dictionary.token2id.itervalues())
most_frequent_ids = sorted(most_frequent_ids, key=tweet_dictionary.dfs.get, reverse=True)
most_frequent_ids = most_frequent_ids[:400]

for id in most_frequent_ids:
    word = tweet_dictionary[id] + "\n"
    output_file.write(word.encode('utf-8'))

tweet_file.close()
output_file.close()
#for id in most_frequent_ids:
#    print tweet_dictionary[id]
#
#tweet_file.seek(0)
#
#
#tweet_corpus = [tweet_dictionary.doc2bow(tweet.split()) for tweet in tweet_file]
#corpora.MmCorpus.serialize(r'F:\MainDesktop\Text mining\tweet_corpus.mm', tweet_corpus) 


#print tweet_corpus
    
