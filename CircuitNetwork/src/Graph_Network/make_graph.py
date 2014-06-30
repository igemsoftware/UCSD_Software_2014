import pydot

# Creates a graph and its image from an input file.
def make_graph(input_file_name, output_file_name):

	# Opens an input file.
	f = open(input_file_name, "r")

	# Creates a pydot graph.
	graph = pydot.Dot('graphname', graph_type='digraph')

	# Generates an edge from each line and adds to the graph.
	for lines in f.readlines():
	
		# Creates a comma-split array.
        	elements = lines.split(',')
	        node_1 = elements[0]
        	node_2 = elements[1]
	        weight = elements[2]
	
		# Converts the array into an edge.
	        edge = pydot.Edge(node_1, node_2, label=weight)
	
		# Adds the edge to the graph.
        	graph.add_edge(edge)
    	
	f.close()
	
	# Creates a .png file.
    	graph.write_png(output_file_name + ".png")
