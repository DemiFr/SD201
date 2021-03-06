import operator
import math
def euclideanDistance(instance1, instance2, length):
	distance = 0
	for x in range(length):
		distance += pow((instance1[x] - instance2[x]), 2)
	return math.sqrt(distance)

def getNeighbors(trainingSet, testInstance, k):
	distances = []
	length = len(testInstance)-1
	for x in range(len(trainingSet)):
		dist = euclideanDistance(testInstance, trainingSet[x], length)
		distances.append((trainingSet[x], dist))
	distances.sort(key=operator.itemgetter(1))
	neighbors = []
	for x in range(k):
		neighbors.append(distances[x][0])
	return neighbors

trainSet = [[2, 2, 2, 'a'], [4, 4, 4, 'b'], [1,1,1,'a'], [2,2,2,'a'], [3,3,3,'b']]
testInstance = [5, 5, 5]
k = 3
neighbors = getNeighbors(trainSet, testInstance, k)
print(neighbors)
