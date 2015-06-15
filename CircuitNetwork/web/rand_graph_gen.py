import sys
import networkx as nx
import random
import matplotlib.pyplot as plt

G = nx.Graph()

#creates networkx graph with specified # of nodes
def node_gen(nodeNum):
	for node in range(nodeNum):
		G.add_node(node +1, total_edges = 0)
		# print "Added node# ", node +1
	# print "All %d nodes added." % nodeNum
	print "All nodes added."
	# print "List of nodes: ", G.nodes(False) 

#creates random edges between all nodes
def edge_gen(nodeNum, edgeNum):
	nodeCount = 1
	#list of all nodes in the graph 'G'
	nodeList = G.nodes(False)
	print "Creating %d edges per node." % edgeNum

	while (nodeCount <= nodeNum):
		#declaring new target node for edge
		newTarget = int(random.choice(nodeList))
		###counter to stop infinite loops/impossible solutions
		internalLoop = 0

		#breaks while loop if all nodes have max edges
		if (nodeCount == nodeNum or not nodeList):
			break

		while (G.node[nodeCount]['total_edges'] <= edgeNum):
			
			#breaks while loop if current node has max edges. 
			if (G.node[nodeCount]['total_edges'] == edgeNum):
				#removes completed node from possible choices
				if not nodeList:
					completeNode = nodeList.index(nodeCount)
					nodeList = nodeList.pop(completeNode)
				
				###iterates to next node in nodeList
				# print "*****"
				# print "Node %d completed" % nodeCount
				# print "*****"
				# print
				nodeCount += 1

				# print "Moving to node: ", nodeCount
				break

			###Catches impossible solutions/infinite loops
			elif (internalLoop >= nodeNum*5):
				nodeCount = nodeNum
				print
				print "Infinite loop reached, solution completed"
				break

			else:
				#checks if the new edge already exists
				if (newTarget == nodeCount or G.has_edge(nodeCount, newTarget) or G.has_edge(newTarget, nodeCount)):
					newTarget = int(random.choice(nodeList))
					internalLoop +=1
					# print "edge exists"

				elif (G.node[newTarget]['total_edges'] == edgeNum):
					newTarget = int(random.choice(nodeList))
					internalLoop += 1
					# print "Target node already has max edges"

				else:
					G.add_edge(nodeCount, newTarget)

					#raises the edge count for the source and target nodes
					G.node[nodeCount]['total_edges'] += 1
					G.node[newTarget]['total_edges'] += 1

					###succesfully adding edges restarts loop counter
					internalLoop = 0

					# print "*****"
					# print "Current node: ", nodeCount
					# print "Edge %d to %d added" % (nodeCount, newTarget)
					# print "Current node's # of edges: ", G.node[nodeCount]['total_edges']
					# print "*****"
					# print

	###prints list of all edges in graph			
	# for line in nx.generate_edgelist(G):
	# 	print line
	print "All edges added."

###Main function where:
### MaxNode = number of nodes in the graph
### MaxEdgeNode = max number of edges each node can have. 
###MaxEdgeNode must be less than MaxNode
def graph_gen(MaxNode,MaxEdgeNode):
	#Printing out basic info for inputs
	# print "Max Nodes: ", MaxNode
	# print "Max Edges per Node: ", MaxEdgeNode

	###checks to see if arguments are valid.
	if (MaxEdgeNode < MaxNode):
		node_gen(MaxNode)
		edge_gen (MaxNode, MaxEdgeNode)

		print "Graph completed."

		nx.write_gml(G, 'matrix_test_graph.gml')
		print "Graph saved to 'matrix_test_graph.gml'"

		nx.draw_networkx(G,node_size=150,node_color="blue",font_color="white")
		plt.show()

	else:
		print
		print "*****"
		print "MaxEdgeNode (argument 2) must be less than MaxNode (argument 1)"
		print "*****"
		print

if __name__ == '__main__' :
	a = int(sys.argv[1])
	b = int(sys.argv[2])

	graph_gen(a,b)