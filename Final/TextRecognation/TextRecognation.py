# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 13:31:18 2018

@author: Hager - Lab
"""
import os
import PyPDF2
class TextRecognation(object):
    Data=""#save reading data in all file
    lines=[]
    Fname=""#save file name
    Body=[]#save body part
    Characters=[]#save Characters par
    Time=[]#save time part
    Place=[]#save lace part
    Caution=[]#save caution
    Scene=[]#save scenes
    Note=[]#save notes
    Reqs=[]
    props=[]
    name=[]#save file name spliiting
    s=0
    
    
    @classmethod
    #check string is number or not
    def RepresentsInt(cls,s):
        try: 
            int(s)
            return True
        except ValueError:
            return False
        
        
    @classmethod
    def init(cls,s):
        cls.Data=""
        cls.Fname=s[0]
        cls.Body=[]
        cls.Characters=[]
        cls.Time=[]
        cls.Place=[]
        cls.Caution=[]
        cls.Scene=[]
        cls.Note=[]
        cls.Reqs=[]
        cls.props=[]
        cls.lines=s
        cls.name=s[0].split()#split for _ to get words from file name
        cls.s=0
        cls.extraction()#split file to play's strucures
        return cls.Fname,cls.Body,cls.Characters,cls.Time,cls.Place,cls.Caution,cls.Scene,cls.Note,cls.Reqs,cls.props
        
        
        
#    @classmethod
#    def getname(cls,s):
#         cls.Fname=os.path.splitext(s)[0] #get filename 
#         pa=cls.Fname.split('/') # split on / to remove path
#         pa.reverse() # make reverse to ignore abig pathes
#         cls.name=pa[0].split('_')#split for _ to get words from file namr
#         u=len(cls.name)
#         i=0
#         cls.Fname = cls.name[i].upper() #save name in upper
#         for i in range(0,u):
#             if cls.RepresentsInt(cls.name[i]) == False and  cls.s == -1:#ignore numbers
#                 cls.s=i #save index of first english word
#             cls.name[i]=cls.name[i].upper()
#             if i!=0: #to ignore first we wrote it in line 64
#                cls.Fname= cls.Fname + " " + cls.name[i].upper() #save name in upper
                
                
    @classmethod
    def extraction(cls):
        i=0
#        print(a)
        t = "-1"
        g=""
#        print(cls.lines)
        for line in cls.lines:
            word=line.split()
            if(i==0):
                i=i+1
                continue;
#            if(i==30):
#                break
#            print(word)
            i=i+1
#            print(word)
#            print(g)
#            print(cls.name[cls.s] in word)
#            print(cls.name[cls.s])
#            print(cls.s)
            if word[0] == "CHARACTERS" or word[0] == "CHARACTERS:" or  word[0] == 'Characters:': 
                t="ch"
            elif word[0] =="PLACE:" or word[0] =="PLACE":
                t="p"
            elif word[0] =="SETTING:" or word[0] =="SETTING" or  word[0] == 'Setting:' or word[0] =="SETTINGS" :
                t="p"
            elif word[0] =="TIME:" or word[0] =="TIME" or  word[0] == 'Time:' or  word[0] == 'Time':
                t="t"
            elif word[0] =="TIME/PLACE:" or word[0] =="TIME/PLACE":
                t="tp"
            elif word[0] =="Scene:" or word[0] =="Scene":
                cls.Scene.append(line)
                t="bd"
            elif word[0] =="SCENE:" or word[0] =="SCENE":
                cls.Scene.append(line)
                t="bd"
            elif word[0] =="NOTE:" or word[0] =="NOTE":
                t="no"
            elif word[0] =="Note:" or word[0] =="Note":
                t="no"
            elif word[0] =="PROPS:" or word[0] =="PROPS":
                t="pr"
            elif word[0] =="SET" and (word[1] =="REQUIREMENTS" or word[1] =="REQUIREMENTS:"):
                t="sr"
            elif word[0] =="CAUTION:" or word[0] =="CAUTION":
                t="ca"
            elif word[0] =="Copyright:" or word[0] =="Copyright":
                cls.Caution.append(line)
                t="cop"
                g="cop"
            elif g=="cop" and len(word)> cls.s and cls.Fname == word:
                t="bd"
                g=""
                cls.Body.append(cls.Fname.upper())
                continue
            elif g=="cop" and (word[0].isupper() or word[0][0]=='['):
                cls.Body.append(cls.Fname.upper())               
                t="bd"
                g=""
            if t == "ch" :
                cls.Characters.append(line)
            elif t== "ca" :
                cls.Caution.append(line)
            elif t== "sr" :
                cls.Reqs.append(line)
            elif t== "pr" :
                cls.props.append(line)
            elif t== "no" :
                cls.Note.append(line)
            elif t== "sc" :
                cls.Scene.append(line)
            elif t== "t" :
                cls.Time.append(line)
            elif t== "p" :
                cls.Place.append(line)
            elif t== "tp" :
                cls.Time.append(line)
                cls.Place.append(line)
            elif t== "bd" :
                cls.Body.append(line)
#            print(t)
        
#Fname,Body,Characters,Time,Place,Caution,Scene,Note,Reqs,props=TextRecognation.init("Kinds/10000_cigarettes.txt")
