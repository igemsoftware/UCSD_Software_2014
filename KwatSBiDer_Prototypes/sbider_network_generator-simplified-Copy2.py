
# coding: utf-8

# In[1]:

import sqlite3
import database_pytools as db
import networkx as nx
conn, cur = db.db_open("sbider.db")


## Helper Methods

# In[2]:

def get_input_transition_species_dictionary(cursor):
    input_transitions_species_dict = {}
    input_transition_species_list = db.db_select(cur, "InputTransitionSpecies", ["it_id", "spe_id"])
    it_id_list = []
    for it_id, spe_id in input_transition_species_list:
        if it_id not in it_id_list:
            input_transitions_species_dict[it_id] = [spe_id]
            it_id_list.append(it_id)
        else:
            input_transitions_species_dict[it_id].append(spe_id) 
    return input_transitions_species_dict  


# In[3]:

def unique_node_list(node_list):
    """Duplicate nodes values are removed from the node_list"""
    unique_node_list = []
    used_node_id_list = []
    for node in node_list:
        #print node
        if node not in used_node_id_list:
            
            #print "node[id_column_index]:",node[id_column_index]
            
            unique_node_list.append(node)
            used_node_id_list.append(node)
    return unique_node_list


# In[4]:

def list_of_lists(list_of_tuples):
    """Convert list of tuples to list of lists"""
    list_of_lists = []
    for tup in list_of_tuples:
        list_of_lists.append(list(tup))
        
    #print list_of_lists
    
    return list_of_lists
        


# In[5]:

def list_of_tuples(list_of_lists):
    """Convert list of lists to list of tuples."""
    list_of_tuples = []
    for lst in list_of_lists:
        list_of_tuples.append(tuple(lst))
        
    #print list_of_lists
    
    return list_of_tuples


# In[6]:

def add_node_id_abbreviation(node, abbrev, index):
    """Adds an id abbreviation to node."""
    node[index] = abbrev + node[index]
    return node
    


# In[7]:

def add_node_list_id_abbreviation(node_list, abbrev, index):
    """Adds an id abbreviation to a list of nodes."""
    for node in node_list:
        node = add_node_id_abbreviation(node, abbrev, index)
    return node_list


# In[8]:

def add_edge_id_abbreviation(edge, abbrev1, abbrev2, index1 = 0, index2 = 0):
    return (abbrev1 + edge[0], abbrev2 + edge[1])


# In[9]:

def add_edge_list_id_abbreviation(edge_list, abbrev1, abbrev2, index1 = 0, index2 = 0):
    edge_list_abbrev = []
    for edge in edge_list:
        edge_list_abbrev.append(add_edge_id_abbreviation(edge, abbrev1, abbrev2, index1, index2))
    return edge_list_abbrev


# In[10]:

def print_list_entries(lst):
    for item in lst:
        print item


# In[11]:

def merge_list_of_lists(list_of_lists):
    condensed_list = []
    for lst in list_of_lists:
        condensed_list.extend(lst)
    return condensed_list
###print merge_list_of_lists([[1], [2]])


## Traverse Subnetwork

#### Node Creation

# In[12]:

def get_node_from_id(cursor, node_table_name, node_id, node_id_type):
    
    ###print "node_table_name:", node_table_name
    ###print "node_id:", node_id
    ###print "node_id_type:", node_id_type
    
    node_cursor = db.db_select(cursor, node_table_name,"*", [node_id_type], ["="], [node_id], [""] )
    
    #print "node_cursor:", node_cursor
    
    node = node_cursor.fetchone()
    
    #print "node:", node
    
    node = list(node)
    
    ###print "node:", node
    
    return node


# In[13]:

def get_node_list_from_other_node_id(cursor, node_other_node_relationship_table, other_node_id, other_node_id_type,
                                node_table_name, node_id_type):
    node_id = db.db_select(cursor, node_other_node_relationship_table,  
                                     [node_id_type], 
                                     [other_node_id_type], 
                                     ["="], 
                                     ["'" + other_node_id + "'"], 
                                     [""])
    
    #print "node_id:", node_id
    
    node_id_list = node_id.fetchall()
    node_id_list = list_of_lists(node_id_list)
    
    #print "node_id_list:", node_id_list
    
    node_list = []
    for node_id in node_id_list:
        #print "node_id:", node_id
        
        node = get_node_from_id(cursor, node_table_name, node_id[0], node_id_type)

        #print "node:", node
        
        node = list(node)
        node_list.append(node)
    return node_list


