#!/usr/bin/python
#-*-coding:utf-8-*-
__author__ = 'robin'

from numpy import array
import numpy as np
import matplotlib.pyplot as plt
#绘制二维散点图，其中标识为两种
def plot2DScatterWith2Type(dataXY,labels,type1,type2):
    fig=plt.figure()
    ax=fig.add_subplot(111)
    idx_1=np.where(array(labels)==type1)
    p1=ax.scatter(dataXY[idx_1,0],dataXY[idx_1,1],marker='*',color='b',label=''+str(type1),s=20)
    idx_2=np.where(array(labels)==type2)
    p2=ax.scatter(dataXY[idx_2,0],dataXY[idx_2,1],marker='o',color='b',label=''+str(type2),s=20)
    plt.legend(loc='upper right')
    plt.show()


def plot2DScatterWith2TypeWithSVM(dataXY,labels,type1,type2,svm):
    fig=plt.figure()
    ax=fig.add_subplot(111)

    tmp1=[False]*100
    for i in range(len(tmp1)):
        tmp1[i]=(array(labels)==type1)[i]and(array(svm)==0)[i]
    idx_1=np.where(tmp1)
    p1=ax.scatter(dataXY[idx_1,0],dataXY[idx_1,1],marker='*',color='b',label=''+str(type1),s=20)

    tmp3=[False]*100
    for i in range(len(tmp3)):
        tmp3[i]=(array(labels)==type1)[i]and(array(svm)==1)[i]
    idx_3=np.where(tmp3)
    p3=ax.scatter(dataXY[idx_3,0],dataXY[idx_3,1],marker='*',color='r',label=''+str(type1),s=20)

    tmp2=[False]*100
    for i in range(len(tmp2)):
        tmp2[i]=(array(labels)==type2)[i]and(array(svm)==0)[i]
    idx_2=np.where(tmp2)
    p2=ax.scatter(dataXY[idx_2,0],dataXY[idx_2,1],marker='o',color='b',label=''+str(type2),s=20)

    tmp4=[False]*100
    for i in range(len(tmp4)):
        tmp4[i]=(array(labels)==type2)[i]and(array(svm)==1)[i]
    idx_4=np.where(tmp4)
    p4=ax.scatter(dataXY[idx_4,0],dataXY[idx_4,1],marker='o',color='r',label=''+str(type2),s=20)

    plt.legend(loc='upper right')
    plt.show()

def plot2DScatterWith2TypeWithSVMWithSP(dataXY,labels,type1,type2,svm,X,Y):
    fig=plt.figure()
    ax=fig.add_subplot(111)

    tmp1=[False]*100
    for i in range(len(tmp1)):
        tmp1[i]=(array(labels)==type1)[i]and(array(svm)==0)[i]
    idx_1=np.where(tmp1)
    p1=ax.scatter(dataXY[idx_1,0],dataXY[idx_1,1],marker='*',color='b',label=''+str(type1),s=20)

    tmp3=[False]*100
    for i in range(len(tmp3)):
        tmp3[i]=(array(labels)==type1)[i]and(array(svm)==1)[i]
    idx_3=np.where(tmp3)
    p3=ax.scatter(dataXY[idx_3,0],dataXY[idx_3,1],marker='*',color='r',label=''+str(type1),s=20)

    tmp2=[False]*100
    for i in range(len(tmp2)):
        tmp2[i]=(array(labels)==type2)[i]and(array(svm)==0)[i]
    idx_2=np.where(tmp2)
    p2=ax.scatter(dataXY[idx_2,0],dataXY[idx_2,1],marker='o',color='b',label=''+str(type2),s=20)

    tmp4=[False]*100
    for i in range(len(tmp4)):
        tmp4[i]=(array(labels)==type2)[i]and(array(svm)==1)[i]
    idx_4=np.where(tmp4)
    p4=ax.scatter(dataXY[idx_4,0],dataXY[idx_4,1],marker='o',color='r',label=''+str(type2),s=20)

    plt.legend(loc='upper right')
    plt.plot(X,Y,'r')
    plt.show()


def plot2DScatterWith3Type(dataXY,labels,type1,type2,type3):
    fig=plt.figure()
    ax=fig.add_subplot(111)
    idx_1=np.where(array(labels)==type1)
    p1=ax.scatter(dataXY[idx_1,0],dataXY[idx_1,1],marker='*',color='r',label=''+str(type1),s=20)
    idx_2=np.where(array(labels)==type2)
    p2=ax.scatter(dataXY[idx_2,0],dataXY[idx_2,1],marker='o',color='b',label=''+str(type2),s=20)
    idx_3=np.where(array(labels)==type3)
    p3=ax.scatter(dataXY[idx_3,0],dataXY[idx_3,1],marker='+',color='g',label=''+str(type3),s=20)
    plt.legend(loc='upper right')
    plt.show()