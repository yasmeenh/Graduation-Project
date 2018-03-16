# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 00:26:22 2018

@author: Yasmeen Hesham
"""
#==============================================================================
#     Importing Packages
#==============================================================================

import nltk
#nltk.download()
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk import ngrams
import csv
import re
import random
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
import copy
from collections import defaultdict

#==============================================================================
#     Class : Preprocess 
#     Functions in the class: 
#     1.setSentences 
#     2.decontracted 
#     3.stopWords 
#     4.stem 
#     5.Lemmatizer
#==============================================================================

class Preprocess:

       sentence = ""

#==============================================================================
#   setSentences Function :- Input : it takes a sentence and assigns it to the 
#   sentence of the class.
#                         - Output : Nothing
#==============================================================================       
       
       def setSentence(self, sent):
           self.sentence = sent
       
    
  
          
#==============================================================================
#   decontracted Function :- Input : it takes a sentence and decontract each 
#   contracted word in the sentence.
#                          - Output :
#==============================================================================

       def decontracted(self,phrase):
           # specific
           phrase = re.sub(r"won't", "will not", phrase)
           phrase = re.sub(r"can't", "can not", phrase)
           phrase = re.sub(r"Won't", "Will not", phrase)
           phrase = re.sub(r"Can't", "Can not", phrase)
           # general
           phrase = re.sub(r"n\'t", " not", phrase)
           phrase = re.sub(r"\'re", " are", phrase)
           phrase = re.sub(r"\'s", " is", phrase)
           phrase = re.sub(r"\'d", " would", phrase)
           phrase = re.sub(r"\'ll", " will", phrase)
           phrase = re.sub(r"\'t", " not", phrase)
           
           phrase = re.sub(r"\'ve", " have", phrase)
           phrase = re.sub(r"\'m", " am", phrase)
           return phrase
      
    
  
       
#==============================================================================
#     stopWords Function :- Input : 
#                         - Output : 
#==============================================================================

       def stopWords(self,sentences):
           new_Stopwords = []
           new_sentences = []
           i = 0
           stop_words = set(stopwords.words("english"))
           
#           print(stop_words)
           for word in stop_words:
               word = self.decontracted(word)
               new_Stopwords.append(word)
           #print(sentences)
#           print(new_Stopwords)
#           ss=sentences[7534]
#           for w in ss[1]:
#               print(w)
           for sentence in sentences:
               new_list = []

               for w in sentence[1]:
#                   if  i== 7534:
#                           print("seaaaeeeeee",w)
#                           print("nooooo",sentence[1])
#                           sentence[1].remove('I')
                   #print("first" , w)
                   if w not in new_Stopwords: #.lower()
#                       print(w)
                       new_list.append(w)
#                       if  i== 7534:
#                           print("seeeeeee",w)

#               if i == 7534:
#                   print(sentence)
               sentence[1] = new_list
               new_sentences.append(sentence)
               i = i+1
#           print("sentence..............",sentences[7534])
                       #print(sentence)
#           ss[1].remove('a')
#           for w in ss[1]:
#               print(w)
           return new_sentences
       
#                 ********************************

       def stem(self, sentences):
               new_sentences = []
               ps=PorterStemmer()
               for s in sentences:
                   new_list = []
                   for w in s[1]:
                       w=ps.stem(w)
                       new_list.append(w)
#                       print(w)
                   s[1] = new_list
                   new_sentences.append(s)
#               print(sentences)
               return new_sentences   
    
    
  
  
#==============================================================================
#     lemmatizer Function :- Input : 
#                          - Output : 
#==============================================================================            
       def lemmatizer(self , senteces):
           lem = WordNetLemmatizer()
           for s in sentences:
               for w in s[1]:
                   lem.lemmatize(w)
                   
           return sentences
    
    
  
  
#==============================================================================
#     Class : extractFeatures 
#     Functions in the class: 
#     1.setN 
#     2.n_gram 
#==============================================================================

class extractFeatures:
    n = 1    # n = 1 by default
    sentences = []
    
    
#==============================================================================
#   setSentences Function :- Input : it takes a sentence and assigns it to the 
#   sentence of the class.
#                         - Output : Nothing
#==============================================================================       
       
    def setSentence(self, sent):
        
        self.sentences = sent
#        self.sentences = ['anger', ['two', 'year', 'back', 'someon', 'invit', 'tutor', 'grand-daught', '.', 'the', 'grand-daught', 'ask', 'question', 'mathemat', 'I', 'taught', '.', 'howev', 'listen', 'made', 'feel', 'unhappi', '.', 'the', 'second', 'year', '.', 'when', 'I', 'enter', 'univers', 'girl', 'parent', 'suggest', 'I', 'employ', 'daghter', 'tutor', '.', 'they', 'told', 'univers', 'homework', 'I', 'would', 'lot', 'time', 'made', 'time-t', 'requir', 'tutor', 'five', 'day', 'week', '.', 'they', 'respect', 'anyway', 'I', 'anoth', 'child', 'teach', '.']], ['sadness', ['I', 'taken', 'respons', 'someth', 'I', 'prepar', '.', 'howev', 'I', 'fail', 'timid', '.', 'after', 'three', 'attempt', 'I', 'still', 'could', 'adapt', 'atmospher', 'fail', '.', 'I', 'felt', 'imcompet', 'felt', 'other', 'would', 'think', 'I', 'prepar', '.']], ['disgust', ['I', 'home', 'I', 'heard', 'loud', 'sound', 'spit', 'outsid', 'door', '.', 'I', 'thought', 'one', 'famili', 'member', 'would', 'step', 'spit', 'bring', 'germ', 'hous', '.']], ['shame', ['I', 'homework', 'teacher', 'ask', 'us', '.', 'I', 'scold', 'immedi', '.']], ['guilt', ['I', 'shout', 'younger', 'brother', 'alway', 'afraid', 'I', 'call', 'loudli', '.']]
#        print(sent)
#        print(self.sentences)
               
    
  
 
#==============================================================================
#     setN Function :- Input : it takes the number of grams and sets it to n variable
#                    - Output : Nothing
#==============================================================================

    def setN(self , N):
        self.n=  N
    
    
  
        
#==============================================================================
#     n_grams Function :- Input: it takes a sentence
#                -  Output: it prints the ngrams
#==============================================================================

    def n_gram(self):
#        print(sentences)
        sent = copy.copy(self.sentences)
        for sentence in sent:
            sentence[1] = ngrams(sentence[1], self.n)
#            for grams in sentence[1]:
#                print (grams)
        return sent
    
    
  
    
#==============================================================================
#     Main
#     Steps: 1. Read the dataset of Emotions
#            2. Decontracted words in each sentence
#            3. Tokenize each sentence
#            4. Stem each word in sentences
#            5. Extract the ngram from the words
#==============================================================================
           

sentences = []
pre = Preprocess()
bigram = extractFeatures()
unigram = extractFeatures()

with open('W:/4th year/GP/GP Ideas/ListenPlays/Emotions/Projects/tts-master-master/ISEAR/DATA.csv') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        sentences.append(row)
#    print(sentences[2571])
    for row in sentences:
        row[1] = pre.decontracted(row[1])
        row[1] = word_tokenize(row[1])

sentences_tokenized = sentences
#print("main",sentences_tokenized[7534])       
sentences_stopWords = pre.stopWords(sentences_tokenized)
#print(sentences_stopWords[7534]) 
sentence_lemmatize = pre.lemmatizer(sentences_stopWords)
#print(sentence_lemmatize)
sentence_stemmed = pre.stem(sentence_lemmatize)
#print(sentence_stemmed)
copy_stemmed = copy.deepcopy(sentence_stemmed)
#Try bigram as a feature
bigram.setN(2)
bigram.setSentence(copy_stemmed)
#print(sentence_stemmed)
bigrams = bigram.n_gram()
#print("seeeeeeeeeeeeen",sentence_stemmed)

#for sentence in bigrams:
#    print(sentence[0])
#    for grams in sentence[1]:
#        print (grams)
#print(sentence_stemmed)

##Try unigram as a feature       
unigram.setN(1)
unigram.setSentence(sentence_stemmed)
unigrams = unigram.n_gram()
#for sentence in unigrams:
#    print(sentence[0])
#    for grams in sentence[1]:
#        print (grams)        
Document = []
d = defaultdict(list)
for sentence in unigrams:
    d[sentence[0]].append(list(sentence[1]))
        
print(d)
r = [(v, k) for k, v in d.items()]
random.shuffle(r)
print(r)
wordy = []
for li in r:
    for lis in li[0]:
         for x in lis:
             wordy.append(x[0])
            
print(wordy)