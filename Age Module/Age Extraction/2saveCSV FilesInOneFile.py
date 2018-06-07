# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 13:13:26 2018

@author: Hager
"""
import csv
sentences=[]
classes=[]
posts=[]
reader=""
reader2=""
rows=[]
with open('preprocessedData.csv') as csvfile:
    reader = csv.reader(csvfile)
    i=0
    for row in reader:
        if(i % 100==0):
                print('r1',i)
#        if i==20:
#            break
        if(i!=0):
            rows.append(row)
        i+=1
with open('preprocessedData2.csv') as csvfile:
    reader2 = csv.reader(csvfile)   
    i=0
    for row in reader2:
        if(i % 100==0):
            print('r2',i)
#        if i==20:
#            break
        if(i!=0):
            rows.append(row)
        i+=1
i=0
for row in rows:
#        row2=row.split(',')
    if(i % 100==0):
        print('split',i)
    posts.append(row[1])
    classes.append(row[0])
    i=i+1
with open('preprocessedData3.csv', 'w', newline='') as csvfile:
    fieldnames = ['AgeClass', 'post']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    j=0
    writer.writeheader()
    for line in posts:
        writer.writerow({'AgeClass': classes[j], 'post': line})
        j+=1
print("sentence full==============================================")
