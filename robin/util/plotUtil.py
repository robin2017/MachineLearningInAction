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
    p1=ax.scatter(dataXY[idx_1,0],dataXY[idx_1,1],marker='*',color='r',label=''+str(type1),s=20)
    idx_2=np.where(array(labels)==type2)
    p2=ax.scatter(dataXY[idx_2,0],dataXY[idx_2,1],marker='o',color='b',label=''+str(type2),s=20)
    plt.legend(loc='upper right')
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