#### Extracting Subnetwork

# In[14]:

def determine_operon_activated_input_transition(cursor, starting_species_list, operon_id):
    """Determining which input transition is activating the operon."""
    starting_species_set = set(tuple(starting_species_list))
    
    ###print "starting_species_set:", starting_species_set
    
    it_trans_id_list = db.db_select(cur, "OperonInputTransition",  ["it_id"], ["ope_id"], ["="], ["'" + operon_id + "'"], [""])
    it_trans_id_list = it_trans_id_list.fetchall()
    it_trans_id_list = list_of_lists(it_trans_id_list)

    ###print "it_trans_id_list:", it_trans_id_list

    it_trans_id_list = merge_list_of_lists(it_trans_id_list)

    ###print "it_trans_id_list:", it_trans_id_list

    it_id_dict = get_input_transition_species_dictionary(cur)

    for it_trans_id in it_trans_id_list:

        ###print "Searching it_trans_list:", it_trans_id
        print "it_id_dict[it_trans_id]:", it_id_dict[it_trans_id]
        
        activating_species_set = set(it_id_dict[it_trans_id])
        
        print "activating_species_set:", activating_species_set
        
        if starting_species_set.issuperset(activating_species_set):
            return it_trans_id
    return None


##### Subnetwork Extraction

# In[15]:

def create_operon_node(cursor, operon_id):    
    """Create operon nodes from the corresponding operon_id."""    

    ###print "operon_id:", operon_id

    operon_node = get_node_from_id(cursor, "Operon", "'" + operon_id + "'", "ope_id")
    
    ###print "operon_node:", operon_node
    
    operon_node_abbrev = add_node_id_abbreviation(operon_node, "ope_", 0)
    
    ###print "operon_node_abbrev:", operon_node_abbrev

    
    return operon_node_abbrev, operon_id
       


# In[16]:

def create_input_transition_node(cursor, operon_id, starting_species_list):
    """Create input transition nodes from the corresponding operon_id."""    

    activated_it_id = determine_operon_activated_input_transition(cursor, starting_species_list, operon_id)

    ###print "activated_it_id:",activated_it_id

    it_node = db.db_select(cursor, "InputTransition", "*", ["it_id"], ["="], [activated_it_id], [""])
    it_node = list(it_node.fetchone())
    
    it_node_abbrev = add_node_id_abbreviation(it_node, "it_", 0)
    
    ###print "it_node_abbrev:", it_node_abbrev

    return it_node_abbrev, activated_it_id


# In[17]:

def create_output_transition_node(cursor, operon_id): 
    """Create input transition nodes from the corresponding operon_id."""    

    ot_node = get_node_list_from_other_node_id(cursor, "OperonOutputTransition", operon_id, "ope_id",
                            "OutputTransition", "ot_id" )[0]
    ot_id = ot_node[0]
    ###print "ot_node:", ot_node 

    ot_node_abbrev = add_node_id_abbreviation(ot_node, "ot_", 0)

    ###print "ot_node_abbrev:", ot_node_abbrev

    
    return ot_node_abbrev, ot_id
        


# In[18]:

def create_input_species_nodes(cursor, it_id):
    """Create species nodes from the corresponding it_id."""    

    it_species_nodes = get_node_list_from_other_node_id(cursor, "InputTransitionSpecies", it_id, "it_id",
                            "Species", "spe_id")
    it_species_nodes = it_species_nodes

    ###print "input_species_nodes:", input_species_nodes

    it_species_ids = [spe_id[0] for spe_id in it_species_nodes]
    it_species_nodes_abbrev = [add_node_id_abbreviation(spe_node, "spe_", 0) for spe_node in it_species_nodes ]
    it_species_nodes_abbrev = [tuple(tup) for tup in it_species_nodes_abbrev]

    ###print "input_species_ids:", input_species_ids

    return it_species_nodes_abbrev, it_species_ids
        


# In[19]:

