# -*- coding: utf-8 -*-
"""
Created on Sun Apr  8 02:20:41 2018

@author: Hager - Lab
"""
from GenderModule.genderExtract import GenderDetect
from TextRecognation.TextRecognation import TextRecognation
s="TextRecognation/Kinds/10,000 CIGARETTES.txt"
if s.lower().endswith('.txt'):#check this file is text document
    file=open(s, "r")#open text file
    Data=file.read() #read play

    file.close()#close file
    s=Data.splitlines();
#    print(s)
    Fname,Body,Characters,Time,Place,Caution,Scene,Note,Reqs,props=TextRecognation.init(s)
    Names=[]
    Gender=[]
    Names,Gender=GenderDetect.init(Characters)
    print(Characters)
    print()
    print()
    print(Names)   
    print()
    print()         
    print(Gender)
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