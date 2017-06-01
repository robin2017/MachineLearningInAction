#!/usr/bin/python
#-*-coding:utf-8-*-
from numpy import *
arr=random.rand(4,4)
print "数组如下："
print arr

mat= mat(random.rand(4,4))
print "矩阵如下："
print mat

print "矩阵求逆如下："
invmat=mat.I
print invmat

print "矩阵*逆矩阵==："
print mat*invmat

print "误差矩阵："
print mat*invmat-eye(4)