import pydot

def make_graph(input_file_name, output_file_name):
	'''
	Create graph and image from input file.
	@param input_file_name: name of input file.
	@type input_file_name: string
	@param output_file_name: name of output file.
	@type output_file_name: string
	'''
	# Opens the input file.
	f = open(input_file_name, "r")

	# Creates pydot graph.
	graph = pydot.Dot('a_graph', graph_type='digraph')

	# Generates an edge from each line and adds to the graph.
	for lines in f.readlines():
		# Creates comma-split array.
		elements = lines.split(',')
		node_1 = elements[0]
		node_2 = elements[1]
		weight = elements[2]
		# Converts the array into an edge, and adds it to the graph.
		an_edge = pydot.Edge(node_1, node_2, label=weight)
		graph.add_edge(an_edge)
	f.close()
	
	# Creates make_random_edge_list_file .png file.
	graph.write_png(output_file_name + ".png")