def create_output_species_nodes(cursor, ot_id):
    """Create species nodes from the corresponding ot_id."""   
    
    ot_species_nodes = get_node_list_from_other_node_id(cursor, "OutputTransitionSpecies", ot_id, "ot_id",
                            "Species", "spe_id")

    ot_species_nodes = ot_species_nodes

    ###print "output_species_nodes:", output_species_nodes

    ot_species_ids = [spe_id[0] for spe_id in ot_species_nodes]
    ot_species_nodes_abbrev = [add_node_id_abbreviation(spe_node, "spe_", 0) for spe_node in ot_species_nodes ]
    ot_species_nodes_abbrev = [tuple(tup) for tup in ot_species_nodes_abbrev]

    ###print "output_species_ids:", output_species_ids
    
    return ot_species_nodes_abbrev, ot_species_ids
 


# In[20]:

def create_subnetwork_path(cursor, operon_path, starting_species_list):
    """Creating a subnetwork path."""
    
    species_set = set()
    input_transition_set = set()
    operon_set = set()
    output_transition_set = set()
    edge_path_list = []
    current_species_list = starting_species_list
    
    ###print "current_species_list:", current_species_list
    
    ###print "operon_path:", operon_path
    
    for operon in range(len(operon_path)):        
            
        operon_id = operon_path.pop(0)     
        
        ###print "operon_id:", operon_id

        operon_node_abbrev, _ = create_operon_node(cursor, operon_id)
        
        ###print "operon_node_abbrev:", operon_node_abbrev
        
        operon_set.add(tuple(operon_node_abbrev))
        
        ###print "operon_set:", operon_set
        
        
        
        it_node_abbrev, it_id = create_input_transition_node(cursor, operon_id, current_species_list)
        it_id_abbrev = it_node_abbrev[0]
        input_transition_set.add(tuple(it_node_abbrev))
        edge_path_list.append([it_node_abbrev[0], operon_node_abbrev[0]])

        
        ###print "input_transition_set:", input_transition_set
        
        
        
        ot_node_abbrev, ot_id = create_output_transition_node(cursor, operon_id)
        ot_id_abbrev = ot_node_abbrev[0]
        output_transition_set.add(tuple(ot_node_abbrev))
        edge_path_list.append([operon_node_abbrev[0], ot_node_abbrev[0]])

        #print "output_transition_set:", output_transition_set

        
        
        
        it_species_nodes_abbrev, _= create_input_species_nodes(cursor, it_id)
        for it_species_node_abbrev in it_species_nodes_abbrev:            
            species_set.add(tuple(it_species_node_abbrev))
            edge_path_list.append([it_species_node_abbrev[0], it_node_abbrev[0]])
           
        ###print "it_species_nodes_abbrev:", it_species_nodes_abbrev
        ###print "species_set:", species_set    
        
        
      
        ot_species_nodes_abbrev, ot_species_id_list  = create_output_species_nodes(cursor, ot_id)
        
        ###print "ot_species_nodes_abbrev:", ot_species_nodes_abbrev
        
        for ot_species_node_abbrev in ot_species_nodes_abbrev:            
            species_set.add(tuple(ot_species_node_abbrev))
            edge_path_list.append([ot_node_abbrev[0], ot_species_node_abbrev[0]])

        ###print "species_set:", species_set
        #print "edge_path_list:", edge_path_list
        
        current_species_list = ot_species_id_list
        
        ###print "current_species_list", current_species_list
        
        edge_path_list = list_of_tuples(edge_path_list)
        
        
    ###print "\nspecies_set", type(species_set), "\n"
    ###print "input_transition_set:", type(input_transition_set), "\n"
    ###print "operon_set:", type(operon_set), "\n"
    ###print "output_transition_set:", type(output_transition_set), "\n"
    ###print "edge_path_list:", type(edge_path_list), "\n"
        
    return species_set, input_transition_set, operon_set, output_transition_set, edge_path_list


# In[21]:

create_subnetwork_path(cur, ["8-1", "21-2"], ["2", "13"])


# In[22]:

