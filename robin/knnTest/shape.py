#!/usr/bin/python
#-*-coding:utf-8-*-
from numpy import *
def autoNorm(dataSet):

    minVals = dataSet.min(0)
    print minVals
    maxVals = dataSet.max(0)
    print maxVals
    ranges = maxVals - minVals
    normDataSet = zeros(shape(dataSet))
    m = dataSet.shape[0]
    print m
    normDataSet = dataSet - tile(minVals, (m,1))
    print normDataSet
    normDataSet = normDataSet/tile(ranges, (m,1))   #element wise divide
    print normDataSet
    return normDataSet, ranges, minVals

data=array([[1.,2.,3.],[4.,5.,6.],[7.,8.,9.]])
autoNorm(data)