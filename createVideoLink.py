#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 02:35:05 2018

@author: lea
"""
import os
folderPath = "/scratch2/lthamie/DATA/extracts_09_12_cha_0o"
filename = "links.csv"

file = open(filename, "w")
for filename in os.listdir(folderPath):
    videoPath = folderPath+'/'+filename
    if filename.endswith('.mp4'):
        name = filename.split('/')
        name = name[-1]
        file.write("http://129.199.81.135/babyvid/" + name+"\n")