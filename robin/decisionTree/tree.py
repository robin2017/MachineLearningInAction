#!/usr/bin/python
#-*-coding:utf-8-*-
__author__ = 'robin'
from math import log
import treePlotter
import operator


#1、计算数据集data的index列的香农熵
def infoEnt(data,index):
    numEntries = len(data)
    #字典，类似java的hashmap
    labelCounts = {}
    for featVec in data:
        #取数据集的某一列
        currentLabel = featVec[index]
        if currentLabel not in labelCounts.keys(): labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1
    Ent = 0.0
    for key in labelCounts:
        prob = float(labelCounts[key])/numEntries
        #信息熵公式
        Ent -= prob * log(prob,2)
    return Ent

#2、构建data的index列的值为value的集合，去掉了index那一列
def splitDataSet(data, index, value):
    retDataSet = []
    for featVec in data:
        if featVec[index] == value:
            #将index那一列去掉
            reducedFeatVec = featVec[:index]
            reducedFeatVec.extend(featVec[index+1:])
            retDataSet.append(reducedFeatVec)
    return retDataSet

#3、计算数据集dataset中信息增益最大的那列，作为划分属性，返回的为那列的下标
def chooseBestFeatureToSplit(dataSet):
    #属性的数目,为数据集列数-1,因为最后一列不是属性,为标识
    numFeatures = len(dataSet[0]) - 1
    #计算标识的信息熵,即数据集的最后一列
    baseEntropy = infoEnt(dataSet,-1)
    bestInfoGain = 0.0; bestFeature = -1
    for i in range(numFeatures):
        featList = [example[i] for example in dataSet]
        uniqueVals = set(featList)
        newEntropy = 0.0
        for value in uniqueVals:
            subDataSet = splitDataSet(dataSet, i, value)
            prob = len(subDataSet)/float(len(dataSet))
            newEntropy += prob * infoEnt(subDataSet,-1)
        #属性i对样本集划分得到的信息增益:
        infoGain = baseEntropy - newEntropy
        if (infoGain > bestInfoGain):
            bestInfoGain = infoGain
            bestFeature = i
    return bestFeature

#4、返回数组中出现次数最多的元素，
def majorityCnt(classList):
    classCount={}
    for vote in classList:
        if vote not in classCount.keys(): classCount[vote] = 0
        classCount[vote] += 1
    sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]

#5、构建决策树（训练学习），返回为多层字典，输入为数据集和属性名称，
def createTree(dataSet,attributes):
    #取二维数据集的最后一列，即标识列
    classList = [example[-1] for example in dataSet]
    #标识列所有的元素一样，递归中止
    if classList.count(classList[0]) == len(classList):
        return classList[0]
    #遍历完所有的特征时仍然不能清晰划分，则返回出现次数最多的类别，这时候会很容易出现误判，递归中止
    if len(dataSet[0]) == 1:
        return majorityCnt(classList)
    bestFeat = chooseBestFeatureToSplit(dataSet)
    bestFeatLabel = attributes[bestFeat]
    myTree = {bestFeatLabel:{}}
    #删除属性中下标为bestFeat的属性
    del(attributes[bestFeat])
    featValues = [example[bestFeat] for example in dataSet]
    #得到数组中所有不同元素的集合
    uniqueVals = set(featValues)
    for value in uniqueVals:
        subLabels = attributes[:]       #copy all of labels, so trees don't mess up existing labels
        myTree[bestFeatLabel][value] = createTree(splitDataSet(dataSet, bestFeat, value),subLabels)
    return myTree


#6、绘制决策树
def createPlot(inTree):
    return treePlotter.createPlot(inTree)

#7、使用决策树执行分类（检测）
#输入为决策树模型，标签名称列表，测试数据点
def classify(inputTree,featLabels,testVec):
    firstStr = inputTree.keys()[0]
    secondDict = inputTree[firstStr]
    featIndex = featLabels.index(firstStr)
    key = testVec[featIndex]
    valueOfFeat = secondDict[key]
    if isinstance(valueOfFeat, dict):
        classLabel = classify(valueOfFeat, featLabels, testVec)
    else: classLabel = valueOfFeat
    return classLabel