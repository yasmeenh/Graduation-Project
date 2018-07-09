# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 16:17:56 2018

@author: technology_laptop
"""
from nltk.stem import PorterStemmer
#import nltk
import pyaudio  
import wave
import contextlib 
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import numpy as np

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
   f = wave.open(r"EnvironmentModule/audio/"+s,"rb")
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

def calculate_duration(fname):
  with contextlib.closing(wave.open(fname,'r')) as f:
    frames = f.getnframes()
    rate = f.getframerate()
    duration = frames / float(rate)
    return duration

#functions to return arrays for integration
def get_audio_file_name(said,character_gender_map,voices_names_map,words,file_name,continuous,ind,MaleOrFemale,words_count):
  ps = PorterStemmer()
  environment_file_name=[]  #it is for the names of sounds files that will be displayed
  continous_or_not=[]      #if the element is 0->the sound is not continous, if it is 1->the sound is continous, if it is 2->the sound is continous with delay
  sound_ind=[] #when to be displayed
  durations=[]
  arr1=np.zeros(160)
  arr2=[]
  between_quotes=find_between(words,'"', '"')
  if between_quotes !="":
   print('between_quotes : '+between_quotes)
   print ('words.find')
   hear_index=words.find('hear')
   print (hear_index)
   if hear_index!=-1:
       quote_index=words.find('"')
       if quote_index > hear_index+4:
           environment_file_name.append(between_quotes)
           continous_or_not.append(9)
           sound_ind.append(ind)
           durations.append(1)
  #make stemming for words
  words=words.split(" ")
  ##make 3 arrays :
  w=0
  for w in words:
   stemmed_word=ps.stem(w)
   if stemmed_word in voices_names_map:
    if stemmed_word not in arr2:
        y=0
        while  y<len(voices_names_map[stemmed_word]):
          arr1[voices_names_map[stemmed_word][y]]+=1
          arr2.append(stemmed_word)
          if arr1[voices_names_map[stemmed_word][y]]==words_count[voices_names_map[stemmed_word][y]]:
              if MaleOrFemale[voices_names_map[stemmed_word][y]]==1 or MaleOrFemale[voices_names_map[stemmed_word][y]]==0:
               if ind==len(said):
                AudioFileName=file_name[character_gender_map[said[ind-1]]+voices_names_map[stemmed_word][y]]
               else:
                AudioFileName=file_name[character_gender_map[said[ind]]+voices_names_map[stemmed_word][y]] 
               environment_file_name.append(AudioFileName)
               continous_or_not.append(continuous[voices_names_map[stemmed_word][y]])
               sound_ind.append(ind)
               
               if AudioFileName!='_':
                durations.append(calculate_duration('EnvironmentModule/audio/'+AudioFileName))
               else:
                durations.append(0) 
               break
              else: 
               if voices_names_map[stemmed_word][y]==44:
                   if arr2.index('they') < arr2.index('laugh'):
                       AudioFileName=file_name[voices_names_map[stemmed_word][y]]
                   else:
                       continue
               AudioFileName=file_name[voices_names_map[stemmed_word][y]]
               if '.wav' in AudioFileName:
                   play_audio(AudioFileName)
               environment_file_name.append(AudioFileName)
               continous_or_not.append(continuous[voices_names_map[stemmed_word][y]])
               sound_ind.append(ind)
               if AudioFileName!='_':
                durations.append(calculate_duration('EnvironmentModule/audio/'+AudioFileName))
               else:
                durations.append(0)
               if stemmed_word=='laugh':
                   break
          y+=1
  

  return environment_file_name,continous_or_not,sound_ind,durations 

class EnvironmentDetect:
    
    @classmethod
    def __init__(cls,Names,Gender,Said,scene,place,BetweenBraces,BetweenBracesLines):  ##el mafrood el parameters de hya elly mb3ota mn bara??????????
        ##definitions
        voicename_row_map={}  
        audio_files=[]
        continuous_or_not=[]
        audio_index=[]
        ee=[]
        dd=[]
        ff=[]
        duration=[]
        ##create map of characters names and genders--> key-> name, value-> gender 0->female, 1->male
        l=0
        character_gender_map={}
        while l<len(Names):
            if Gender[l]=='male':
             character_gender_map[Names[l]]=1
            else:
             character_gender_map[Names[l]]=0
            l=l+1
        df = pd.read_excel('E:/GP/Graduation-Project-master (1)/Graduation-Project-master/Final/EnvironmentModule/Data/EnvironmentData.xlsx', sheetname='sheet1')
        VoiceNames = df['category']
        FileName = df['filename']
        continuous = df['continuous'] ##check if the voice is continuous or not 0 for not continuous, 1 for continuous,2 continuous with delay
        MaleOrFemale=df['m_or_f']
        words_count = df['words count']
        i=0

        while i < len(VoiceNames):   
          voicname=VoiceNames[i].split( "_" ) #this is for voicenames that contain more than one word
          j=0
          words_count1=len(voicname)
          while j < words_count1:
            if voicname[j] in voicename_row_map:
             voicename_row_map[voicname[j]].append(i)
            else: 
             ##put word counts as the first element in the value list for each key
             voicename_row_map.setdefault(voicname[j], []).append(i)  
            j+=1
          i+=1
        if scene:
          i=0
          while i<len(scene):
            scene[i].split(" ")
            ee,dd,ff,qq=get_audio_file_name(Said,character_gender_map,voicename_row_map,scene[i],FileName,continuous,0,MaleOrFemale,words_count)
            audio_files.extend(ee)
            continuous_or_not.extend(dd)
            audio_index.extend(ff)
            duration.extend(qq)
            i=i+1  
          
        if place:
          i=0
          while i<len(place):
            place[i].split(" ")
            ee,dd,ff,qq=get_audio_file_name(Said,character_gender_map,voicename_row_map,place[i],FileName,continuous,0,MaleOrFemale,words_count)
            audio_files.extend(ee)
            continuous_or_not.extend(dd)
            audio_index.extend(ff)
            duration.extend(qq)
            i=i+1
        k=0
        while k<len(BetweenBraces):
         BetweenBraces[k].split(" ")
         ee,dd,ff,qq=get_audio_file_name(Said,character_gender_map,voicename_row_map,BetweenBraces[k],FileName,continuous,BetweenBracesLines[k],MaleOrFemale,words_count) #BetweenBracesLines[k]=el index bta3 el kalm dah
         audio_files.extend(ee)
         continuous_or_not.extend(dd)
         audio_index.extend(ff)
         duration.extend(qq)
         k=k+1
        return  audio_files,continuous_or_not,audio_index,duration
