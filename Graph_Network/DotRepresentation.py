"""Creates DOT representations of graphs from given edge-list files."""



"""Opens a graph file, possibly a text file."""
graphFile = open("./name_of_the_graph_file.txt")

"""Reads the graph file and splits it by lines."""
graphLines = graphFile.readlines()

"""Creates an array to hold the outputs."""
dotRepresentaionLines = ["graphFile { "]


"""Splits each line of graphLines by comma, reformats as dot format,
and appends to the output array, dotRepresentationLines."""
for aLine in graphLines:
	foo = aLine.split(',')
	bar = "%s--%s;", foo[0],foo[1]
	dotRepresentaionLines.append(bar)
	
"""Appends closing bracket to the array, lines."""
dotRepresentationLines.append("}")

"""Writes lines to a file."""
dotRepresentaionLines.write("aDotRepGraph.txt")
