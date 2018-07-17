#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 06:22:25 2018

@author: lea
"""

path = '/home/lea/Stage/DATA/tests/Batch_3294999_batch_results.csv'

file = open(path,'r')
file_r = file.read()
lines = file_r.split('\n')
len_lines = len(lines)
print (lines[0])
tab = []

for col in lines:
    tab.append(col.split(','))
    
    
print (tab[2][34])
col = "WorkerId,WorkTimeInSeconds,Input.media-link,Answer.act1Action,Answer.act1Look,Answer.act1Point,Answer.act1Touch,Answer.act2Action,Answer.act2Look,Answer.act2Point,Answer.act2Touch"
col_list = []
print("len de tab[0]" + str(len(tab[0])))
for i in range (0,len(tab[0])-1,1):
    val = tab[0][i]
    if val in col:
        col_list.append(i)
print (col_list)
data = []
dic = {}
for i in range(1, len_lines-1):
    for j in col_list:
        #print ("i = " + str(i))
        #print ("j = " + str(j))
        name = tab[0][j]
        dic[name] = tab[i][j]
        print (tab[i][j])
        data.append(dic)
        
        
print(data[0])
