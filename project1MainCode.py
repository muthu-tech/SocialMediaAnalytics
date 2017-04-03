# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 00:30:29 2017

@author: muthu
"""
#fix_encoding = lambda s: s.decode('utf8', 'ignore')
'''from textblob import TextBlob
c
from pprint import pprint
with open('C:\Users\muthu\Desktop\DataScience\Project1\corpusTweet.txt') as file:
    corpusData = json.load(file)
print(corpusData)
tweets_file = open('C:\Users\muthu\Desktop\DataScience\Project1\corpusTweet.txt', 'r')
#for line in tweets_file:
tweetCorpus = json.loads(tweets_file)
print(tweetCorpus)
import json   
tweets_data_path = 'C:\Users\muthu\Desktop\DataScience\Project1\check.txt'

tweets_data = []
tweets_file = open(tweets_data_path, "r")
for line in tweets_file:
    try:
        tweet = json.loads(line)
        tweets_data.append(tweet)
    except:
        continue
    
print(len(tweets_data))'''
from pprint import pprint
from textblob import TextBlob
tweets_data_path = 'C:\Users\muthu\Desktop\DataScience\Project1\Tweets.txt'
tweets_file = open(tweets_data_path, "r")
import json

# Read each tweet and add it to the list
tweets=[]
for eachLine in tweets_file:
    if eachLine=='\n':
        continue
    tweets.append(json.loads(eachLine))
tweets_file.close()
#print(len(tweets))
'''for t in tweets:
    #print('tweet = ',t)
    try:
        print(t['text'])
    except KeyError:
        pass'''
    #print('------------')
import re
pol_list=[]
subj_list=[]
tweetTexts = []
for eachTweet in tweets:
    try:
        #text = re.sub(r':.*$', "", eachTweet['text'].encode('utf-8'))
        tweetTexts.append(eachTweet['text'])
        stringUnderTest = TextBlob(eachTweet['text'])
        pol_list.append(stringUnderTest.sentiment.polarity)
        subj_list.append(stringUnderTest.sentiment.subjectivity)
    except:
        pass
print()
'''import matplotlib.pyplot as plt
#Subjectivity Histogram
#print(len(tweetTexts))

aggregatePolarity = sum(i for i in pol_list)
pol_Average = aggregatePolarity/len(pol_list)


aggregateSubjectivity = sum(i for i in subj_list)
subjectivity_Average = aggregateSubjectivity/len(subj_list)   
plt.hist(subj_list, bins=20) #, normed=1, alpha=0.75)
plt.xlabel('subjectivity score')
plt.ylabel('Tweet count')
plt.grid(True)
plt.axvline(subjectivity_Average, color='b', linestyle='dashed', linewidth=2)
plt.savefig('subjectivityHistogram10kTweets.pdf')
plt.show()
plt.hist(pol_list, bins=20) #, normed=1, alpha=0.75)
plt.xlabel('Polarity score')
plt.ylabel('Tweet count')
plt.grid(True)
plt.axvline(pol_Average, color='b', linestyle='dashed', linewidth=2)
plt.savefig('polarityHistogram10kTweets.pdf')
plt.show()'''
 

import nltk
''' Stemming for collected tweets   http://stackoverflow.com/questions/10554052/what-are-the-major-differences-and-benefits-of-porter-and-lancaster-stemming-alg '''
from nltk.stem.snowball import SnowballStemmer
ss = SnowballStemmer('english')
stemmedWordlist=[]
defaultStopwords = nltk.corpus.stopwords.words("english")
'''for eachTweet in tweetTexts:
    #print(ss.stem(eachTweet))
    try:
       stemmedWordlist.append(ss.stem(eachTweet))
    except KeyError:
        pass'''

#for eachTweet in tweetTexts:
#    for eachWord in eachTweet:
#        stemmedWord += ss.stem(eachWord)
#        stemmedWordlist.append(stemmedWord)
#print(stemmedWordlist)
#print(stemmedWordlist)
from nltk.tokenize import word_tokenize
desiredStopWords = defaultStopwords+['http://','rt','@','RT','rt','.com']  #we need to add numbers to this ignore-list to get better results
wordCloudInput = []
tempList = []
#print(desiredStopWords)
#theBigListOfWords =tempList.append(' '.join(eachTweet[0] for eachTweet in tweetTexts))
#for eachWord in theBigListOfWords:
#    if eachWord not in desiredStopWords:
#        wordCloudInput.append(eachWord)
#print(wordCloudInput[0])
'''import sys  
sys.setdefaultencoding('utf8')
reload(sys) '''
newList =[]
for eachTweet in tweetTexts:
    newList.append(eachTweet.strip())
    print(newList,'\n')
#==============================================================================
#     tweettokens=word_tokenize(eachTweet.decode('utf-8'))
#     for eachWord in tweettokens:
#         stemmedWord = ss.stem(eachWord)
#         stemmedWordlist.append(stemmedWord)
#==============================================================================
#==============================================================================
# for word in stemmedWordlist:
#     if word not in desiredStopWords:
#         wordCloudInput.append(word)
#==============================================================================
#print(wordCloudInput[0:4])
#print(stemmedWordlist)'''
    
     


