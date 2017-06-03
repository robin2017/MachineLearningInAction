#!/usr/bin/python
#-*-coding:utf-8-*-
__author__ = 'robin'

import trees
mydat,labels=trees.createDataSet()
# print mydat
#
# print labels
#
# print trees.calcShannonEnt(mydat)
#
# print trees.chooseBestFeatureToSplit(mydat)

print trees.createTree(mydat,labels)