import networkx as nx
import numpy as np
import sqlite3 
       
graph = nx.graph()

edge_list = [(1,4), (2,1), (2,3), (3,1), (3,4), (4,3)]
for edge in edge_list:
    graph.add_edge(*edge)

#selecting all of the nodes from the sql db
data = cur.select("")

#adding all of the nodes from the sql db
for node_pair in data:
    graph.add_edges(node_pair[0], node_pair[1])
    
adj_matrix = graph.adjacency_matrix()

#creating the reachability matrix
reach_matrix = adj_matrix
temp_matrix = reach_matrix
for count in len(data) - 1:
    temp_matrix *= temp_matrix
    reach_matrix+= temp_matrix
    
    