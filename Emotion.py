# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 00:26:22 2018

@author: Yasmeen Hesham
"""

import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from nltk import ngrams
import csv
import re

#==============================================================================
#     Class : Emotion 
#     Functions in the class: 
#     1.setSentences :- Input : it takes a sentence and assigns it to the sentence of the class
#                       Output : Nothing
#     2.decontracted :- Input : it takes a sentence and decontract each contracted word in the sentence
#     3.stopWords :- Input : 
#                    Output : 
#==============================================================================

class Preprocess:

       sentence = ""

       def setSentence(self, sent):
           self.sentence = sent
           
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
       
       def stopWords(self,sentences):
           stop_words = set(stopwords.words("english"))
           filteredSentence = []
           print(sentences)
           for sentence in sentences:
               for w in sentence:
                   if w not in stop_words:
                       filteredSentence.extend(w)
               sentence = filteredSentence
           return sentence
               
    
    
        
#==============================================================================
#     Class : Stemming 
#     Functions in the class: 
#     1.stem :- Input : it takes a list of tokenized sentences
#               Output : it returns the sentence of the stemmed words
#==============================================================================        

class Stemming:
    
    def stem(self, sentences):
        
        ps=PorterStemmer()
        for s in sentences:
            for w in s:
                w=ps.stem(w)
                #print(w)
        return sentences



#==============================================================================
#     Class : ngram 
#     Functions in the class: 
#     1.setN :- Input : it takes the number of grams and sets it to n variable
#               Output : Nothing
#     2.n_grams :- Input: it takes a sentence
#                  Output: it prints the ngrams
#==============================================================================

class ngram:
    n = 1    # n = 1 by default
    
    def setN(self , N):
        self.n=  N
        
    def n_gram(self,sentences):
        print(sentences)
        for sentence in sentences:
            Ngrams = ngrams(sentence, self.n)
            for grams in Ngrams:
                print (grams)
        return Ngrams
    
    
    
#==============================================================================
#     Main
#     Steps: 1. Read the dataset of Emotions
#            2. Decontracted words in each sentence
#            3. Tokenize each sentence
#            4. Stem each word in sentences
#            5. Extract the ngram from the words
#==============================================================================
           
sentences_tokenized = []
pre = Preprocess()
stem = Stemming()
ng = ngram()

with open('W:/4th year/GP/GP Ideas/ListenPlays/Emotions/Projects/tts-master-master/ISEAR/DATA.csv') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        pre.setSentence(row[1])
        row[1] = pre.decontracted(row[1])
        sentences_tokenized.append(word_tokenize(row[1]))


sentences_tokenized = pre.stopWords(sentences_tokenized)
stemmedSentence = stem.stem(sentences_tokenized)
ng.setN(2)
ng.n_gram(stemmedSentence)