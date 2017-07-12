#!/usr/bin/python
#-*-coding:utf-8-*-
__author__ = 'robin'
from numpy import *
import svdRec
def test():
    data=svdRec.loadExData()
    U,Sigma,VT=linalg.svd(data)
    print "data"
    print data
    print " u "
    print U
    print " sigma "
    print Sigma
    print " vt "
    print VT


def test2():
    myMat=mat(svdRec.loadExData())
    print myMat
    print svdRec.ecludSim(myMat[:,0],myMat[:,4])
    print svdRec.cosSim(mat([[4],[2]]),mat([[1],[2]]))
    print svdRec.pearsSim(myMat[:,0],myMat[:,4])


def test3():
    myMat=mat(svdRec.loadExData())
    myMat[0,1]= myMat[0,0]= myMat[1,0]= myMat[2,0]=4
    myMat[3,3]=2
    print myMat
    print "-----"
    print svdRec.recommend(myMat,2)


def test4():
    myMat=mat(svdRec.loadExData3())
    U,Sigma,VT=linalg.svd(myMat)
    print "data"
    print myMat
    print " u "
    print U
    print " sigma "
    print Sigma
    print " vt "
    print VT

    sig2=Sigma**2
    print "九成能量"
    print 0.9*sum(sig2)
    print "2维能量"
    print sum(sig2[:2])
    print "3维能量"
    print sum(sig2[:3])
    print "4维能量"
    print sum(sig2[:4])
    print "5维能量"
    print sum(sig2[:5])
    print "6维能量"
    print sum(sig2[:6])

def test5():
    myMat=mat(svdRec.loadExData3())

    print myMat
    print "-----"
    print svdRec.recommend(myMat,2)
def test6():
    myMat=mat(svdRec.loadExData3())

    print myMat
    print "-----"
    print svdRec.recommend(myMat,2,5,svdRec.cosSim,svdRec.svdEst)


def test7():
    svdRec.imgCompress(2)



test7()
