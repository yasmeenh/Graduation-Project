# -*- coding: utf-8 -*-
"""
Created on Sun Apr  8 02:20:41 2018

@author: Hager - Lab
"""
from prepareLearning import prepare
from GenderModule.genderExtract import GenderDetect
from AgeModule.AgeExtract import AgeDetect
from EmotionModule.EmotionExtract import EmotionDetect
from TextRecognation.TextRecognation import TextRecognation
s="TextRecognation/Kinds/Lighting rod man.txt"
if s.lower().endswith('.txt'):#check this file is text document
    file=open(s, "r")#open text file
    Data=file.read() #read play

    file.close()#close file
    s=Data.splitlines();
#    print(s)
    Fname,Body,Characters,Time,Place,Caution,Scene,Note,Reqs,props=TextRecognation.init(s)
    Names=[]
    Gender=[]
    Age=[]
    Said=[]
    Sentence=[]
    Names,Gender,Age=GenderDetect.init(Characters)
    Said,Sentence,SemiSentence=prepare.__init__(Body,Names,Fname)
    Age=AgeDetect.__init__(Names,Age, Said,SemiSentence)
    Emotion=EmotionDetect.init(SemiSentence)
    i=0
    print(Emotion)
#    emotions 1--> angry   2-->fear   3-->Happy   4-->neutral   5-->sad
    for line in  SemiSentence:
        print(str(Emotion[i]) + ' : ' + SemiSentence[i])
        i+=1   
    print()
    print()
    print(Names)   
    print()
    print()         
    print(Gender)      
    print()
    print()         
    print(Age)
    
    
    
#    print(Body)
#    print()
#    print()
#    print(Caution)   
#    print()
#    print()         
#    print(Characters)
#    print()
#    print()
#    print(Time)
#    print()
#    print()
#    print(Place)   
#    print()
#    print()         
#    print(Scene)
#    print()
#    print()
#    print(Note)
#    print()
#    print()
#    print(Reqs)   
#    print()
#    print()         
#    print(props)
#    print()
#    print()
else: #any other Documents
    print( "you must insert txt file")#error