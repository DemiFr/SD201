# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 09:25:59 2016

@author: yali
"""

import numpy as np
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer
from sklearn import datasets
from sklearn import svm
import random
import sklearn as sk

dataFiles = []
#Categories = ['company','company','company','company','company','fruit','fruit','fruit','fruit','fruit']
Categories = ['fruit','fruit','company','company','company',
'company','company','company','fruit','fruit',
'company','company','company','fruit','company',
'company','fruit','company','fruit','fruit']
for i in range(20):
    f = open('b'+str(i))
    lines = f.readlines()
    doc = ''
    for line in lines:
        doc = doc + line
    dataFiles.append(doc)
    
#Transfer the Array into Matrix
count_vect = CountVectorizer()
vectors = count_vect.fit_transform(dataFiles)
X=vectors.toarray()
print X
#print vectors

#K-fold
# Etape1 split
a = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
a=np.array(a)
a=np.random.permutation(a)

#print a
n_splits=10
temp = int(len(dataFiles)/n_splits)
K_array = []
Cat_array = []
K = []
Cat = []
t = 0
for i in range(n_splits):
    for j in range(temp):
        K_array.append(dataFiles[a[t]])
        Cat_array.append(Categories[a[t]])
        t = t+1
#print K_array
#print Cat_array
K = np.reshape(K_array, (n_splits, temp))
Cat = np.reshape(Cat_array, (n_splits, temp))
#print K
#print Cat

# Etape 2
for i in range(n_splits):
    TrainingSet = []
    TestSet = []
    TrainingCat = []
    TestCat = []
    Score_ary = []
    for k in range(temp):
        TestSet.append(K[i][k])
    for j in range(n_splits):
        if i != j:
            
            for k in range(temp):
                TrainingSet.append(K[j][k])
                TrainingCat.append(Cat[j][k])
    #print TrainingSet
    #print TestSet
    
    TrainingSet1 = [TrainingSet[i:i+temp]for i in range(0, len(TrainingSet), temp)]
    print TrainingSet1    
    #Etape 3
#    clf = MultinomialNB()
#    clf.fit(TrainingSet1, TrainingCat)
#    print(clf.predict(TestSet))
    
#    for x in range(len(TrainingSet[t])):
#        Score_ary.append(clf.score(TestSet[x], TestCat[x]))
#        print Score_ary




            