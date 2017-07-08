#!/usr/bin/python
#-*-coding:utf-8-*-
__author__ = 'robin'
import smo as smo
import robin.util.fileUitl as file
import robin.util.plotUtil as plo

def plotData():
    dataArr,labelArr=file.file2matrix('testSetCircular.txt',2)
    plo.plot2DScatterWith2Type(dataArr,labelArr,1,-1)

def calAlpha():
    dataArr,labelArr=file.file2matrix('testSet.txt',2)
    #b,alphas=smo.smoP(dataArr,labelArr,0.6,0.001,40)
    b,alphas=smo.smoP(dataArr,labelArr,200,0.0001,10000,('rbf',1.3))
    print(b)
    print(alphas[alphas>0])


def PlotDataAndSVM():
    dataArr,labelArr=file.file2matrix('testSetCircular.txt',2)
    b,alphas=smo.smoP(dataArr,labelArr,0.6,0.001,40)
    print alphas[alphas>0]
    w=smo.calcWs(alphas,dataArr,labelArr).tolist()
    svm=[0]*100
    for i in range(len(svm)):
        if(alphas[i]!=0):
            svm[i]=1

    plo.plot2DScatterWith2TypeWithSVM(dataArr,labelArr,1,-1,svm)

PlotDataAndSVM()