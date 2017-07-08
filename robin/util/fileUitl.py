#!/usr/bin/python
#-*-coding:utf-8-*-
from numpy import zeros

__author__ = 'robin'
#返回的是数据集和标记空间，其中attrnum为属性的数目，标记空间即为文件的最后一列，整个文件有（attrnum+1）列
def file2matrix(filename,attrNum):
    fr = open(filename)
    numberOfLines = len(fr.readlines())         #get the number of lines in the file
    dataSet = zeros((numberOfLines,attrNum))        #prepare matrix to return
    labelSpace = []                       #prepare labels return
    fr = open(filename)
    index = 0
    for line in fr.readlines():
        line = line.strip()
        listFromLine = line.split('\t')
        dataSet[index,:] = listFromLine[0:attrNum]
        labelSpace.append(float(listFromLine[-1]))
        index += 1
    return dataSet,labelSpace