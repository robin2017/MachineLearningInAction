#!/usr/bin/python
#-*-coding:utf-8-*-
__author__ = 'robin'
from numpy import *  #导入模块一：numpy
import operator      #导入模块二：操作模块



#四个参数分别为：待测数据点，样本集数据，样本集标签，k
def knn(point, data, labels, k):

    #得到样本集中样本数量,即矩阵的行数
    dataSize = data.shape[0]
    diffMat = tile(point, (dataSize,1)) - data
    sqDiffMat = diffMat**2
    sqDistances = sqDiffMat.sum(axis=1)
    #欧式距离
    distances = sqDistances**0.5
    sortedDistIndicies = distances.argsort()
    classCount={}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1
    sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]