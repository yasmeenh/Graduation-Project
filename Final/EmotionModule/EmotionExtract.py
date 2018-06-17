# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 11:41:27 2018

@author: Hager - Lab
"""


import pickle

class EmotionDetect(object):
    sentence=[]
    Emotion=[]
    loaded_model=''
    @classmethod
    def init(cls,sentence):
        cls.Sentence=sentence
        filename = 'EmotionModule\Data\Emotion_Model.sav'
        cls.loaded_model = pickle.load(open(filename, 'rb'))
        cls.Emotion=cls.loaded_model.predict(cls.Sentence)   
        return cls.Emotion
    

        
#file=open("characters.txt", "r") 
#s=file.read() 
#GenderDetect.init(s)
