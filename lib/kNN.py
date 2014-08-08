from numpy import *
import operator
import os as os

def create_dataset():
    group = array([[1.0,1.1],[1.0,1.0],[0, 0],[0,0.1]])
    labels = ['A','A','B','B']
    return group,labels

#example
#inX = [2.3,34,23]
#dataset = array([[1,2,3],[2,3,4],[4,5,6]])
#labels = ["atype","btype","atype"]
#return label
#when you use clssify function, you should normalize the dataSet and don't forget the vector inX 
def classify(inX,dataSet,labels,k):
    dataSetSize = dataSet.shape[0]
    
    #calculate the distance
    diffMat = tile(inX,(dataSetSize,1)) - dataSet
    sqDiffMat = diffMat ** 2
    sqDistance = sqDiffMat.sum(axis=1)
    distances = sqDistance ** 0.5
    #print distances
    sortedDistIndicies = distances.argsort() #return an array of indexing value ascendingly
    #print sortedDistIndicies
    classCount = {}
    
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1 #get value ,first arg is the key and the second is default
    #print classCount 
    sortedClassCount = sorted(classCount.iteritems(),
                              key = operator.itemgetter(1), #sorted with key,this is a  function
                              reverse = True) #now the first one is the max number
    
    #print sortedClassCount
    return sortedClassCount[0][0]

def file2matrix(filename):
    fr = open(filename)
    arrayOfLines = fr.readlines()
    numberOfLines = len(arrayOfLines)
    returnMat = zeros((numberOfLines, 3)) #return a new m*n zero matrix
    classLabelVector = []
    index = 0
    for line in arrayOfLines:
        line = line.strip() #strip enter character
        listFormLine = line.split('\t')
        returnMat[index,:] = listFormLine[0:3] #give the value of 0-2 to the index line
        classLabelVector.append(listFormLine[-1]) #get the last element
        index += 1

    return returnMat,classLabelVector
    
#normalizing numeric value
#because of the value is strongly affect the distance although they are as important as others
#newValue = (oldValue - min )/( max - min)
def autoNorm(dataSet):
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    ranges = maxVals - minVals
    normDataSet = zeros(shape(dataSet))
    m = dataSet.shape[0]
    normDataSet = dataSet - tile(minVals, (m, 1))
    normDataSet = normDataSet / tile(ranges, (m, 1))
    return normDataSet, ranges, minVals
    
def classTest(filename):
    hoRatio = 0.10
    dataMat, labels = file2matrix(filename)
    normMat, ranges, minVals = autoNorm(dataMat)
    lines = normMat.shape[0] 
    errorCount = 0.0
    numTestVectors = int(lines * hoRatio)
    for i in range(numTestVectors):
        classifyResult = classify(normMat[i,:], normMat[numTestVectors:lines,:], labels, 3)
        print "the classifier came back with: %s, the real answer is: %s" % (classifyResult,labels[i])
        
        if (classifyResult != labels[i]):
            errorCount += 1.0

    print "the total error is %d and the fault rate is %f" %(errorCount, errorCount/(lines-numTestVectors))

def img2vector(filename):
    returnVector = zeros((1,1024))
    fr = open(filename)
    for i in range(32):
        lineStr = fr.readline()
        for j in range(32):
            returnVector[0,i*32+j] = int(lineStr)
    return returnVector

def classifyHandler(filename):
    resultList = ['Not at all','In little dose','In large dose']
    #index = 0
    argList = []
    argList.append(float(raw_input("percentage of first argument: ")))
    argList.append(float(raw_input("percentage of second argument: ")))
    argList.append(float(raw_input("percentage of third argument: ")))
    #argList[index] = float(raw_input("percentage of first argument: "))
    #index = index + 1
    #argList[index] = float(raw_input("percentage of second argument: "))
    #index = index + 1
    #argList[index] = float(raw_input("percentage of third argument: "))
    #index = index + 1
    
    inX = array([argList[0], argList[1], argList[2]])
    dataMat, labels = file2matrix(filename)
    normMat, ranges, minVals = autoNorm(dataMat)
    classifyResult = classfiy((inX-minVals)/ranges, normMat, labels, 3)
    return classifyResult 


def handwritingClassTest(trainingPath, testPath):
    hwLabels = []
    trainingFileList = os.listdir(trainingPath)
    m = len(trainingFileList)
    trainingMat = zeros([m,1024])
    for i in range(m):
        fileNameStr = trainingFileList[i]
        fileStr = fileNameStr.split('.')[0]
        trainingMat[i,:] = img2vector('%s%s' % (trainingPath,fileNameStr))
        numStr = fileStr.split('_')[1]
        hwLabels.append(numStr)

    testFileList = os.listdir(testPath)
    errorCount = 0.0
    mTest = len(testFileList)
    for i in range(mTest):
        fileNameStr = testFileList[i]
        fileStr = fileNameStr.split('.')[0]
        numStr = fileStr.split("-")[0]
        testVector = img2vector('%s%s' % (testPath, fileNameStr))
        #here trainingMat only has 0 or 1 values so we don't need normalization
        classifyResult = classify(testVector, trainingMat, hwLabels, 3)
        if classifyResult != hwLabels[i]:
            errorCount += 1.0

    print "\nthe total number of errors is: %d "% errorCount
    print "\nthe total error rate is: %f"%(errorCount/float(mTest))

def handwritingClassifyer(inX, trainingPath):
    hwLabels = []
    trainingFileList = os.listdir(trainingPath)
    m = len(trainingFileList)
    trainingMat = zeros([m,1024])
    for i in range(m):
        fileNameStr = trainingFileList[i]
        fileStr = fileNameStr.split('.')[0]
        trainingMat[i,:] = img2vector('%s%s' % (trainingPath,fileNameStr))
        numStr = fileStr.split("_")[0]
        hwLabels.append(numStr)
    result = classify(inX, trainingMat, hwLabels, 3)
    return result
    