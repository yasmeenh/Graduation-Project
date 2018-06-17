# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 14:40:44 2018

@author: technology_laptop
"""
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
import TextToSound
import difflib
import pyaudio  
import wave 
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
#define stream chunk   
chunk = 1024
##function to find the words between 2 words
def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""
##definitions
ps = PorterStemmer()
VoiceName = []
VoiceFile = [] 
voicename_row_map={}       
word1_rows=[]
word2_rows=[]
intersection=[] ##intersection between word1_rows and word2_rows 
words=[] ##it is an array for words that may be environment     

##Reading the meta_data file
df = pd.read_excel('E:/GP/environment module/environment with map/data_with_added_row_number4.xlsx', sheetname='data_with_added_row_number3')
print('ghjkl2')
VoiceNames = df['category']
FileName = df['filename']
print('ghjkl3')
#making the map
##loop to make the map
i=0
while i < len(VoiceNames):   
    voicname=VoiceNames[i].split( "_" ) #this is for voicenames that contain more than one word
    #print('ghjkl4')
    j=0
    while j < len(voicname):
      if voicname[j] in voicename_row_map:
        #el mafrod a-add 3la list 3la tool
        
        voicename_row_map[voicname[j]].append(i)
        #print('ghjkl5')
      else: 
        #print('ghjkl')
        
        #el mafrod hena a-create l list
        voicename_row_map.setdefault(voicname[j], []).append(i)
        #print('ghjkl6')
      j=j+1
    i = i + 1
#print(voicename_row_map)
##get body,scene and place to extract the environment from them
body=TextToSound.Body 
scene=TextToSound.Scene
place=TextToSound.Place
w=0  ##index for the coming loop
if scene:
  words.extend(scene.split(" "))
elif place:
  words.extend(place.split(" "))
else:
    
  i=0
  for string in body:
      if i==1:
          break
      if "[" in string or "]" in string:
       print('string')
       print('\n')
       print(string)
       print('\n')
       BetweenBraces=find_between( string, "[", "]" ).split(" ")
       #if not BetweenBraces:
       words.extend(BetweenBraces)
      else:
          continue
    
##run the audio file
value1=False
door_word=False
print("worddddddds")
print(words)

while w<len(words):   
 if words[w]=='door':
   door_word=True 
 stemmed_word=ps.stem(words[w])
 if stemmed_word in voicename_row_map:
  print('ghjkl11')
  print(words[w])
  #ygib el index elly hwa feeh we yro7 ysha8l l soot
  #open a wav format music
  
  if not value1:
      word1_rows=voicename_row_map[stemmed_word]
      value1=True
      print('word1_rows')
      print(word1_rows)
  else:
      word2_rows=voicename_row_map[stemmed_word]
      print('word2_rows')
      print(word2_rows)
 
 if word2_rows:
  intersection=list(set(word1_rows).intersection(word2_rows))
  print(intersection) 
  print('ghjkl12')
  if intersection:
   value1=False
   word1_rows=[]
   word2_rows=[]
   AudioFileName=FileName[intersection[0]]
   print(intersection[0])
   #AudioFileName=FileName[D2[s1[w]][0]]
   print(AudioFileName)
   f = wave.open(r"E:/GP/environment module/ESC-50-master/ESC-50-master/audio/"+AudioFileName,"rb") 
   
  #instantiate PyAudio 
   #print('ghjkl13')
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
 w=w+1
if not intersection:
   print('ghjkl144')
   print('word1_rows[0]')
   print(word1_rows[0])
   AudioFileName=FileName[word1_rows[0]]
   #AudioFileName=FileName[D2[s1[w]][0]]
   print(AudioFileName)
   f = wave.open(r"E:/GP/environment module/ESC-50-master/ESC-50-master/audio/"+AudioFileName,"rb") 
   
  #instantiate PyAudio 
   #print('ghjkl13')
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
           
     