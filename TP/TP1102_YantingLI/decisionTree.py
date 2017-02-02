# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 09:50:48 2016

@author: yali
"""

import numpy as np
import sklearn as sk
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
from scipy import stats

#Building the Decision tree
training_data = np.load('training_data.npy')
traing_class = np.load('training_class.npy')
test_data = np.load('test_data.npy')
test_class = np.load('test_class.npy')

clf = tree.DecisionTreeClassifier(criterion='gini', random_state=np.random.RandomState(130))
clf = clf.fit(training_data, traing_class)

with open('iris.dot', 'w') as f:
    f = tree.export_graphviz(clf, out_file=f)
prediction = clf.predict(test_data)
print prediction

#Computing Confidence Interval
a = np.array([])
for i in range(len(test_class)):
    if test_class[i] == prediction[i]:
        a = np.append(a, [1])
    else:
        a = np.append(a, [0])
print stats.norm.interval(0.95, loc=np.mean(a), scale=stats.sem(a))


#Overcoming Overfitting