def get_subnetwork(cursor, list_of_operon_paths, starting_species_list_of_list): 
    species_subnetwork_set = set()
    input_transition_subnetwork_set = set()
    operon_subnetwork_set = set()
    output_transition_subnetwork_set = set()
    source_id_target_id_set = set()
    source_id_target_id_paths = []
    
    for operon_path, starting_species_list in zip(list_of_operon_paths, starting_species_list_of_list):
        species_set, input_transition_set, operon_set,        output_transition_set, edge_path_list =        create_subnetwork_path(cursor, operon_path, starting_species_list)
        
        ###print "species_set:", species_set
        ###print "input_transition_set:", input_transition_set
        ###print "operon_set:", operon_set
        ###print "output_transition_set:", output_transition_set
        ###print "edge_path_list:", edge_path_list
        
        species_subnetwork_set = species_subnetwork_set.union(species_set)
        
        ###print "species_subnetwork_set:", species_subnetwork_set
        
        input_transition_subnetwork_set = input_transition_subnetwork_set.union(input_transition_set)
        
        ###print "input_transition_subnetwork_set:", input_transition_subnetwork_set
        
        operon_subnetwork_set = operon_subnetwork_set.union(operon_set)
        
        ###print "operon_subnetwork_set:", operon_subnetwork_set

        output_transition_subnetwork_set = output_transition_subnetwork_set.union(output_transition_set)
        
        ###print "output_transition_subnetwork_set:", output_transition_subnetwork_set

        source_id_target_id_set = source_id_target_id_set.union(set(edge_path_list))
        
        ###print "source_id_target_id_set:", source_id_target_id_set

       
    species_subnetwork_list = list_of_lists(species_subnetwork_set)
    input_transition_subnetwork_list = list_of_lists(input_transition_subnetwork_set)
    operon_subnetwork_list = list_of_lists(operon_subnetwork_set)
    output_transition_subnetwork_list = list_of_lists(output_transition_subnetwork_set)
    source_id_target_id_list = list_of_lists(source_id_target_id_set) 
    
    
    return species_subnetwork_list, input_transition_subnetwork_list,        operon_subnetwork_list, output_transition_subnetwork_list,        source_id_target_id_list 
        
#create_subnetwork_path(cur, ["2", "13"])
#get_subnetwork(cur,[["8-1", "21-2"]] , [["2", "13"]])
get_subnetwork(cur,[["8-1", "21-2"], ["1-1"]] , [["2", "13"], ["20","21"]])

        


# In[23]:

def get_subnetwork_paths(cursor, list_of_operon_paths):
    """List of paths."""
    for operon_path in list_of_operon_paths:
        _, __, ___, ____, edge_path_list =        create_subnetwork_path(cursor, operon_path, starting_species_list)
        source_id_target_id_paths.append(edge_path_list)


## Whole Network 

# In[24]:

"""COMPLETE"""

