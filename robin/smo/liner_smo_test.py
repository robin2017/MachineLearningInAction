#!/usr/bin/python
#-*-coding:utf-8-*-
__author__ = 'robin'
import smo as smo

import robin.util.fileUitl as file
import robin.util.plotUtil as plo

def plotData():
    dataArr,labelArr=file.file2matrix('testSet.txt',2)
    plo.plot2DScatterWith2Type(dataArr,labelArr,1,-1)

def calAlpha():
    dataArr,labelArr=file.file2matrix('testSet.txt',2)
    b,alphas=smo.smoP(dataArr,labelArr,0.6,0.001,40)
    w=smo.calcWs(alphas,dataArr,labelArr)

    print(b)
    print(alphas[alphas>0])



def plotDataAndSVM():
    dataArr,labelArr=file.file2matrix('testSet.txt',2)
    b,alphas=smo.smoP(dataArr,labelArr,0.6,0.001,40)
    print alphas[alphas>0]
    w=smo.calcWs(alphas,dataArr,labelArr).tolist()
    svm=[0]*100
    for i in range(len(svm)):
        if(alphas[i]!=0):
            svm[i]=1

    bb=b.tolist()[0][0]
    w0=w[0][0]
    w1=w[1][0]
    X=[2,8]
    y0=(-bb-w0*X[0])/w1
    y1=(-bb-w0*X[1])/w1
    Y=[y0,y1]

    plo.plot2DScatterWith2TypeWithSVMWithSP(dataArr,labelArr,1,-1,svm,X,Y)

plotDataAndSVM()