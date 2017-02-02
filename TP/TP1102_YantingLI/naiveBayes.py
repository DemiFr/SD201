# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 08:34:15 2016
@author: yali
"""
import sklearn as sk
import numpy as np
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer
import random
from sklearn.cross_validation import train_test_split

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
    #print doc
    dataFiles.append(doc)
#print repr(dataFiles)

#Transfer the Array into Matrix
count_vect = CountVectorizer()
vectors = count_vect.fit_transform(dataFiles)
X=vectors.toarray()
#print vectors
#Split
TrainingSet,TestSet,TrainingCat,TestCat = train_test_split(X,Categories, test_size = 0.3)
#print X

TrainingSet=np.random.permutation(TrainingSet)

clf = MultinomialNB()
clf.fit(TrainingSet, TrainingCat)

print(clf.predict(TestSet))

#score
Score_ary = []
for i in range(1,len(TrainingSet)+1):
    Score_ary.append(clf.score(TestSet, TestCat))
print Score_ary

#k-fold cross validation