def get_whole_network(cursor):
    """Whole network data prep for json."""
    
    #*****Gathering all nodes
    species_nodes_list = db.db_select(cursor, "Species", ["spe_id", "name", "type"])
    species_nodes_list = species_nodes_list.fetchall()
    species_nodes_list = list_of_lists(species_nodes_list)
    species_nodes_list_abbrev = add_node_list_id_abbreviation(species_nodes_list, "spe_", 0)

    #print "species_nodes_list_abbrev:", species_nodes_list_abbrev

    input_transition_nodes_list = db.db_select(cursor, "InputTransition", ["it_id", "logic"])
    input_transition_nodes_list = input_transition_nodes_list.fetchall()
    input_transition_nodes_list = list_of_lists(input_transition_nodes_list)
    input_transition_nodes_list_abbrev = add_node_list_id_abbreviation(input_transition_nodes_list, "it_", 0)
          
    #print "input_transition_nodes_list:", input_transition_nodes_list

    operon_nodes_list = db.db_select(cursor,"Operon", ["ope_id", "name", "image"])
    operon_nodes_list = operon_nodes_list.fetchall()
    operon_nodes_list = list_of_lists(operon_nodes_list)
    operon_nodes_list_abbrev = add_node_list_id_abbreviation(operon_nodes_list, "ope_", 0)        
    
    #print "operon_nodes_list:", operon_nodes_list_abbrev

    output_transition_nodes_list = db.db_select(cursor, "OutputTransition", ["ot_id"])
    output_transition_nodes_list = output_transition_nodes_list.fetchall()
    output_transition_nodes_list = list_of_lists(output_transition_nodes_list)
    output_transition_nodes_list_abbrev = add_node_list_id_abbreviation(output_transition_nodes_list, "ot_", 0)
    
    species_nodes_list_abbrev, input_transition_nodes_list_abbrev, operon_nodes_list_abbrev, output_transition_nodes_list_abbrev
    
    #print "output_transition_nodes_list_abbrev:", output_transition_nodes_list_abbrev
    
    #********************************************Gathering all edges#********************************************#
    ##***********************************************************************************************************#
    ##***********************************************************************************************************#
    
    species_input_transition_edge_list = db.db_select(cursor,"InputTransitionSpecies", ["spe_id", "it_id"])
    species_input_transition_edge_list = species_input_transition_edge_list.fetchall()
    species_input_transition_edge_list = list_of_lists(species_input_transition_edge_list)
    species_input_transition_edge_list_abbrev = add_edge_list_id_abbreviation(species_input_transition_edge_list, 
                                                                                "spe_", "it_")
    #print_list_entries(species_input_transition_edge_list_abbrev)
    #print "species_input_transition_edge_list_abbrev:", species_input_transition_edge_list_abbrev
                                                                                 
    input_transition_operon_edge_list = db.db_select(cursor,"OperonInputTransition", ["it_id", "ope_id"])
    input_transition_operon_edge_list = input_transition_operon_edge_list.fetchall()
    input_transition_operon_edge_list = list_of_lists(input_transition_operon_edge_list)
    input_transition_operon_edge_list_abbrev = add_edge_list_id_abbreviation(input_transition_operon_edge_list,
                                                                                "it_", "ope_")
    #print_list_entries(input_transition_operon_edge_list_abbrev)
    #print "input_transition_operon_edge_list_abbrev:", input_transition_operon_edge_list_abbrev
    
    operon_output_transition_edge_list = db.db_select(cursor,"OperonOutputTransition", ["ope_id", "ot_id"])
    operon_output_transition_edge_list = operon_output_transition_edge_list.fetchall()
    operon_output_transition_edge_list = list_of_lists(operon_output_transition_edge_list)
    operon_output_transition_edge_list_abbrev = add_edge_list_id_abbreviation(operon_output_transition_edge_list,
                                                                                "ope_", "ot_")
    #print_list_entries(operon_output_transition_edge_list_abbrev)
    #print "operon_output_transition_edge_list_abbrev", operon_output_transition_edge_list_abbrev

    output_transition_species_edge_list = db.db_select(cursor,"OutputTransitionSpecies", ["ot_id", "spe_id"])
    output_transition_species_edge_list = output_transition_species_edge_list.fetchall()
    output_transition_species_edge_list = list_of_lists(output_transition_species_edge_list)
    output_transition_species_edge_list_abbrev = add_edge_list_id_abbreviation(output_transition_species_edge_list,
                                                                                "ot_", "spe_")
    #print_list_entries(output_transition_species_edge_list_abbrev)
    #print "output_transition_species_edge_list_abbrev:", output_transition_species_edge_list_abbrev
    
    all_edges = species_input_transition_edge_list_abbrev + input_transition_operon_edge_list_abbrev +    operon_output_transition_edge_list_abbrev + output_transition_species_edge_list_abbrev
    
    #print "all_edges:",all_edges
    
    return (species_nodes_list_abbrev, input_transition_nodes_list_abbrev, operon_nodes_list_abbrev,
            output_transition_nodes_list_abbrev, all_edges)

    


## JSON Generator

# In[25]:

def nx_node_coor_dictionary(node_list, edge_list):
    """Creates a dictionary of node positions using spring layout from networkx."""
    
    json_graph = nx.Graph()
    add_node_values_to_nxGraph(json_graph, node_list )
    json_graph.add_edges_from(edge_list)
    node_coor_dictionary = nx.spring_layout(json_graph)
    return node_coor_dictionary
    


# In[26]:

def add_node_values_to_nxGraph(nxGraph, node_list):
    """Extracts the node id and enters it into nxGraph."""
    
    for node in node_list:
        nxGraph.add_node(node[0])

    


# In[27]:

