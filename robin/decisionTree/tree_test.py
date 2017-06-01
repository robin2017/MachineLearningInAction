#!/usr/bin/python
#-*-coding:utf-8-*-
__author__ = 'robin'
import tree
def createDataSet():
    dataSet = [[1, 1, 'yes'],
               [1, 1, 'yes'],
               [1, 0, 'no'],
               [0, 1, 'no'],
               [0, 1, 'no']]
    labels = ['no surfacing','flippers']
    #change to discrete values
    return dataSet, labels
data,labels=createDataSet()
print tree.shannonEnt(data,-1)