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
	root.height = 0
	counter += 1
	queue = [root]
	root.nodeType = "device"
	while counter < numNodes and queue:
		currentNode = queue[0]
		queue = queue [2:]
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
		print 'IDENTIFIER:', queue[0].identifier
		print 'HEIGHT:', queue[0].height
		print 'NEIGHBORS:', queue[0].neighbors
		print 'NODETYPE:', queue[0].nodeType
		print '\n------------------------------------------------------------\n'
		print 'IDENTIFIER:', queue[1].identifier
		print 'HEIGHT:', queue[1].height
		print 'NEIGHBORS:', queue[1].neighbors
		print 'NODETYPE:', queue[1].nodeType
		print '\n------------------------------------------------------------\n'
		if counter == 31:
			print queue
			print '\n------------------------------------------------------------\n'
	return root

		
# how to use my code
# make a binary tree with 31 nodes (this is a full binary tree) and then return the root of the tree
generateTree(31)