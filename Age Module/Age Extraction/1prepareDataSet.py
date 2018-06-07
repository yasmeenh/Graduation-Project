# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 13:47:00 2018

@author: Hager
"""

#==============================================================================
#     Importing Packages
#==============================================================================
import nltk
#nltk.download('all-nltk')
#nltk.download()
import sklearn.feature_extraction.text
from nltk.tokenize import TreebankWordTokenizer
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk import ngrams
import sys
import csv
import re
import random
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns; sns.set()
import copy
from collections import defaultdict
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.linear_model import SGDClassifier
from nltk.stem.snowball import SnowballStemmer
from sklearn.model_selection import train_test_split
from sklearn import datasets, linear_model
from sklearn.model_selection import cross_validate
from sklearn.metrics.scorer import make_scorer
from sklearn.metrics import confusion_matrix
from sklearn.svm import LinearSVC
from sklearn.metrics import recall_score
from sklearn.svm import SVC
class LemmaTokenizer(object):
    def init(self):
        self.wnl = WordNetLemmatizer()
    def call(self, articles):
        return [self.wnl.lemmatize(t) for t in word_tokenize(articles)]


class StemmedCountVectorizer(CountVectorizer):
    def build_analyzer(self):
        wnl = WordNetLemmatizer()
        analyzer = super(StemmedCountVectorizer, self).build_analyzer()
        return lambda doc: ([stemmer.stem(wnl.lemmatize(w)) for w in analyzer(doc)])

#==============================================================================

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

       def stem(self, sentences):
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
       def lemmatizer(self , sentece1):
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
        print(self.sentences)
               
    
  
 
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
        
        sent = copy.copy(self.sentences)
        
#        print(self.n)
        newSent=[]
#        print(self.sentences)
        for senten in sent: 
##            sentence =  "this is my friend".split()
#            newSent.append(ngrams(sentence, self.n))
##            for grams in sentence2:
##                print (grams)
            
#            print(sentence)
            a=[]
            a.append(senten)
#            print(sentence)
            vect = sklearn.feature_extraction.text.CountVectorizer(  \
                                                        ngram_range=(self.n,self.n),tokenizer=TreebankWordTokenizer().tokenize)
#            print (senten.split())
            vect.fit(a)
            print('{1}-grams: {0}'.format(vect.get_feature_names(), self.n))
        return newSent
    
    
  
    
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
decrement = True
maxInt = sys.maxsize
while decrement:
    # decrease the maxInt value by factor 10 
    # as long as the OverflowError occurs.

    decrement = False
#    try:
    csv.field_size_limit(1727770)
#    except OverflowError:
#        maxInt = int(maxInt/10)
#        decrement = True
with open('Data Set\Agewthtpun.csv') as csvfile:
    reader = csv.reader(csvfile)
    I=0
    for row in reader:
        if(I >= 400000):
#            break
            sentences.append(row)
        if(I % 1000==0):
            print('r',I) 
        
#        print (row)
        I=I+1
#    print(I)
    print('Readfile====================================================================')
reader=""
I=0
classes=[]
posts=[]
for row in sentences:
    if(I % 100==0):
        print(I)
    if(I!=0):
        row[2] = pre.decontracted(row[2])        
        posts.append( word_tokenize(row[2]))
#            posts.append(row[2])
        if int(row[1]) <= 15:
           classes.append('1')
        elif int(row[1]) <= 45:
            classes.append('2')
        else:
            classes.append('3')
    I=I+1
##    print(I)
print('token====================================================================')
sentences=[]
sentences_tokenized = posts    
posts=[] 

sentences_stopWords = pre.stopWords(sentences_tokenized)
sentences_tokenized=[]
print('stopwords====================================================================')

sentence_lemmatize = pre.lemmatizer(sentences_stopWords)
sentences_stopwords=[]
print('lemmatize====================================================================')

sentence_stemmed = pre.stem(sentence_lemmatize)
sentences_lemmatize=[]
print('stem====================================================================')
text=[]
#f2=open('labels.txt','w')
#with open('preprocessedData.txt','w') as f:
#    j=0
#    for line in sentence_stemmed:
#    #    print(line)
#    #    print("*********************************")
#    #    t=""
#        i=0;
#        t=" ".join(line)
#    #    for word in line:
#    #        if i==0:
#    #            t=word
#    #            i+=1
#    #            continue
#    #        t+=" " + word;
#    ##    print (t)
#    ##    print("&&&&&&&&&&&&&&&&&&&&&&&")
#        text.append(t)
#        f.write(t+'\n')
#        f2.write(classes[j]+'\n')
#        j=j+1
#f2.close()
with open('preprocessedData2.csv', 'w', newline='') as csvfile:
    fieldnames = ['AgeClass', 'post']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    j=-1
    for line in sentence_stemmed:
        t=""
        i=0;
        t=" ".join(line)
        text.append(t)
        j=j+1
        writer.writerow({'AgeClass': classes[j], 'post': t})
print("sentence full==============================================")
    
    
#posts, test, classes, testclass = train_test_split(text,
#                                                          classes,
#                                                          test_size=0.33,
#                                                          random_state=42,stratify=classes)
#
#
##print(posts)
#count_vect = CountVectorizer()
#X_train_counts = count_vect.fit_transform(posts)
##print(X_train_counts)
#tfidf_transformer = TfidfTransformer()
#X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
##print(X_train_tfidf)
#
### Initialize our classifier Naive Base and make model
##clf = MultinomialNB().fit(X_train_tfidf,classes)
##
##text_clf = Pipeline([('vect', CountVectorizer()),
##                      ('tfidf', TfidfTransformer()),
##                      ('clf', MultinomialNB()) ])
##text_clf = text_clf.fit(posts, classes)
### Make predictions
##predicted = text_clf.predict(test)
###preds = gnb.predict(test)
##print(np.mean(predicted == testclass))
#
#print("first============================================")
#
## Training Support Vector Machines - SVM and calculating its performance
#scoring = ['precision', 'recall','f1','accuracy']
#clf = SVC(kernel='linear', C=1, random_state=0)
#c=[0.001,0.003,0.1,0.2,0.8,1,3,4,10,20,30,50]
#for reg in c:
#    SVC.C=reg
#    scores = cross_validate(clf,X_train_tfidf , classes, scoring=scoring,cv=5, return_train_score=False,verbose=10)
#    print (scores['f1'])
#    print (scores['precision']) 
#    print (scores['recall']) 
#    print (scores['accuracy']) 
##text_clf_svm = Pipeline([('vect', CountVectorizer()), ('tfidf', TfidfTransformer()),
##                         ('clf-svm', SGDClassifier(loss='hinge', penalty='l2',alpha=1e-3, n_iter=5, random_state=42))])
##print(len(posts))
##print(len(classes))
##text_clf_svm = text_clf_svm.fit(posts, classes)
##predicted_svm = text_clf_svm.predict(test)
##print(np.mean(predicted_svm == testclass))
##
##
##print("second============================================")
#
##s=LemmaTokenizer.init()
#
##posts=s._call_(posts)
##print(posts)
##
##stemmer = SnowballStemmer("english", ignore_stopwords=True,)
##stemmed_count_vect = StemmedCountVectorizer(stop_words='english')
##cl = Pipeline([('vect', CountVectorizer(ngram_range=(1, 2), min_df=2)), ('tfidf', TfidfTransformer()), 
##                             ('mnb', MultinomialNB(fit_prior=False))])
##
##cl = cl.fit(posts, classes)
##
##predicted_mnb_stemmed = cl.predict(test)
##
##print(np.mean(predicted_mnb_stemmed == testclass))
##
##print("third============================================")
#
#
##text_clf_svm2 = Pipeline([('vect', CountVectorizer(ngram_range=(1, 2), min_df=2)), ('tfidf', TfidfTransformer()),
##                         ('clf-svm', SGDClassifier(loss='hinge', penalty='l2',alpha=1e-3, n_iter=5, random_state=42))])
##print(len(posts))
##print(len(classes))
##text_clf_svm2 = text_clf_svm2.fit(posts, classes)
##predicted_svm2 = text_clf_svm2.predict(test)
##print(np.mean(predicted_svm2 == testclass))
##
##
##print("fourth============================================")
#
##c1=0
##c2=0
##c3=0
##v=0
##for i in testclass:
##    if i=='1':
##        c1+=1
##    elif i=='2':
##        c2+=1
##    else:
##        c3+=1
##print(c1)
##print(c2)
##print(c3)


















#copy_stemmed = copy.deepcopy(sentence_stemmed)

##Try bigram as a feature
#bigram.setN(2)
##bigram.setSentence(copy_stemmed)
##print(posts);
#bigram.setSentence(posts)
##print(sentence_stemmed)
#bigrams = bigram.n_gram()
#
#print('====================================================================')
#
####Try unigram as a feature       
##unigram.setN(1)
##unigram.setSentence(sentence_stemmed)
##unigrams = unigram.n_gram()
##for sentence in unigrams:
##    for grams in sentence:
##        print (grams)  
#        
#print('====================================================================')
#
##Document = []
##d = defaultdict(list)
##for sentence in unigrams:
##    d[sentence[0]].append(list(sentence[1]))
##        
##print(d)
##r = [(v, k) for k, v in d.items()]
##random.shuffle(r)
##print(r)
##wordy = []
##for li in r:
##    for lis in li[0]:
##         for x in lis:
##             wordy.append(x[0])
##            
##print(wordy)