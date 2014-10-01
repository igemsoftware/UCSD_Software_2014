def toReturn():
	x_coordinate=[1,2,3,4,5,6,7,8]
	y_coordinate=[9,10,11,12,13,14,15,16]
	
	species_table=[['species_id_1','name_1','type_1'],['species_id_2','name_2','type_2'], \
	['species_id_3','name_3','type_3'],['species_id_4','name_4','type_4'],['species_id_5','name_5','type_5']]
	
	input_transitons_table=[['input_id_1','logic_1'],['input_id_2','logic_2'], \
	['input_id_3','logic_3']]
	
	operon_table=[['operon_id_1','operon_name_1','http://SBOL_1'], \
	['operon_id_2','operon_name_2','http://SBOL_2'],['operon_id_3','operon_name_2','http://SBOL_2']]
	
	output_transitions_table=[[1],[2],[3]]
	
	edge_table=[['species_id_1','input_id_1'],['species_id_2','input_id_1'],['species_id_3','input_id_2'], \
	['species_id_4','input_id_1'], ['input_id_1','operon_id_1'],['input_id_2','operon_id_2'], \
	['input_id_3','operon_id_3'],['operon_id_1',1],['operon_id_2',2],['operon_id_3',3], \
	[1, 'species_id_3'],[3,'species_id_5']]
	
	return x_coordinate,y_coordinate,species_table,input_transitons_table, \
	operon_table,output_transitions_table,edge_table
	
def traversal():
	#calls Kwat's code to get traversal output
	species_list=[['species_id_1','species_id_5','species_id_4'],['species_id_2'],['species_id_3']]
	operon_list=[['operon_id_3'],['operon_id_2','operon_id_3']]
	input_transitions_ids=[['input_id_3','input_id_1'],['input_id_2'],['input_id_3']]
	output_transitions_ids=[[3,2],[1],[2]]
	return species_list,operon_list,input_transitions_ids,output_transitions_ids
