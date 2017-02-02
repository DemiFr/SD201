# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 09:55:30 2016

@author: yali
"""
import sklearn as sk
from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer
from sklearn.neighbors import KNeighborsClassifier
import random
from sklearn.cross_validation import train_test_split

#Read the documents and transfer into an array, with each line represent each doc.
Train_ary = []
Categories = ['company','company','company','company','company','fruit','fruit','fruit','fruit','fruit']
#Categories = [0,0,0,0,0,1,1,1,1,1]
for i in range(10):
    f = open('a'+str(i))
    lines = f.readlines()
    doc = ''
    for line in lines:
        doc = doc + line
    #print s
    Train_ary.append(doc)
#print repr(Train_ary)

tf_vec = TfidfVectorizer(sublinear_tf = True,
                        max_df = 0.5,stop_words = 'english');
tfidf=tf_vec.fit_transform(Train_ary)
vector=tfidf.array()

#Split
TrainingSet,TestSet,TrainingCat,TestCat = train_test_split(vector,Categories, test_size = 0.333)

print 'Train: ' + repr(len(TrainingSet))
print 'Test: ' + repr(len(TestSet))
print 'Train: ' + repr(len(TrainingCat))
print 'Test: ' + repr(len(TestCat))
print TestCat
print TrainingCat


#knn
Score_ary = []
for i in range(1,len(TrainingSet)+1):
    neigh = KNeighborsClassifier(n_neighbors=i)
    neigh.fit(TrainingSet,TrainingCat)
    Score_ary.append(neigh.score(TestSet, TestCat))
print Score_ary
#print neigh.score(TestSet, TestCat)