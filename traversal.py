import sys
import random

### Classes ###
class Node(object):
	def __init__(self, ch=None):
		self.identifier = ch
		self.height = -1
		self.neighbors = []
		self.nodeType = None

# generates a tree, returning the root
# input the number of nodes in the tree
# output: the root of the tree
def generateTree(numNodes):
	counter = 0
	root = Node(counter)
	counter += 1
	root.height = 0
	queue = [root]
	root.nodeType = "device"
	while counter < numNodes and queue:
		currentNode = queue[0]
		queue = queue [1:]
		if currentNode.height % 2 == 1:
			nodeType = "device"
		else:
			nodeType = "transition"
		# create new nodes
		child1 = Node(counter)
		counter += 1
		child2 = Node(counter)
		counter += 1
		child1.height = currentNode.height +1
		child2.height = currentNode.height +1
		currentNode.neighbors.append(child1)
		currentNode.neighbors.append(child2)
		child1.neighbors.append(currentNode)
		child2.neighbors.append(currentNode)
		child1.nodeType = nodeType
		child2.nodeType = nodeType
		
		# add new nodes to queue
		queue.append(child1)
		queue.append(child2)
	return root

		
# prints out the tree
# input the root of the tree
def printTree(root):
	queue = [root]
	while queue:
		current = queue[0]
		queue = queue[1:]
		print "id: "+ str(current.identifier)+" height: "+ str(current.height)
		for neighbor in current.neighbors:
			if neighbor.height > current.height:
				queue.append(neighbor)
		
		

# make a tree with size twice as large as your input

root = generateTree(31)
# print out the tree
printTree(root)

# PUT YOUR CODE HERE


