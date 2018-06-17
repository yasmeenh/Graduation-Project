# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 11:41:27 2018

@author: Hager - Lab
"""


import pickle

class AgeDetect(object):
    Lines=[]
    Names=[]
    sentence=[]
    Said=[]
    Model=[]
    loaded_model=''
    @classmethod
    def __init__(cls,names,age,said,sentence):
        cls.Names=names
        cls.Age=age
        cls.Said=said
        cls.Sentence=sentence
        filename = 'AgeModule\Data\Age_Model.sav'
        cls.loaded_model = pickle.load(open(filename, 'rb'))
        for i in range (len(cls.Age)):
            if cls.Age[i]!=0:
                continue
            c=0
            cls.Model=[]
            for j in range(len(said)):
                if(said[j]==names[i]) and c!=10:
                    cls.Model.append(sentence[j])
                    c+=1
                if c==9:
                    break
            cls.Age[i]=cls.getAge()
            
        return cls.Age
    

    
                #####################################################
                ################## Check Age ########################
                #####################################################
    @classmethod
    #check string is number or not
    def getAge(cls):
#        print('****************************************************************')
#        print(cls.Model)
        if len(cls.Model)==0:
            return 2
        result=cls.loaded_model.predict(cls.Model)
        c1=0
        c2=0
        c3=0
#        print(result)
        for j in range(len(result)):
            if result[j]==1:
                c1+=1
            elif result[j]==2:
                c2+=1
            else:
                c3+=1
#        print('****************************************************************')
#        print()
#        print()
        if c2>=c1 and c2>=c3:
            return 2
        elif c1>=c2 and c1>c3:
            return 1
        return 3
        
        
#file=open("characters.txt", "r") 
#s=file.read() 
#GenderDetect.init(s)
