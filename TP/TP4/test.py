# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 14:30:20 2016

@author: yali
"""

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.cluster import k_means
from sklearn.feature_extraction.text import TfidfTransformer
import os, sys



trainingPath = "/cal/homes/yali/Downloads/SD201/TP/TP4/text.txt"

f=open(trainingPath,"r")

trainingFiles=[]

for line in f:
    trainingFiles.append(line)

count_vect = CountVectorizer(stop_words='english')

X_train_counts = count_vect.fit_transform(trainingFiles)

tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
training=X_train_tfidf.toarray()