def create_json_network(json_file_path, species_nodes_list, input_transitions_nodes_list, 
                           operon_nodes_list, output_transitions_nodes_list, source_id_target_id_list):
    """Writes the whole network json."""
    
    node_list = species_nodes_list + input_transitions_nodes_list +                operon_nodes_list + output_transitions_nodes_list
    node_coor_dictionary = nx_node_coor_dictionary(node_list, source_id_target_id_list)
    #print node_coor_dictionary
    #return node_coor_dictionary

    f=open(json_file_path,'w')
    numRuns=0

    #NEEDS TO BE PHASED OUT!
    #x_coordinate = [1,1,1,1]
    #y_coordinate = [1,2,3,4]
    
    x_coor_factor = 10000
    y_coor_factor = 10000

    f.write('{\n\t"data" : { ')
    f.write('\n\t"selected" : true,')
    f.write('\n\t"_Annotations": [] ,')
    f.write('\n\t"shared_name" : "Test.sif",')
    f.write('\n\t"SUID" : 52,')
    f.write('\n\t"name":"Test.sif"')
    f.write('\n\t},')
    f.write('\n\t"elements":{')
    f.write('\n\t\t"nodes":[')

    #def make_species_nodes(f, species_table)
    for node in species_nodes_list:

        ###print "species node:", node
        #node[2] currently undefined. Fix in database. 
        node[2] = "None"

        f.write('\n\t\t\t{')
        f.write('\n\t\t\t\t"data":{')
        f.write('\n\t\t\t\t\t"id":"'+node[0]+'",')
        f.write('\n\t\t\t\t\t"name":"'+node[1]+'",')
        f.write('\n\t\t\t\t\t"type":"'+node[2]+'"')
        f.write('\n\t\t\t\t},')

        f.write('\n\t\t\t\t"position":{')
        f.write('\n\t\t\t\t\t"x":'+str( node_coor_dictionary[node[0]][0] * x_coor_factor )+',')
        f.write('\n\t\t\t\t\t"y":'+str( node_coor_dictionary[node[0]][1] * y_coor_factor))
        f.write('\n\t\t\t\t},')



        #This needs to be phase out. 
        #current_species_list=node[0]
        #shortest_path_species_list=species_list[0]
        #boolean=compare(current_species_list,shortest_path_species_list)
        boolean = False

        f.write('\n\t\t\t\t"classes":"species')

        if boolean:
            f.write(' shortestPath",')
        else:
            f.write('",')

        f.write('\n\t\t\t\t"selected":false')
        f.write('\n\t\t\t},')
        numRuns+=1

    #def make_input_transitions_IF_table
    numRuns=0
    for node in input_transitions_nodes_list:
        f.write('\n\t\t\t{')
        f.write('\n\t\t\t\t"data":{')
        #print "Make_input_transitions:", node
        f.write('\n\t\t\t\t\t"id":"'+node[0]+'",')
        f.write('\n\t\t\t\t\t"logic":"'+node[1]+'"')
        f.write('\n\t\t\t\t},')

        f.write('\n\t\t\t\t"position":{')
        f.write('\n\t\t\t\t\t"x":'+str( node_coor_dictionary[node[0]][0] * x_coor_factor)+',')
        f.write('\n\t\t\t\t\t"y":'+str( node_coor_dictionary[node[0]][1] * y_coor_factor))
        f.write('\n\t\t\t\t},')



        #This needs to be phase out. 
        #current_input_transition_list=node[0]
        #shortest_input_transitions_list=input_transitions_ids[0]
        #boolean=compare(current_input_transition_list,shortest_input_transitions_list)
        boolean = False

        f.write('\n\t\t\t\t"classes":"input transition')

        if boolean:
            f.write( ' shortestPath",')
        else:
            f.write('",')

        f.write('\n\t\t\t\t"selected":false')
        f.write('\n\t\t\t},')
        numRuns+=1

    numRuns=0
    for node in operon_nodes_list:

        ###print "species node:", node
        #node[2] CURRENTLY UNDEFINED. FIX IN DATABASE. 
        node[2] = "None"
        
        node[0] = node[0].replace(",", "-")

        f.write('\n\t\t\t{')
        f.write('\n\t\t\t\t"data":{')
        f.write('\n\t\t\t\t\t"id":"'+node[0]+'",')
        f.write('\n\t\t\t\t\t"SBOL":"'+node[2]+'",')
        f.write('\n\t\t\t\t\t"name":"'+node[1]+'"')
        #the following comments are located in the plasmid table,
        #not the operon table
        #f.write('\n\t\t\t\t\t"meriam_id":"",')
        #f.write('\n\t\t\t\t\t"Lit Ref":""')
        f.write('\n\t\t\t\t},')

        f.write('\n\t\t\t\t"position":{')
        f.write('\n\t\t\t\t\t"x":'+str( node_coor_dictionary[node[0]][0] * x_coor_factor)+',')
        f.write('\n\t\t\t\t\t"y":'+str( node_coor_dictionary[node[0]][1] * y_coor_factor))
        f.write('\n\t\t\t\t},')


        #This needs to be phase out. 
        #current_operon_list=node[0]
        #shortest_operon_list=operon_list[0]
        #boolean=compare(current_operon_list,shortest_operon_list)
        boolean = False



        f.write('\n\t\t\t\t"classes":"operon')

        if boolean:
            f.write(' shortestPath",')
        else:
            f.write('",')


        f.write('\n\t\t\t\t"selected":false')
        f.write('\n\t\t\t},')

        numRuns+= 1

    numRuns = 0
    for node in output_transitions_nodes_list:
        f.write('\n\t\t\t{')
        f.write('\n\t\t\t\t"data":{')
        f.write('\n\t\t\t\t\t"id":"'+str(node[0])+'"')
        f.write('\n\t\t\t\t},')

        f.write('\n\t\t\t\t"position":{')

        #print "numRuns:", numRuns
        #print "x_coordinate[3]:", x_coordinate[3], "\n"

        f.write('\n\t\t\t\t\t"x":'+str( node_coor_dictionary[node[0]][0] * x_coor_factor) +',')
        f.write('\n\t\t\t\t\t"y":'+str( node_coor_dictionary[node[0]][1] * y_coor_factor))
        f.write('\n\t\t\t\t},')


        #This needs to be phase out.
        #current_output_transition_list=node[0]
        #shortest_output_transition_list=output_transitions_ids[0]
        #boolean=compare(current_output_transition_list,shortest_output_transition_list)
        boolean = False



        f.write('\n\t\t\t\t"classes":"output transition')

        if boolean:
            f.write(' shortestPath",')
        else:
            f.write('",')

        f.write('\n\t\t\t\t"selected":false')
        f.write('\n\t\t\t}')
        if numRuns<len(output_transitions_nodes_list) - 1:
            f.write(',')
        numRuns+=1

    device_number=0
    f.write('\n\t\t],')
    f.write('\n\t\t"edges":[')

    edge_id=0
    for edge in source_id_target_id_list:

        #print edge

        f.write('\n\t\t\t{')
        f.write('\n\t\t\t\t"data":{')

        #THIS IS DEFINITELY A PROBLEM PLEASE FIX AT SOME POINT

        f.write('\n\t\t\t\t\t"id":"'+str(edge_id + 50)+'",')
        f.write('\n\t\t\t\t\t"source":"'+str(edge[0])+'",')
        f.write('\n\t\t\t\t\t"target":"'+ str(edge[1])+'"')
        f.write('\n\t\t\t\t},')
        f.write('\n\t\t\t\t\t"selected":false')
        f.write('\n\t\t\t}')
        if edge_id<(len(source_id_target_id_list)-1):
            f.write(',')
        edge_id+=1

    f.write('\n\t\t]')
    f.write('\n\t}\n}')

    f.close()


