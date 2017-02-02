# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 08:47:30 2016

@author: yali
"""
import csv
import sklearn as sk
from sklearn.feature_extraction.text import CountVectorizer


f = open('a2')
lines = f.readlines()
s = ''
for line in lines:
    s = s + line

print s

'''  
count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform('a3.txt')
#print X_train_counts
  
categories = ['company','fruit'];