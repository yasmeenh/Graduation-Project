# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 13:56:48 2018

@author: Hager - Lab
"""
#import sklearn.feature_extraction.text
#from nltk.tokenize import TreebankWordTokenizer
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
#from nltk import ngrams
#from string import punctuation
#import sys
#import csv
import re
#import random
#import numpy as np
#import matplotlib.pyplot as plt 
import seaborn as sns; sns.set()


class prepare:
    Body = ""
    lines=[]
    said=[]
    sentence=[]
    sentences=[]
    BetweenBraces=[]
    BetweenBracesLines=[]
    
#==============================================================================
#   setSentences Function :- Input : it takes a sentence and assigns it to the 
#   sentence of the class.
#                         - Output : Nothing
#==============================================================================       
    @classmethod   
    def __init__(cls, body, Characters, Fname):
       cls.Body = body
       cls.lines=[]
       cls.said=[]
       cls.sentence=[]
       cls.sentences=[]
       cls.BetweenBraces=[]
       cls.BetweenBracesLines=[]
#       print(body)
       fname=""
       i=0
       for f in Fname:
           if f!=' ' and i !=len(Fname)-1:
               fname+=f+' '
           else:
               fname+=f
           i+=1
#       print(fname)
       i=0
       j=0
       bracket=0
       for line in body:
#           print(line)
           if line.find(Fname)!=-1 or line.find(fname)!=-1 :
               continue
           if bracket==1 or line[0]=='[' or line[len(line)-1]==']' or line[0]=='(' or line[len(line)-1]==')':
               if bracket==0:
                   cls.BetweenBraces.append(line)
                   cls.BetweenBracesLines.append(len(cls.said))
                   j+=1
               else:
                   cls.BetweenBraces[j-1]+=' '+ line
               if line[0]=='['  or line[0]=='(' :
                   bracket=1
               if line[len(line)-1]==']'  or line[len(line)-1]==')' :
                   bracket=0
               continue
           if line.upper() == line and line[1]==' ' and line[1]==line[3] :
               continue
           words=line.split()
#           if words[0]=='BANK':
#               print(Characters)
#           print(words[0] + str(cls.RepresentsInt(words[0][0])))
           if (cls.RepresentsInt(words[0][0]) or words[0].upper() != words[0]) and len(cls.lines) != 0 :
               cls.lines[i-1]+=' '+ (cls.strip_punctuation(cls.decontracted(line)))
           else: 
               k=-1
               for c in Characters:
                   cw=c.split()
                   a=len(c)
                   if line.find(c)!=-1 and cw[0]==words[0]:
                       cls.lines.append(cls.decontracted(line[a+1:]))
                       cls.said.append(c)
        #               print(cls.lines[i])
                       i+=1
                       k=1
                       break
                   elif cw[0]==words[0] or (len(cw)>1 and cw[1]==words[0]):
                       cls.lines.append(cls.decontracted(line[len(words[0])+1:]))
                       cls.said.append(c)
        #               print(cls.lines[i])
                       i+=1
                       k=1
               if k==-1 and len(cls.lines) != 0:
                  cls.lines[i-1]+=' '+ line
                  
#               if words[0]=='BANK':
#                   print('BAAAAAAAAAAAAAAAAAAAANAAK')
#                   print(k)
#                   break
#       print(cls.lines)
       i=0
       for line in cls.lines:
            cls.sentences.append(cls.lines[i])
            cls.lines[i]=word_tokenize(cls.strip_punctuation(cls.lines[i]))
#            print(cls.lines[i])
            i+=1
       cls.lines=cls.stem(cls.lemmatizer(cls.stopWords(cls.lines)))
       i=0
       for line in  cls.lines:
           cls.sentence.append(" ".join(line))
#           print(cls.said[i]+ ' : ' + cls.sentence[i])
           i+=1
#       for line in cls.lines:
       print('cls.BetweenBracesLines')
       print(cls.BetweenBracesLines)
       return cls.said,cls.sentences,cls.sentence,cls.BetweenBraces,cls.BetweenBracesLines
#            print(line)
         
        
        
#==============================================================================
#   decontracted Function :- Input : it takes a sentence and decontract each 
#   contracted word in the sentence.
#                          - Output :
#============================================================================== 
    @classmethod
    #check string is number or not
    def RepresentsInt(cls,s):
        try: 
            int(s)
            return True
        except ValueError:
            return False   
        
        
        
#==============================================================================
#   decontracted Function :- Input : it takes a sentence and decontract each 
#   contracted word in the sentence.
#                          - Output :
#==============================================================================
    @classmethod
    def decontracted(cls,phrase):
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

    @classmethod
    def stopWords(cls,sentences):
       new_Stopwords = []
       new_sentences = []
       i = 0
       stop_words = set(stopwords.words("english"))
       
#           print(stop_words)
       for word in stop_words:
           word = cls.decontracted(word)
           new_Stopwords.append(word)
       #print(sentences)
#           print(new_Stopwords)
#           ss=sentences[7534]
#           for w in ss[1]:
#               print(w)
       ii=0;
       for sentence in sentences:
           ii+=1
           if ii%1000==0:
               print(ii)
           new_list = []
#               new_list.append(sentence[0])              
#               new_list.append(sentence[1])
           for w in sentence:
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
           sentence = new_list
           new_sentences.append(sentence)
           i = i+1
#           print("sentence..............",sentences[7534])
                   #print(sentence)
#           ss[1].remove('a')
#           for w in ss[1]:
#               print(w)
       return new_sentences
   
#                 ********************************
   
#                 ********************************

   
    @classmethod
    def stem(cls, sentences):
           new_sentences = []
           ps=PorterStemmer()
           ii=0
           for s in sentences:
               ii+=1
               if ii%1000==0:
                   print(ii)
               new_list = []
               for w in s:
                   w=ps.stem(w)
                   new_list.append(w)
#                       print(w)
               s = new_list
               new_sentences.append(s)
#               print(sentences)
           return new_sentences   


  
  
#==============================================================================
#     lemmatizer Function :- Input : 
#                          - Output : 
#==============================================================================            
   
    @classmethod
    def lemmatizer(cls , sentece1):
       lem = WordNetLemmatizer()
       ii=0
       for s in sentece1:
           ii+=1
           if ii%1000==0:
               print(ii)
           for w in s:
               lem.lemmatize(w)
               
       return sentece1


  


  
  
#==============================================================================
#     remove Punctuations Function :- Input : 
#                                   - Output : 
#==============================================================================            
   
    @classmethod
    def strip_punctuation(cls,s):
#           return ''.join(c for c in s if c not in punctuation)
       return re.sub('[^ a-zA-Z0-9]', '', s)
  