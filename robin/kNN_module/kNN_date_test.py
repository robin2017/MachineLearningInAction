#!/usr/bin/python
#-*-coding:utf-8-*-
__author__ = 'robin'
from numpy import *
import kNN_date
def createDataSet():
    #样本集数据
    group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    #样本集标签
    labels = ['A','A','B','B']
    return group, labels

data,labels=createDataSet()
print kNN_date.knn([0,0],data,labels,3)