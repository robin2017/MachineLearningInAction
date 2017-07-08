#!/usr/bin/python
#-*-coding:utf-8-*-
from numpy import array, shape, arange

__author__ = 'robin'

import logRegres
from robin.util import plotUtil
from robin.util import fileUitl


def test_get():
    dataSet,labels=logRegres.loadDataSet()

    print dataSet
    print labels
    #plotUtil.plot2DScatterWith2Type(dataSet,labels,1,0)

    print logRegres.gradAscent(dataSet,labels)



def test_plotBestFit():
    dataSet,labels=logRegres.loadDataSet()
    weights=logRegres.gradAscent(dataSet,labels)
    logRegres.plotBestFit(weights.getA())

logRegres.colicTest()
