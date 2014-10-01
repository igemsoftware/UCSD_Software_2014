'''Randomly generates edge list (.txt), test file, for graph representation.'''



import os
import random
from sys import argv



def make_random_edge_list(output_file_path, output_file, number_of_edges):
    '''
    Randomly generates edge list (.txt), test file, for graph representation.
    
    @param output_file_path: path to output file.
    @type output_file_path: string.
    
    @param output_file: name of edge list to be generated.
    @type output_file: string.
    
    @param number_of_edges: number of edges in test file.
    @type number_of_edges: int.
    '''
    
    # Quits if output path does not exist.
    if not os.path.exists(output_file_path):
        print 'Output path does not exist.'
        return
    
    # Combines path and name of output file.
    path_and_file = os.path.join(output_file_path, output_file_name)
    
    # Opens empty file (.txt).
    f = open(path_and_file + ".txt", "w")
    
    # Writes random lines onto file using for loop.
    for i in range(number_of_edges):
        # List that holds line, or edge.
        a_list=[]
        # Randomly generates three digits, node 1, node 2, and the weight for each edge.
        for j in range(3):
            a_random_num = random.randint(1, 10)
            a_list.append(a_random_num)
            # Writes line, or edge.
        f.write("%d, %d, %d\n" % (a_list[0], a_list[1], a_list[2]))
    
    f.close()
    


'''Main'''


    
# Command line arguments.
script, output_file_path, output_file_name, edge_number = argv



make_random_edge_list(output_file_path, output_file_name, edge_number)


