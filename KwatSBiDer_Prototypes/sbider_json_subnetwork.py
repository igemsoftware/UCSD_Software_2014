
# coding: utf-8

## Subnetwork Creator

# In[1]:

def get_all_input_transition_species(cursor, input_transition_id):
    species_list = []
    species_list_unformatted = db.db_select(cursor, "InputTransitionSpecies", ["spe_id"], ["it_id"], ["="], ["'" + input_transition_id + "'"], [""])
    species_list_unformatted = species_list_unformatted.fetchall()
    
    ###print "species_list_unformatted:", species_list_unformatted
    
    for species_index in range(len(species_list_unformatted)):
        species_list.append(list(species_list_unformatted[species_index]))
        
    #print "(before) species_list:", species_list

    species_list = db.uniquely_merge_list_of_lists(species_list)
    
    #print "(after) species_list:", species_list
    
    return species_list


# In[2]:

def get_all_output_transition_species(cursor, input_transition_id):
    species_list = []
    species_list_unformatted = db.db_select(cursor, "OutputTransitionSpecies", ["spe_id"], ["ot_id"], ["="], ["'" + input_transition_id + "'"], [""])
    species_list_unformatted = species_list_unformatted.fetchall()
    
    ###print "species_list_unformatted:", species_list_unformatted

    for species_index in range(len(species_list_unformatted)):
        species_list.append(list(species_list_unformatted[species_index]))
    
    #print "(before) species_list:", species_list

    species_list = db.uniquely_merge_list_of_lists(species_list)
    
    #print "(after) species_list:", species_list
        
    return species_list


# In[3]:

def get_traversal_network(cursor, species_paths_list, operon_paths_list, input_transitions_paths_list, output_transitions_paths_list):
    
    #subnetwork = get_path(input_dictionary, output_dictionary, input_species_list, output_species_list)
    
    """Collecting subnetwork information."""
    # operon_paths_list, input_transitions_paths_list,\
    # output_transitions_paths_list, species_paths_list = get_path()

    # Operon Nodes Validation Done
    operon_ids_list = db.uniquely_merge_list_of_lists(operon_paths_list)
    operon_nodes_list = []
    for operon_id in operon_ids_list:
        operon_node = db.db_select(cursor,"Operon", ['ope_id', 'name', 'image'], ['ope_id'], ['='], [ "'" + operon_id + "'"], [""])
        operon_node = list(operon_node.fetchone())
        operon_node[0] = "ope_" + operon_node[0]
        operon_nodes_list.append(operon_node)
    
    # Species Nodes Validation Done
    species_ids_list = db.uniquely_merge_list_of_lists(species_paths_list)
    species_nodes_list = []
    for species_id in species_ids_list:
        
        #print "species_id:", species_id
        
        species_node = db.db_select(cursor, "Species", ['spe_id', 'name', 'type'], ['spe_id'], ['='], ["'" + species_id + "'"], [""])
        species_node = list(species_node.fetchone())
        species_node[0] = "spe_" + species_node[0]
        
        #print "species_node_id_abbreviated:", species_node
        
        species_nodes_list.append(species_node)
        
    # Input Transitions Validation Done
    input_transitions_id_list = db.uniquely_merge_list_of_lists(input_transitions_paths_list)
    input_transitions_nodes_list = []
    for input_transition_id in input_transitions_id_list:
        input_transitions_node = db.db_select(cursor,"InputTransition", ['it_id', 'logic'], ['it_id'], ['='], ["'" + input_transition_id + "'"], [""])
        input_transitions_node = list(input_transitions_node.fetchone())
        input_transitions_node[0] = "it_" + input_transitions_node[0]
        input_transitions_nodes_list.append(input_transitions_node)
        
    # Output Transitions Validation Done    
    output_transitions_id_list = db.uniquely_merge_list_of_lists(output_transitions_paths_list)
    output_transitions_nodes_list = []
    for output_transition_id in output_transitions_id_list:
        #output_transition_node = db_select(cursor,"OutputTransition", ['ot_id'], ['ot_id'], ['='], ["'" + output_transition_id + "'"], [""])
        #output_transition_node = list(output_transition_node.fetchone())
        #output_transitions_node_list.append(output_transitions_node)
        output_transitions_nodes_list.append(["ot_" + output_transition_id])
        
        
    source_id_target_id_list = []
    
    # operon_paths_list, input_transitions_paths_list,\
    # output_transitions_paths_list, species_paths_list
    
    for operon_path, input_transition_path, output_transition_path in    zip(operon_paths_list, input_transitions_paths_list, output_transitions_paths_list):

        for operon_id, input_transition_id, output_transition_id in zip(operon_path, input_transition_path, output_transition_path):

            #print "input_transition:", input_transition_id

            # adding all input_transition_species edges
            input_transition_species = get_all_input_transition_species(cur, input_transition_id)
            for species_id in input_transition_species:

                ###print "input_transition, species_id:", input_transition_id, ",",species_id

                source_id_target_id_list.append(["spe_" + species_id, "it_" + input_transition_id])

            #adding all input_transition_operon edges
            source_id_target_id_list.append(["it_" + input_transition_id, "ope_" + operon_id])

            #adding all output_transition_operon edges
            source_id_target_id_list.append(["ope_" + operon_id, "ot_" + input_transition_id])

            #adding all output_transition_species edges
            output_transition_species = get_all_output_transition_species(cur, input_transition_id)
            for species_id in output_transition_species:

                ###print "output_transition, species_id:", output_transition_id, ",", species_id

                source_id_target_id_list.append(["ot_" + output_transition_id, "spe_" + species_id])
        
    
    return species_nodes_list, input_transitions_nodes_list, operon_nodes_list, output_transitions_nodes_list, source_id_target_id_list


