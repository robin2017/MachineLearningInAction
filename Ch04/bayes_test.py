#!/usr/bin/python
#-*-coding:utf-8-*-
import random
from numpy import array

__author__ = 'robin'

import bayes
def test_vocList():
    listOposts,listClasses=bayes.loadDataSet()
    myVocabList=bayes.createVocabList(listOposts)
    print myVocabList

def test_word2vec():
    listOposts,listClasses=bayes.loadDataSet()
    myVocabList=bayes.createVocabList(listOposts)
    print bayes.setOfWords2Vec(myVocabList,listOposts[0])

def test_train():
    listOposts,listClasses=bayes.loadDataSet()
    myVocabList=bayes.createVocabList(listOposts)
    trainMat=[]
    for postinDoc in listOposts:
        trainMat.append(bayes.setOfWords2Vec(myVocabList,postinDoc))
    p0v,p1v,pab=bayes.trainNB0(trainMat,listClasses)

    print p1v
def testingNB():
    listOPosts,listClasses = bayes.loadDataSet()
    myVocabList = bayes.createVocabList(listOPosts)
    trainMat=[]
    for postinDoc in listOPosts:
        trainMat.append(bayes.setOfWords2Vec(myVocabList, postinDoc))
    p0V,p1V,pAb = bayes.trainNB0(array(trainMat),array(listClasses))
    testEntry = ['love', 'my', 'dalmation']
    thisDoc = array(bayes.setOfWords2Vec(myVocabList, testEntry))
    print testEntry,'classified as: ',bayes.classifyNB(thisDoc,p0V,p1V,pAb)
    testEntry = ['stupid', 'garbage']
    thisDoc = array(bayes.setOfWords2Vec(myVocabList, testEntry))
    print testEntry,'classified as: ',bayes.classifyNB(thisDoc,p0V,p1V,pAb)


def spamTest():
    docList=[]; classList = []; fullText =[]
    for i in range(1,26):
        str=open('email/spam/%d.txt' % i).read()
        print "str"
        print str
        wordList = bayes.textParse(str)
        print "wordlist"
        print wordList
        docList.append(wordList)
        fullText.extend(wordList)
        classList.append(1)
        wordList = bayes.textParse(open('email/ham/%d.txt' % i).read())
        docList.append(wordList)
        fullText.extend(wordList)
        classList.append(0)
    print "doclist"
    print len(docList)
    print docList
    print "fulllist"
    print len(fullText)
    print fullText
    print classList

    vocabList = bayes.createVocabList(docList)#create vocabulary
    trainingSet = range(50); testSet=[]           #create test set
    for i in range(10):
        randIndex = int(random.uniform(0,len(trainingSet)))
        testSet.append(trainingSet[randIndex])
        del(trainingSet[randIndex])
    trainMat=[]; trainClasses = []
    for docIndex in trainingSet:#train the classifier (get probs) trainNB0
        trainMat.append(bayes.bagOfWords2VecMN(vocabList, docList[docIndex]))
        trainClasses.append(classList[docIndex])
    p0V,p1V,pSpam = bayes.trainNB0(array(trainMat),array(trainClasses))
    errorCount = 0
    for docIndex in testSet:        #classify the remaining items
        wordVector = bayes.bagOfWords2VecMN(vocabList, docList[docIndex])
        if bayes.classifyNB(array(wordVector),p0V,p1V,pSpam) != classList[docIndex]:
            errorCount += 1
            print "classification error",docList[docIndex]
    print 'the error rate is: ',float(errorCount)/len(testSet)
    #return vocabList,fullText


spamTest()