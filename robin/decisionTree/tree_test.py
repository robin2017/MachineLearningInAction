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

def test_infoEnt():
    data,labels=createDataSet()
    print tree.infoEnt(data,-1)

def test_splitDataSet():
    data,labels=createDataSet()
    print tree.splitDataSet(data,0,1)

def test_chooseBestFeatureToSplit():
    data,labels=createDataSet()
    print tree.chooseBestFeatureToSplit(data)

def test_majorityCnt():
    a=[1,2,3,4,6,4,5,7,6,3,4]
    print tree.majorityCnt(a)

def test_createTree():
    data,attributes=createDataSet()
    print tree.createTree(data,attributes)

def test_plot():
    data,attributes=createDataSet()
    tree.createPlot(tree.createTree(data,attributes))

def test_contactLenses():
    fr=open('lenses.txt')
    lenses=[inst.strip().split('\t') for inst in fr.readlines()]
    #四个属性名称
    lensesAtts=['age','prescript','astigmatic','tearRate']
    lensesTree=tree.createTree(lenses,lensesAtts)
    print lensesTree
    tree.createPlot(lensesTree)

test_contactLenses()