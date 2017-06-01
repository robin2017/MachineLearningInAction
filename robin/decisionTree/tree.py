#!/usr/bin/python
#-*-coding:utf-8-*-
__author__ = 'robin'
from math import log
import operator

def shannonEnt(data,index):
    numEntries = len(data)
    #字典，类似java的hashmap
    labelCounts = {}
    for featVec in data:
        #取数据集的某一列
        currentLabel = featVec[index]
        if currentLabel not in labelCounts.keys(): labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1
    shannonEnt = 0.0
    for key in labelCounts:
        prob = float(labelCounts[key])/numEntries
        #信息熵公式
        shannonEnt -= prob * log(prob,2)
    return shannonEnt