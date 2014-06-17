"This program creates a .dot representation from a graph."



"Reads a graph file, possibly a text file."
graphFile = readlines(aGraph.txt)

"Creates an array"
graphLines = [graphFile { ]

for line in graphFile.lines:
	foo = line.split(',')
	bar = "%s--%s;", foo[0],foo[1]
	graphLines.append(bar)
	
"Appends closing bracket to the array, lines"
lines.append("}")

"Writes lines to a file."
lines.write("aDotRepGraph.txt")

