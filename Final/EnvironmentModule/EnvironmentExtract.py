# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 16:17:56 2018

@author: technology_laptop
"""
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
import difflib
import pyaudio  
import wave 
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
from prepareLearning import prepare
from TextRecognation.TextRecognation import TextRecognation

##function to find the words between 2 words
def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""
##function to read the audio file
def play_audio(s):
   chunk = 1024
   f = wave.open(r"E:/GP/Graduation-Project-master (1)/Graduation-Project-master/Final/EnvironmentModule/audio/"+s,"rb") 
  #instantiate PyAudio 
   p = pyaudio.PyAudio()
  #open stream 
   stream = p.open(format = p.get_format_from_width(f.getsampwidth()),  
                channels = f.getnchannels(),  
                rate = f.getframerate(),  
                output = True)  
  #read data 
   data = f.readframes(chunk)  

  #play stream 
   while data:  
     stream.write(data)  
     data = f.readframes(chunk)  

  #stop stream 
   stream.stop_stream()  
   stream.close()  

  #close PyAudio 
   p.terminate()    

#functions to return arrays for integration
def get_audio_file_name(voices_names_map,words,file_name,continuous,index):
  ps = PorterStemmer()
  ##make 3 arrays :
  environment_file_name=[]  #it is for the names of sounds files that will be displayed
  continous_or_not=[]      #if the element is 0->the sound is not continous, if it is 1->the sound is continous, if it is 2->the sound is continous with delay
  sound_index=[] #when to be displayed 
  word1_rows=[]
  word2_rows=[]
  intersection=[]
  w=0
  value1=False
  door_word=False
  door_word1=False
  for w in words.split(" "):
   stemmed_word=ps.stem(w)
   if stemmed_word=='door':
     door_word=True 
   
   if stemmed_word in voices_names_map:
    
    if not value1:   ##check there is no environment words before
        if door_word:
            door_word1=True   #door word is the first one
        ##hena lw el kelma l word count bta3ha be 1 yb2a ysh8lha 3la tool lo msh keda yb2a ha5znha
        if voices_names_map[stemmed_word][0]==-1:
            #play the audio
           #print('mennnnnnnnnna')
           AudioFileName=file_name[voices_names_map[stemmed_word][1]]
           #play_audio(AudioFileName)
           environment_file_name.append(AudioFileName)
           continous_or_not.append(continuous[voices_names_map[stemmed_word][1]])
           if index==-1:
             sound_index.append(index)
           if index!=-1:
              sound_index.append(index)
        else:
          word1=stemmed_word  
          word1_rows=voices_names_map[stemmed_word]
          value1=True
    else: 
        if voices_names_map[stemmed_word][0]==-1:
            #play the audio
           #print('mennnnnnnnnna')
           AudioFileName=file_name[voices_names_map[stemmed_word][1]]
           #play_audio(AudioFileName)
           environment_file_name.append(AudioFileName)
           continous_or_not.append(continuous[voices_names_map[stemmed_word][1]])
           if index==-1:
             sound_index.append(index)
           if index!=-1:
              sound_index.append(index)
        else: 
           ##it is the second word
           ##check that word2!=word1
           if stemmed_word!=word1:
            word2_rows=voices_names_map[stemmed_word]
   if word2_rows:
    intersection=list(set(word1_rows).intersection(word2_rows))
    if intersection:
     if not door_word:   
      value1=False
      word1_rows=[]
     else:
      if not door_word1: #this means that word "door" comes second
        word1_rows=[]
        word1_rows=word2_rows
        
     word2_rows=[]
     if len(intersection)>1:
      h=0
      while h<len(intersection):
       if intersection[h]==-2:
         h=h+1
         continue
       else:
        intersection_index=intersection[h]
        AudioFileName=file_name[intersection_index] ##to not get the word_counts as intersection
        
        environment_file_name.append(AudioFileName)
        continous_or_not.append(continuous[intersection_index])
        if index==-1:
             sound_index.append(index)
        if index!=-1:
           sound_index.append(index)
           
        break
      #AudioFileName=FileName[D2[s1[w]][0]]
      #print(AudioFileName)
      #play_audio(AudioFileName)
     else:             #new addedddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
      value1=False    #delete word1_rows array and word2_rows array as they don't come after each other-- special cases --> sea waves,door
      word1_rows=[]
      word2_rows=[]
   #w=w+1
  if not intersection:
     #print('ghjkl144')
     value1=False    #delete word1_rows array and word2_rows array as they don't come after each other-- special cases --> sea waves,door
     word1_rows=[]
     word2_rows=[]
  return environment_file_name,continous_or_not,sound_index 



class EnvironmentDetect:
    
    @classmethod
    def __init__(cls,scene,place,BetweenBraces,BetweenBracesLines):  ##el mafrood el parameters de hya elly mb3ota mn bara??????????
        #define stream chunk   
        chunk = 1024
        ##definitions
        voicename_row_map={}
        environment_map={}      
        word1_rows=[]
        word2_rows=[]
        intersection=[] ##intersection between word1_rows and word2_rows 
        words=[] ##it is an array for words that may be environment  
        ps = PorterStemmer()
        audio_files=[]
        continuous_or_not=[]
        audio_index=[]
        ee=[]
        dd=[]
        ff=[]
         ##Reading the meta_data file 
        df = pd.read_excel('E:/GP/Graduation-Project-master (1)/Graduation-Project-master/Final/EnvironmentModule/Data/EnvironmentData.xlsx', sheetname='sheet1')
        #print('ghjkl2')
        VoiceNames = df['category']
        words_count = df['words count'] ##8alabn msh ha7tgha
        FileName = df['filename']
        continuous = df['continuous'] ##check if the voice is continuous or not 0 for not continuous, 1 for continuous
        #print('ghjkl3')
        #making the map
        ##loop to make the map
        i=0
        while i < len(VoiceNames):   
            voicname=VoiceNames[i].split( "_" ) #this is for voicenames that contain more than one word
            #print('ghjkl4')
            j=0
            words_count1=len(voicname)
            while j < words_count1:
              stemmed_voicname=ps.stem(voicname[j])
              if stemmed_voicname in voicename_row_map:
               #el mafrod a-add 3la list 3la tool
               voicename_row_map[stemmed_voicname].append(i)
               #print('ghjkl5')
              else: 
               #print('ghjkl')
               #el mafrod hena a-create l list 
               ##put word counts as the first element in the value list for each key
               voicename_row_map.setdefault(stemmed_voicname, []).append(-words_count1)
               voicename_row_map[stemmed_voicname].append(i)
               #print('ghjkl6')
              j=j+1
            i = i + 1
    
        if scene:
          scene=scene.split(" ") ##we amshy 3lihm
          ee,dd,ff=get_audio_file_name(voicename_row_map,scene,FileName,continuous,-1)
          audio_files.extend(ee)
          continuous_or_not.extend(dd)
          audio_index.extend(ff)
          
        if place:
          i=0
          while i<len(place):
            place[i].split(" ")
            #place=place.split(" ")
            ee,dd,ff=get_audio_file_name(voicename_row_map,place[i],FileName,continuous,-1)
            audio_files.extend(ee)
            continuous_or_not.extend(dd)
            audio_index.extend(ff)
            
            i=i+1
        k=0
        while k<len(BetweenBraces):
         BetweenBraces[k]=prepare.strip_punctuation(BetweenBraces[k])  
         BetweenBraces[k].split(" ")
         ee,dd,ff=get_audio_file_name(voicename_row_map,BetweenBraces[k],FileName,continuous,BetweenBracesLines[k]) #BetweenBracesLines[k]=el index bta3 el kalm dah
         audio_files.extend(ee)
         continuous_or_not.extend(dd)
         audio_index.extend(ff)
         k=k+1
        return  audio_files,continuous_or_not,audio_index
    
