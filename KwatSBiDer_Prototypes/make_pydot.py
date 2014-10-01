'''Creates pydot text, graph, and image from edge list (.txt).'''



import os
from sys import argv
import pydot



def make_pydot_text(input_file_path, input_file, output_file_path, output_file):
	'''
	Creates pydot text (.txt) from edges list (.txt).
	
	@param input_file_path: path to input file.
	@type input_file_path: string.
	
	@param input_file: input edge list (.txt).
	@type input_file: .txt.
	
	@param output_file_path: path to output file.
	@type output_file_path: string.
	
	@param output_file: output file (.txt).
	@type output_file: string.
	'''
	
	# Quits if any file path does not exist.
	if not os.path.exists(input_file_path):
		print 'Input file path does not exist!'
		return
	if not os.path.exists(output_file_path):
		print 'Output file path does not exist!'
		return
	
	# Combines file path and file name.
	full_input_file_name = os.path.join(input_file_path, input_file)
	full_output_file_name = os.path.join(output_file_path, output_file)
	
	# Opens input and output files.
	in_f = open(full_input_file_name, 'r')
	out_f = open(full_output_file_name + ".txt", 'w')

	# Reads edges file (.txt) by line.
	edges = in_f.readlines()

	# Creates array to hold output.
	out_f.write("Graph\n{\n")
	
	# Converts each edge line into dot-representing format.
	for a_line in edges:
	
		# Comma splits.
		split = a_line.split(',')
	
		# Strips any space.
		split[0].strip(' ')
		split[1].strip(' ')
		
		# Generates dot-representing format and writes to output file.
		a_dot_edge = "%s--%s" % (split[0], split[1])
		out_f.write(a_dot_edge)
	
	# End of output array.	
	out_f.write("}")
	
	# Closes input and output files.
	in_f.close()
	out_f.close()



def make_pydot_graph(input_file_path, input_file, output_file_path, output_file):
	'''
	Creates pydot graph from input file (.txt).
	
	@param input_file_path: path to input file.
	@type input_file_path: string.
	
	@param input_file: input edge list (.txt).
	@type input_file: .txt.
	
	@param output_file_path: path to output file.
	@type output_file_path: string.
	
	@param output_file: output file (.txt).
	@type output_file: string.
	
	@return: graph in pydot format.
	'''
	
	# Quits if any file path does not exist.
	if not os.path.exists(input_file_path):
		print 'Input file path does not exist!'
		return
	if not os.path.exists(output_file_path):
		print 'Output file path does not exist!'
		return
	
	# Combines file path and file name.
	full_input_file_name = os.path.join(input_file_path, input_file)
	full_output_file_name = os.path.join(output_file_path, output_file)
	
	# Opens input and output files.
	in_f = open(full_input_file_name, 'r')
	out_f = open(full_output_file_name, 'w')

	# Creates pydot graph.
	graph = pydot.Dot('graph_name', graph_type='digraph')

	# Generates edge from each line and adds to graph.
	for a_line in in_f.readlines():
		# Creates comma-split array.
		elements = a_line.split(',')
		node_1 = elements[0]
		node_2 = elements[1]
		weight = elements[2]
		# Converts array into edge, and adds it to graph.
		an_edge = pydot.Edge(node_1, node_2, label=weight)
		graph.add_edge(an_edge)
		
	# Writes graph to output file.
	out_f.write(graph)
		
	in_f.close()
	out_f.close()

	return graph



def make_pydot_image(input_pydot_graph, output_file_path, output_file):
	'''
	Creates pydot image from input file (.txt).
	
	@param input_pydot_graph: name of input pydot graph.
	@type input_pydot_graph: pydot graph.
	
	@param output_file_path: path to output file.
	@type output_file_path: string.
	
	@param output_file: output file (.txt).
	@type output_file: string.
	'''
	
	# Quits if output file path does not exist.
	if not os.path.exists(output_file_path):
		print 'Output file path does not exist!'
		return

	full_output_file_name = os.path.join(output_file_path, output_file)

	# Creates image file (.png) from pydot graph file.
	input_pydot_graph.write_png(output_file+ ".png")

def test():
	print "Test success!"

'''Main'''



# Command line arguments.
script, input_file_path, input_file, output_file_path, output_file = argv



make_pydot_text(input_file_path, input_file, output_file_path, output_file)
a_pydot_graph = make_pydot_graph(input_file_path, input_file, output_file_path, output_file)
make_pydot_image(a_pydot_graph, output_file_path, output_file)