## BLAH

# In[28]:

import sbider_search_better_trimmed_v12 as search


# In[29]:

inp_dic, outp_dic = db.make_ope_id_spe_id_dicts(cur)


# In[30]:

search.main(cur, "cI > gfp")


#### CREATING THE JSON WHOLE AND SUBNETWORK 

# In[31]:

"""TEST WHOLE NETWORK JSON CREATION"""
def create_whole_network_json():
    """Generates the whole network json."""
    
    conn, cursor = db.db_open("sbider.db")
    json_info = get_whole_network(cursor)
    create_json_network("sbider_whole_network.json", *json_info)
    db.db_close(conn, cursor)
    #****sbider_server_path_name = "server/path"
    #****create_json_network(sbider_server_path_name, *json_info)


# In[32]:

def create_subnetwork_json(cursor, list_of_operon_paths, starting_species_list_of_lists):
    """Generates the subnetwork json."""
    
    conn, cursor = db.db_open("sbider.db")
    operon_input_transition_dictionary = get_input_transition_species_dictionary(cursor)
    

    json_info = get_subnetwork(cursor, list_of_operon_paths, starting_species_list_of_lists)

    create_json_network("sbider_subnetwork_hurrah.json", *json_info)
    
    ###db.db_close(conn, cursor)
    #****sbider_server_path_name = "server/path"
    #****create_json_network(sbider_server_path_name, *json_info)


# In[ ]:



