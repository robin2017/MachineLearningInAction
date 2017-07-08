#!/usr/bin/python
#-*-coding:utf-8-*-
from numpy import shape

__author__ = 'robin'

from robin.util import fileUitl
from robin.util import plotUtil
import svmMLiA
def test_plot():
    dataSet,labelSpace=fileUitl.file2matrix('testSet.txt',2)
    plotUtil.plot2DScatterWith2Type(dataSet,labelSpace,1.,-1.)

def test_1():
    dataArr,labelArr=svmMLiA.loadDataSet('testSet.txt')
    print labelArr


def test_2():
    dataArr,labelArr=svmMLiA.loadDataSet('testSet.txt')
    b,alphas=svmMLiA.smoSimple(dataArr,labelArr,0.6,0.001,40)
    print "b"
    print b
    print "alphas"
    print alphas
    print ">0"
    print alphas[alphas>0]

def test_3():
    dataArr,labelArr=svmMLiA.loadDataSet('testSet.txt')
    b,alphas=svmMLiA.smoSimple(dataArr,labelArr,0.6,0.001,40)
    print shape(alphas[alphas>0])
    for i in range(100):
        if alphas[i]>0.0:print dataArr[i],labelArr[i]

def test_4():
    dataArr,labelArr=svmMLiA.loadDataSet('testSet.txt')
    b,alphas=svmMLiA.smoP(dataArr,labelArr,0.6,0.001,40)
    print shape(alphas[alphas>0])
    for i in range(100):
        if alphas[i]>0.0:print dataArr[i],labelArr[i]

def test_smo_simple():
    dataArr,labelArr=svmMLiA.loadDataSet('testSet.txt')
    b,alphas=svmMLiA.smoSimple(dataArr,labelArr,0.6,0.001,40)
    print(b)
    print(alphas[alphas>0])

def test_smo_all():
    dataArr,labelArr=svmMLiA.loadDataSet('testSet.txt')
    b,alphas=svmMLiA.smoP(dataArr,labelArr,0.6,0.001,40)
    print(b)
    print(alphas[alphas>0])

test_smo_all()