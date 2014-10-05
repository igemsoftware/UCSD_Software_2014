import testfile as tf
x_coordinate,y_coordinate,species_table,input_transitions_table,operon_table, \
output_transitions_table,edge_table=tf.toReturn()

species_list,operon_list,input_transitions_ids,output_transitions_ids=tf.traversal()
'''
1. need to import position from graphviz
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
for node in species_table:
	f.write('\n\t\t\t{')
	f.write('\n\t\t\t\t"data":{')
	f.write('\n\t\t\t\t\t"id":"'+node[0]+'",')
	f.write('\n\t\t\t\t\t"name":"'+node[1]+'",')
	f.write('\n\t\t\t\t\t"type":"'+node[2]+'"')
	f.write('\n\t\t\t\t},')
	
	f.write('\n\t\t\t\t"position":{')
	f.write('\n\t\t\t\t\t"x":'+str(x_coordinate[numRuns])+',')
	f.write('\n\t\t\t\t\t"y":'+str(y_coordinate[numRuns]))
	f.write('\n\t\t\t\t},')
	
	current_species_list=node[0]
	shortest_path_species_list=species_list[0]
	boolean=compare(current_species_list,shortest_path_species_list)
	
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
for node in operon_table:
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
	f.write('\n\t\t\t\t\t"x":'+str(x_coordinate[numRuns])+',')
	f.write('\n\t\t\t\t\t"y":'+str(y_coordinate[numRuns]))
	f.write('\n\t\t\t\t},')
	
	current_operon_list=node[0]
	shortest_operon_list=operon_list[0]
	boolean=compare(current_operon_list,shortest_operon_list)
	
	f.write('\n\t\t\t\t"classes":"operon')
	
	if boolean:
		f.write(' shortestPath",')
	else:
		f.write('",')

	
	f.write('\n\t\t\t\t"selected":false')
	f.write('\n\t\t\t},')

	numRuns=0
	
for node in output_transitions_table:
	f.write('\n\t\t\t{')
	f.write('\n\t\t\t\t"data":{')
	f.write('\n\t\t\t\t\t"id":"'+str(node[0])+'"')
	f.write('\n\t\t\t\t},')
	
	f.write('\n\t\t\t\t"position":{')
	f.write('\n\t\t\t\t\t"x":'+str(x_coordinate[numRuns])+',')
	f.write('\n\t\t\t\t\t"y":'+str(y_coordinate[numRuns]))
	f.write('\n\t\t\t\t},')
	
	current_output_transition_list=node[0]
	shortest_output_transition_list=output_transitions_ids[0]
	boolean=compare(current_output_transition_list,shortest_output_transition_list)
	
	f.write('\n\t\t\t\t"classes":"output transition')
	
	if boolean:
		f.write(' shortestPath",')
	else:
		f.write('",')
	
	f.write('\n\t\t\t\t"selected":false')
	f.write('\n\t\t\t}')
	if numRuns<len(operon_table) - 1:
		f.write(',')
	numRuns+=1
	
device_number=0
f.write('\n\t\t],')
f.write('\n\t\t"edges":[')

edge_id=0
for edge in edge_table:
	
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
	if edge_id<(len(edge_table)-1):
		f.write(',')
	edge_id+=1

f.write('\n\t\t]')
f.write('\n\t}\n}')
	
f.close()





