# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 11:30:56 2016

@author: yali
"""
import sklearn as sk
from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer
 

Train_ary = []
for i in range(3):
    f = open('a'+str(i))
    lines = f.readlines()   #read all the lines as a list['line1','line2','line3']
#    print lines             #lines is a list 
    
    doc = ''                #create a string 'doc'
    for line in lines:
        doc = doc + line    #transfer the list into a string 'doc'
    Train_ary.append(doc)   #Train_ary is a list of string
print Train_ary 

count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform(Train_ary)
X=X_train_counts.toarray()
print X