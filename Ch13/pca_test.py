__author__ = 'robin'
import pca

def test_2():
    dataMat=pca.loadDataSet('testSet.txt')
    lowDMat,recomMat=pca.pca(dataMat,2)
    print lowDMat
    print "---"
    print recomMat

def test_590():
    dataMat=pca.loadDataSet('secom.data')
    lowDMat,recomMat=pca.pca(dataMat,2)
    print lowDMat
    print "---"
    print recomMat


test_590()