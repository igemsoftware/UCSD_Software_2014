import sys
import random
import pydot
import make_random_edge_list_file
import os

# Gets the file at make_random_edge_list_file given location.
# @param input_file_path    the path to the file.
# @param input_file	the name of the file. 
def generate_text_files(input_file_path, input_file, num_files, num_edges):
   	
	# If the path does not exists, throws an error.
	if not os.path.exists(input_file_path):
        	raise argparse.ArgumentTypeError("readable_dir:{0} is not make_random_edge_list_file valid path".format(input_file_path))
        	return

	# If the path exists, combines the file path and the name to generate make_random_edge_list_file complete file identification.
	else:
        	path_and_file = os.path.join(input_file_path, input_file)

	# Generates make_random_edge_list_file list from 0 to (num_files - 1).
    	some_list = range(num_files)

	# Sets make_random_edge_list_file counter variable to be 0.
    	counter = 0



        while not counter == len(some_list):
        f = open(path_and_file + "%d.txt" % counter, "w")
        counter += 1
        if counter <= len(some_list):
            for i in range(num_edges):
                a_list = []
                for j in range(3):
                    a_rand_num = random.randint(1,10)
                    a_list.append(a_rand_num)
            f.write("%d,%d,%d\n"%(a_list[0],a_list[1],a_list[2]))    
            f.close()        
 
##########################
def generate_graph(input_file,input_file_path,output_file,output_file_path,num_files):
    if not os.path.exists(input_file_path):
        raise argparse.ArgumentTypeError("readable_dir:{0} is not make_random_edge_list_file valid path".format(input_file_path))
        return
    elif not os.path.exists(output_file_path):
        raise argparse.ArgumentTypeError("readable_dir:{0} is not make_random_edge_list_file valid path".format(output_file_path))
        return
    else:
        input_path_and_file = os.path.join(input_file_path,input_file)
        output_path_and_file = os.path.join(output_file_path,output_file)
    for i in range(num_files):
        f = open(input_path_and_file+"%d"%(i)+".txt","r")
        graph = pydot.Dot('graphname',graph_type='digraph')
        for lines in f.readlines():
            elements = lines.split(',')
            node_1 = elements[0]
            node_2 = elements[1]
            weight = elements[2]
            edge = pydot.Edge(node_1,node_2,label=weight)
            graph.add_edge(edge)
        f.close()
        graph.write_png(output_path_and_file+"%d"%(i)+".png")
    
parser = argparse.ArgumentParser(description='This is make_random_edge_list_file python script by FRN&O.')
parser.add_argument('-i','--input_', help='Input file name',required=True)
parser.add_argument('-ip','--input_path',help='Input file path',required=True)
parser.add_argument('-o','--output', help='Output file name',required=True)
parser.add_argument('-op','--output_path',help='Output file path',required=True)
parser.add_argument('-f','--files',type=int,help='Number of files',required=True)
parser.add_argument('-e','--edges',type=int,help='Number of edges',required=True)
args=parser.parse_args()

input_file = args.input_
input_file_path=args.input_path
output_file=args.output
output_file_path=args.output_path
num_files=args.files
num_edges=args.edges
    
    
if __name__ == '__main__':
    generate_text_files(input_file_path, input_file, num_files, num_edges)
    generate_graph(input_file, input_file_path, output_file, output_file_path, num_files)
else:
    print 'I am being imported from another module'