# In[3]:




## JSON Creator

# In[4]:

def create_json_subnetwork(species_nodes_list, input_transitions_nodes_list, operon_nodes_list, output_transitions_nodes_list, source_id_target_id_list):
    
    '''
    1. need to import position from networkx
    2. need to import name
    3. need to import literature information

    table=jsonCreator(input.items(),output.items(),['90,1','81,1'],['2','4','10','3'])
    '''
    def compare(object,list2):
        for item in list2:
            if item==object:
                return True
        return False

    f=open('sbider.json','w')
    species_name='test'
    SBOL_link='SBOL link'
    target_string_list=['TARGET STRING LIST']
    table=['this','is','not','going','to','work']
    numRuns=0

    x_coordinate = [1,1,1,1]
    y_coordinate = [1,2,3,4]


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
        f.write('\n\t\t\t\t\t"x":'+str(x_coordinate[0] * (numRuns + 1) * 100) +',')
        f.write('\n\t\t\t\t\t"y":'+str(y_coordinate[0] * 100))
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
        f.write('\n\t\t\t\t\t"id":"'+node[0]+'",')
        f.write('\n\t\t\t\t\t"logic":"'+node[1]+'"')
        f.write('\n\t\t\t\t},')

        f.write('\n\t\t\t\t"position":{')
        f.write('\n\t\t\t\t\t"x":'+str(x_coordinate[1] * (numRuns + 1) * 100)+',')
        f.write('\n\t\t\t\t\t"y":'+str(y_coordinate[1] * 100))
        f.write('\n\t\t\t\t},')



	#This needs to be phase out. 	
        #current_input_transition_list=node[0]
        #shortest_input_transitions_list=input_transitions_ids[0]
        #boolean=compare(current_input_transition_list,shortest_input_transitions_list)
	boolean = False



        f.write('\n\t\t\t\t"classes":"input transition IF')

        if boolean:
            f.write( ' shortestPath",')
        else:
            f.write('",')

        f.write('\n\t\t\t\t"selected":false')
        f.write('\n\t\t\t},')
        numRuns+=1
    """
    #def make_input_transitions_OR_table	
    numRuns=0
    for node in input_transitions_table:
        f.write('\n\t\t\t{')
        f.write('\n\t\t\t\t"data":{')
        f.write('\n\t\t\t\t\t"id":"'+node[0]+'",')
        f.write('\n\t\t\t\t\t"logic":"'+node[1]+'"')
        f.write('\n\t\t\t\t},')

        f.write('\n\t\t\t\t"position":{')
        f.write('\n\t\t\t\t\t"x":'+str(x_coordinate[numRuns])+',')
        f.write('\n\t\t\t\t\t"y":'+str(y_coordinate[numRuns]))
        f.write('\n\t\t\t\t},')

        current_input_transition_list=node[0]
        shortest_input_transitions_list=input_transitions_ids[0]
        boolean=compare(current_input_transition_OR_list,shortest_input_transitions_OR_list)

        f.write('\n\t\t\t\t"classes":"input transition OR')

        if boolean:
            f.write( ' shortestPath",')
        else:
            f.write('",')

        f.write('\n\t\t\t\t"selected":false')
        f.write('\n\t\t\t},')
        numRuns+=1

    #def make_input_transitions_AND_table	
    numRuns=0
    for node in input_transitions_table:
        f.write('\n\t\t\t{')
        f.write('\n\t\t\t\t"data":{')
        f.write('\n\t\t\t\t\t"id":"'+node[0]+'",')
        f.write('\n\t\t\t\t\t"logic":"'+node[1]+'"')
        f.write('\n\t\t\t\t},')

        f.write('\n\t\t\t\t"position":{')
        f.write('\n\t\t\t\t\t"x":'+str(x_coordinate[numRuns])+',')
        f.write('\n\t\t\t\t\t"y":'+str(y_coordinate[numRuns]))
        f.write('\n\t\t\t\t},')

        current_input_transition_list=node[0]
        shortest_input_transitions_list=input_transitions_ids[0]
        boolean=compare(current_input_transition_list,shortest_input_transitions_list)

        f.write('\n\t\t\t\t"classes":"input transition NOT')

        if boolean:
            f.write( ' shortestPath",')
        else:
            f.write('",')

        f.write('\n\t\t\t\t"selected":false')
        f.write('\n\t\t\t},')
        numRuns+=1

    #def make_input_transitions_NOT_table	
    numRuns=0
    for node in input_transitions_table:
        f.write('\n\t\t\t{')
        f.write('\n\t\t\t\t"data":{')
        f.write('\n\t\t\t\t\t"id":"'+node[0]+'",')
        f.write('\n\t\t\t\t\t"logic":"'+node[1]+'"')
        f.write('\n\t\t\t\t},')

        f.write('\n\t\t\t\t"position":{')
        f.write('\n\t\t\t\t\t"x":'+str(x_coordinate[numRuns])+',')
        f.write('\n\t\t\t\t\t"y":'+str(y_coordinate[numRuns]))
        f.write('\n\t\t\t\t},')

        current_input_transition_list=node[0]
        shortest_input_transitions_list=input_transitions_ids[0]
        boolean=compare(current_input_transition_list,shortest_input_transitions_list)

        f.write('\n\t\t\t\t"classes":"input transition NOT')

        if boolean:
            f.write( ' shortestPath",')
        else:
            f.write('",')

        f.write('\n\t\t\t\t"selected":false')
        f.write('\n\t\t\t},')
        numRuns+=1
    """


    numRuns=0
    for node in operon_nodes_list:

	###print "species node:", node
	#node[2] currently undefined. Fix in database. 
	node[2] = "None"

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
        f.write('\n\t\t\t\t\t"x":'+str(x_coordinate[2] * (numRuns + 1) * 100)+',')
        f.write('\n\t\t\t\t\t"y":'+str(y_coordinate[2] * 100))
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

	print "numRuns:", numRuns
	print "x_coordinate[3]:", x_coordinate[3], "\n"

        f.write('\n\t\t\t\t\t"x":'+str(x_coordinate[3] * (numRuns + 1) * 100)+',')
        f.write('\n\t\t\t\t\t"y":'+str(y_coordinate[3] * 100))
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


# In[5]:

import database_pytools as db
conn, cur = db.db_open("sbider.db")

species_paths_list = [['11', '13', '20','21', '33'], ['39','36', '1', '2', '9','8']]
operon_paths_list = [ ['1,1', '2,1', '3,1'], ['2,1', '46,1', '47,1', '57,1'] ]
input_transitions_paths_list = [ ['1', '3', '5'], ['2', '72', '75', '98'] ]
output_transitions_paths_list = [ ['1', '3', '5'], ['2', '72', '75', '98'] ]

species_nodes_list, input_transitions_nodes_list, operon_nodes_list,\
	output_transitions_nodes_list, source_id_target_id_list\
	 = get_traverse_subnetwork(cur, species_paths_list, operon_paths_list,\
	 input_transitions_paths_list, output_transitions_paths_list)


create_json_subnetwork(species_nodes_list, input_transitions_nodes_list,\ 
operon_nodes_list, output_transitions_nodes_list, source_id_target_id_list)

db.db_close(conn, cur)
