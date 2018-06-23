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
from EnvironmentModule.EnvironmentExtract import EnvironmentDetect
#s="TextRecognation/Kinds/blue_christmas.txt"
s="TextRecognation/Kinds/family_2_0.txt"
#s="TextRecognation/Kinds/while_the_auto_waits.txt"
#s="TextRecognation/Kinds/traces_of_memory.txt"
#s="TextRecognation/Kinds/the_death_of_the_hired_man.txt"
#s="TextRecognation/Kinds/10,000 CIGARETTES.txt"
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
    BetweenBraces=[]      ##it is used for environment
    BetweenBracesLines=[] ##it is an index for environment (when it appears to dispaly the sound) 
    audio_files=[]
    continuous_or_not=[]
    audio_index=[]
    Names,Gender,Age=GenderDetect.init(Characters)
    Said,Sentence,SemiSentence,BetweenBraces,BetweenBracesLines=prepare.__init__(Body,Names,Fname)
    
    print('BetweenBraces')
    print(BetweenBraces)
    print('BetweenBracesLines')
    print(BetweenBracesLines)
    i=0
    for line in  BetweenBracesLines:
        print(str(BetweenBracesLines[i]) + ' : ' + BetweenBraces[i])
        i+=1   
    Age=AgeDetect.__init__(Names,Age, Said,SemiSentence)
    Emotion=EmotionDetect.init(SemiSentence)
    #Characters File
    path = 'E:/GP/Graduation-Project-master (1)/Graduation-Project-master/Final/Characters.txt'
    Characters = open(path,'w')
    k=0
    while k<len(Names):
      Characters.write(Names[k]+'\n'+str(Age[k])+'\n'+Gender[k]+'\n')
      k+=1
    Characters.close()
    #Sentences File
    path = 'E:/GP/Graduation-Project-master (1)/Graduation-Project-master/Final/Sentences.txt'
    Sentences = open(path,'w')
    l=0
    while l<len(Said): 
      Sentences.write(Said[l]+'\n'+str(Emotion[i])+'\n'+Sentence[l]+'\n')
      l+=1
    Sentences.close()
    
    audio_files,continuous_or_not,audio_index=EnvironmentDetect.__init__(Scene,Place,BetweenBraces,BetweenBracesLines)
    #Environment File
    path = 'E:/GP/Graduation-Project-master (1)/Graduation-Project-master/Final/Environment.txt'
    Environment = open(path,'w')
    m=0
    while m<len(audio_files):
      Environment.write(audio_files[m]+'\n'+str(continuous_or_not[m])+'\n'+str(audio_index[m])+'\n') 
      m+=1
    Environment.close()
    '''
    print(audio_files)
    print(continuous_or_not)
    print(audio_index)
    '''
    
    
    
    '''
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
    '''