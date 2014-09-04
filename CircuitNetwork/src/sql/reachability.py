import networkx as nx
import numpy as np
import sqlite3 
import itertools as it
import heapq as hp

def reach_matrix(graph,path_length, accumulate = True): 
    '''
    returns a reachability matrix with the given path length specified
    @param accumulate allows you to specify if you want to add matrixes 
    together as the reachability table is being created. Else you get a 
    reachability matrix for nodes reaching each other by the given path_length.
    
    
    Examples. The following data is test data. Uncomment to use. 
    data = [(1,4), (2,1), (2,3), (3,1), (3,4), (4,3)]
    ex 1. reach(graph, 4, accumulate = True)
    ex 2. reach(graph, 4, accumulate = False)
    '''      
        
    adj_matrix = nx.adjacency_matrix(graph)
    #print "printing the adjacency matrix"
    #print adj_matrix
    
    #creating the reachability matrix
    reach_matrix = np.matrix(adj_matrix)
    temp_matrix = np.matrix(adj_matrix)
    
    #subtracting one because you start at A^2
    if(accumulate == True):
        for count in range(path_length -1):
            temp_matrix = temp_matrix * adj_matrix
            reach_matrix += temp_matrix
    else:
        for count in range(path_length -1):
            temp_matrix = temp_matrix * adj_matrix
        reach_matrix = temp_matrix
    
    #print 10*"\n"
    #print "printing the reachability table before transpose"
    #print reach_matrix
    #print temp_matrix
    #print "printing the reachability table after transpose"
    #print adj_matrix
    trans_reach_mat = np.transpose(reach_matrix)
    return np.array(trans_reach_mat)
    
def reach(point_a, point_b, reach_matrix):
    '''
    returns a boolean value to tell you whether point_a can reach point_b 
    '''
    reach_value = reach_matrix[point_a][point_b]
    print reach_value
    if reach_value == 0:
        return False
    else: 
        return True
        
def reach_converge_nodes(reach, *nodes_list):
    '''
    returns priority queue with the best convergence or an empty queue if 
    there is none
    @param reach is the table that you want to use
    @param nodes_list is the list of nodes for which you want a convergence point
    '''
    #need to use the reachability table to 
    print nodes_list
    conv_array  = np.array([*node_list])
    row_len, col_len = conv_array.shape
    priority = 0
    priority_q = PriorityQueue()
    for row in range(row_len):
        curr_node = conv_array=[row]
        if 0 in row:
            priority = 0
        else:
            priority = sum(curr_node)
            #need to link back somehow. 
            priority_q.put((priority,value_of_current_node)
    return priority_q
    
def grapher():
    graph = nx.DiGraph()
    
    #data = [(1,4), (2,1), (2,3), (3,1), (3,4), (4,3)]
    #data = [(2,1), (2,3), (3,5), (5,4), (4,1)]
    data = [(995,777),(999137,154), (999137,777), (995,154)]
    for edge in data:
        graph.add_edge(*edge)
    
    #selecting all of the nodes from the sql db
    #data = cur.select("")
    
    #adding all of the nodes from the sql db
    
    #for edge in data:
    #   graph.add_edges(node_pair[0], node_pair[1]) 
    return graph   
    
def index_dict(graph):
    '''
    return a dictionary with the numerical indices of the 
    reachability table. 
    '''
    
    nodes = graph.nodes()
    index_dict = {}
    node_enum = enumerate(nodes)
    for node in node_enum:
        index_dict[node[1]] = node[0] 
    return index_dict
        
def index_by_str(column, row, indices):
    '''
    return the numerical indices of the reachability table
    @param row is the string representation of the row value
    @param column is the string representation of the column value
    @param indices is the dictionary containing indice numerical values. 
    '''
    
    return (indices[column], indices[row])

def get_subnetwork(inputs_list):
    """Finds the subnetwork made up from the inputs_list.

    Returns:
         all of the node values that are reachable from all nodes
	 in the input list
    """
    
    for inputs in inputs_list:
        get the column from the reach_matrix
	for reached in inputs:
            subnetwork.append()
#testing the reach_matrix
graph = grapher()  
path_length = len(graph.nodes()) 
reach_mat = reach_matrix(graph, 3)
print reach_mat

#testing the index maker
indices = index_dict(graph)
column, row = index_by_str(2,1, indices)
#print "Printing the indices dict"
#print indices
#print "Printing row and column information"
#print column, row

#testing the accession method for the reach_matrix
print reach(row, column, reach_mat)

print reach_convergence_nodes()


    
