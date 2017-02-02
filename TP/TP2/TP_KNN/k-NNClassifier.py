import sklearn as sk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.neighbors import KNeighborsClassifier

import os, sys

trainingPath = "../dataset/training/"
files = os.listdir( trainingPath )
trainingFiles=[]
trainingCl=[]
for l in files:
    print l
    if "computer" not in l and "fruit" not in l:
        continue
    print l
    f=open(trainingPath+l,"r").read()
    if "computer" in l:
        trainingCl.append(1)
    else:
        trainingCl.append(0)
    trainingFiles.append(f)

testPath = "../dataset/test/"
files = os.listdir( testPath )
testFiles=[]
testCl=[]
for l in files:
    if "computer" not in l and "fruit" not in l:
        continue
    f=open(testPath+l,"r").read()
    if "computer" in l:
        testCl.append(1)
    else:
        testCl.append(0)
    testFiles.append(f)

count_vect = CountVectorizer(stop_words='english')
X_train_counts = count_vect.fit_transform(trainingFiles)
training=X_train_counts.toarray()
neigh = KNeighborsClassifier(n_neighbors=3)
neigh.fit(training,trainingCl)

X_test_counts = count_vect.transform(testFiles)
test=X_test_counts.toarray()
print neigh.score(test,testCl)

print("Accuracy:"+str(acc/len(testCl)))
