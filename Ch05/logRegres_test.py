#!/usr/bin/python
#-*-coding:utf-8-*-
__author__ = 'robin'

import logRegres
from robin.util import plotUtil
from robin.util import fileUitl
dataSet,labels=fileUitl.file2matrix("testSet.txt",2)
plotUtil.plot2DScatterWith2Type(dataSet,labels,1,0)