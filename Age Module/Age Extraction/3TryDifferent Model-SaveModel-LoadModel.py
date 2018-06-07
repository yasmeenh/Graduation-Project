# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 17:00:22 2018

@author: Hager - Lab
"""

#==============================================================================
#     Importing Packages
#==============================================================================

import pickle
import sklearn.feature_extraction.text
#from nltk.tokenize import TreebankWordTokenizer
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






posts = []
classes=[]
rows=[]
decrement = True
maxInt = sys.maxsize
decrement = False
#    try:
csv.field_size_limit(1727770)
with open('preprocessedData3.csv') as csvfile:
    reader2 = csv.reader(csvfile)   
    i=0
    for row in reader2:
        if(i % 100==0):
            print('r',i)
#        if i==100000:
#            break
        if(i!=0):
            rows.append(row)
        i+=1
i=0
c1=0
c2=0
c3=0
for row in rows:
    if c1==8670 and c2==8670 and c3==8670:
        break
#        row2=row.split(',')
    if(i % 100==0):
        print('split',i)
#    posts.append(row[1])
    if row[0]=='1'and c1<8670:
        classes.append(1)
        posts.append(row[1])
        c1+=1
    elif row[0]=='2'and c2<8670:
        classes.append(2)
        posts.append(row[1])
        c2+=1
    elif c3<8670: 
        classes.append(3)
        posts.append(row[1])
        c3+=1
    i=i+1
print('read posts====================================================================')

print('read classes ====================================================================')
posts, test, classes, testclass = train_test_split(posts,
                                                          classes,
                                                          test_size=0.33,
                                                          random_state=42,stratify=classes)

print("c1 =",c1)
print("c2 =",c2)
print("c3 =",c3)
#print(posts)
#########################################################################
#######################Trial Part #######################################
#########################################################################
count_vect = CountVectorizer(ngram_range=(1, 4), min_df=2)
X_train_counts = count_vect.fit_transform(posts)
#print(X_train_counts)
tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
# Training Support Vector Machines - SVM and calculating its performance
scoring = ['precision_micro', 'recall_micro','f1_micro','accuracy']
clf = SVC(kernel='linear', C=1, random_state=0)
#c=[0.001,0.003,0.1,0.2,0.8,1,3,4,10,20,30,50]
c=[0.001,0.2,3,10,50]
for reg in c:
    SVC.C=reg
    print(reg)
    scores = cross_validate(clf,X_train_tfidf , classes, scoring=scoring,cv=5, return_train_score=False,verbose=10)
    print(scores)
    print("-----------------------------------------------------------------------")

#########################################################################
#######################End Trial Part ###################################
#########################################################################
    
    

#########################################################################
#######################Save Model Part ##################################
#########################################################################

print("Start to save Model in file")
text_clf_svm2 = Pipeline([('vect',CountVectorizer(ngram_range=(1, 4), min_df=2)), ('tfidf', TfidfTransformer()),
                         ('clf-svm', SVC(kernel='linear', C=1, random_state=0))])
print(len(posts))
print(len(classes))
model = text_clf_svm2.fit(posts, classes)
predicted_svm2 = model.predict(test)
print("predict from certain model")
print(np.mean(predicted_svm2 == testclass))


filename = 'finalized_model.sav'
pickle.dump(model, open(filename, 'wb'))
 
# some time later...
 #########################################################################
#######################End Save Model Part ###############################
##########################################################################
 
 
 
 
 #########################################################################
#######################Read Model Part ###################################
##########################################################################
# load the model from disk
loaded_model = pickle.load(open(filename, 'rb'))
result = loaded_model.score(test, testclass)
print("predict from Loaded model")
print(result)