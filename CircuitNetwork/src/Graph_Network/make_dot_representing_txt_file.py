'''Creates dot-representing .txt file from edges .txt file.'''

from sys import argv

# Command line arguments.
script, input_file, output_file = argv

# Opens input and output files.
i_f = open(input_file, 'r')
o_f = open(output_file + ".txt", 'w')

# Reads the edges .txt file by line.
edges = i_f.readlines()

# Creates an array to hold output.
o_f.write("Graph\n{\n")

# Converts each edge line into dot-representing line.
for a_line in edges:
	
	# Comma splits.
	foo = a_line.split(',')
	
	# Strips any space.
	foo[0].strip(' ')
	foo[1].strip(' ')
	
	# Writes dot-representing line.
	bar = "%s--%s" % (foo[0], foo[1])
	o_f.write(bar)

# Ends output array.	
o_f.write("}")

# Closes input and output files.
i_f.close()
o_f.close()