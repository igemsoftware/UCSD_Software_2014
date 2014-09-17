import networkx as nx
import numpy as np
import sqlite3 
import itertools as it
import heapq as hp
import pandas as pd

def create_reach_matrix(graph,path_length, breadcrumbs = True): 
    """returns a reachability matrix in the form of a pandas dataframe with the 
    given path length specified
    Args:
     	breadcrumbs: allows you to specify if you want to add matrixes 
    together as the reachability table is being created. Else you get a 
    reachability matrix for nodes reaching each other by the given path_length.
    
    
    Examples. The following data is test data. Uncomment to use. 
    data = [(1,4), (2,1), (2,3), (3,1), (3,4), (4,3)]
    ex 1. reach(graph, 4, accumulate = True)
    ex 2. reach(graph, 4, accumulate = False)
    """     
            
    adj_matrix = nx.adjacency_matrix(graph)
    #print "printing the adjacency matrix"
    #print adj_matrix
    
    #creating the reachability matrix
    reach_matrix = np.matrix(adj_matrix)
    temp_matrix = np.matrix(adj_matrix)
    
    #subtracting one because you start at A^2
    if(breadcrumbs == True):
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
    reach_matrix = np.transpose(reach_matrix)
    reach_matrix = np.array(reach_matrix)
    return reach_matrix, graph.nodes()
    
def write_reach_matrix(reach_matrix, labels):
	"""
	Args: 
	reach_matrix: a numpy matrix with the reachability calculated
	labels: the labels for the columns and the rows. 
	"""
	reach_df = pd.DataFrame.from_dict(reach_matrix)
	reach_df.columns = labels
	reach_df.index = labels
	reach_df.to_csv("reach_matrix.csv", index = True)

def read_reach_matrix():
	""" Opens the reach_ability matrix as a dataframe pandas object
	"""
	global reach_df 
	reach_df = pd.DataFrame.from_csv("reach_matrix.csv")
	return reach_df
	
    
def reach(query_statement):
	"""Returns a boolean value to tell you whether point_a can reach point_b 
	Must call read_reach_matrix() for this method. Currently only handles the
	buffer case.
	"""
	
	query = query_statement.strip()
	input, output = query.split(' ---> ')
	#input = [x.strip() for x in input]
	#output = [x.strip() for x in output]
	#input = input.split(' and ')
	#output = input.split(' and ')
	#input = [x.strip() for x in input]
	#output = [x.strip() for x in output]
	
	reach_value = reach_df.loc(output, input)
	print "the current output and input values are", input, output
	print  'the current reach value is', reach_df.loc(output, input)
	if reach_value == 0:
		return False
	elif reach_value > 0:
		return True
        
'''
def reach_converge_nodes(reach, *nodes_list):
    """
    returns priority queue with the best convergence or an empty queue if 
    there is none
    @param reach is the table that you want to use
    @param nodes_list is the list of nodes for which you want a convergence point
    """
    #need to use the reachability table to 
    print nodes_list
    #conv_array  = np.array([*node_list])
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
'''
def grapher():
	"""Returns a graph that can be passed onto the create_reach_matrix
	"""
	graph = nx.DiGraph()
    
	#data = [(1,4), (2,1), (2,3), (3,1), (3,4), (4,3)]
	data = [('hi','bye'), ('hi','sigh'), ('sigh','cry'), ('back','cry'), ('cry','bye')]
	#data = [(995,777),(999137,154), (999137,777), (995,154)]
	for edge in data:
		graph.add_edge(*edge)
    
	#selecting all of the nodes from the sql db
	#data = cur.select("")
    
	#adding all of the nodes from the sql db
    
	#for edge in data:
	#graph.add_edges(node_pair[0], node_pair[1]) 
	return graph   
    
'''
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
            
'''            
#testing the reach_matrix
graph = grapher()  
path_length = len(graph.nodes()) 
reach_mat, labels = create_reach_matrix(graph, 5)
print labels
write_reach_matrix(reach_mat, labels)
reach_mat = read_reach_matrix()
print reach_mat


#testing the accession method for the reach_matrix
print reach_mat.index
print reach_mat
"""
for item in reach_mat.index:
	print item, "is of type", type(item)
"""
print reach_mat.loc['bye', 'hi']
print reach('hi ---> cry')

