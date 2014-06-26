# Creates DOT-represented-graph files from given edge-list files.

import argparse
#import sys

the_description = "This program creates DOT-represented-graph files from\ngiven edge-list files."
parser = argparse.ArgumentParser(description=the_description)

parser.add_argument("input", help="input file")
parser.add_argument("-o", "--output", action="store_true", help="specify output location")

args = parser.parse_args()

# Opens an input file, a graph file.
inputFile = open(args.input, "r")

# Opens an output file.
if args.output:
	outputFile = open("%s/DotRepresentationOutput.txt" % args.output, "r")

else:
	outputFile = open("./DotRepresentationOutput.txt", "w")

# Reads the graph file and splits it by lines.
inputLines = inputFile.readlines()

# Creates an array to hold the outputs.
outputFile.write("Graph\n{\n")

'''
Splits each line of graphLines by a comma, reformats in a dot format,
and writes on the output file.
'''
for aLine in inputLines:
	foo = aLine.split(',')
	foo[0].strip()
	foo[1].strip()
	bar = "%s--%s" % (foo[0], foo[1])
	outputFile.write(bar)
	
# Writes a closing bracket.
outputFile.write("}")

# Closes the files.
inputFile.close()
outputFile.close()
