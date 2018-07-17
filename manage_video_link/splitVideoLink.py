#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 06:04:26 2018

@author: lea
"""
txtFilename = '/home/lea/Stage/DATA/list[4573].txt'
csvFilename="/home/lea/Stage/DATA/media_link_file.csv"

def addToCSV(content):
    file = open(csvFilename,"w")
    file.write('media-link\n')
    file.write(str(content))
    
def extractTxt(filename):
    fileContent = ""
    file = open(filename, "r")
    for line in file : 
        fileContent = fileContent + line
    return fileContent


fileContent = extractTxt(txtFilename) 
fileContent.replace('mp4', 'mp4\n')
addToCSV(fileContent)

