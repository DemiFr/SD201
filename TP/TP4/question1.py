# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 13:46:32 2016

@author: yali
"""
import sklearn as sk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.cluster import k_means

f = open('text.txt')
lines = f.readlines()
corpus = []
for line in lines:
    corpus.append(line)
#print corpus

#First get a normalization vector and then transform into TF-idf:
count_vect = CountVectorizer(stop_words='english')
X_train_counts = count_vect.fit_transform(corpus)

tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
X = X_train_tfidf.toarray()
#print X
#print '  '

#Or only thansfer the corpus into a TF-idf vector:
vectorizer = TfidfVectorizer(min_df=1)
X_tfidf = vectorizer.fit_transform(corpus)
X = X_tfidf.toarray()
#print X

a,b,c = k_means(X,n_clusters=8, random_state=0)

print c