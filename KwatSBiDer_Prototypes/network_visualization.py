'''
//Script Description:
    Extracting information directly from the database, sbider.db, and constructing 
    a Cytoscape.js executable JSON graph. This script essentially translates ALL 
    the database information via the JSON file. 

IMPORTANT: EVERY MODULE IN USE, INCLUDING THE DATABASE--SBIDER.DB, MUST BE IN THE SAME FOLDER

****************************
@author: Fernando Contreras
@email: f2contre@gmail.com
@project: SBiDer    
****************************

IMPORTANT: EVERY INPUT/OUTPUT AND DICTIONARY KEY/VALUE ARE STRINGS EXCEPT FOR THE EDGE DICTIONARY IN THE GET_NETWORK
           METHOD 
    
//Modules 
    @database_pytool.py: module constructed by SQL team, which is used to access different database 
    tables via the database select method
    
    @paths.py: module that I constructed, which is used to determine database path and output file path

//Global Variables
    @devices: access plasmid table in database, 
        value = list of tuples
        tuple = (device id, device name, miriam id, title, authors, journal, year) 
        
    @operon_device: access operon-plasmid relationship table in database,
        value = list of tuples
        tuple = (operon id, plasmid id)        
        
    @operators: access interactor table in database,
        value  = list of tuples
        tuple  = (interactor id, interactor name, interactor type)
       
    @operon_id: using the operon_device list to create a dictionary
        value = dictionary 
        dictionary = {device name_device id:[associated operons]}
            key: device name and id separated by '_'
            value: list of operons associated with device key 
            
    @operon_output: access operon-output transition relationship table and construct dictionary 
            value = dictionary 
            dictionary = {operon id:interactor id}
                key = operon id 
                value = associated output interactor id 
                
    @operon_intput: access operon-input transition relationship table and construct dictionary 
            value = dictionary 
            dictionary = {operon id:interactor id}
                key = operon id 
                value = associated input interactor id 
              
'''

import database_pytool as dp
import paths
#must open database first 
database_path = paths.file_path('/Users/K/Desktop/sbider_project/sbider_algorithms/Fernando/', 'sbider.db')
dp.open(database_path)

global devices
devices = dp.select('plasmid',['id','name', 'miriam_id','title','authors', 'journal', 'year'])


global operon_device
operon_device = dp.select('opr',['operon_id','plasmid_id'])


global operators
operators  = dp.select('interactor',['id','name', 'type'])


global operon_id
operon_id  =  {}
for device in devices:
    device_id = device[0]
    device_name = device[1]
    #incorporating device_id in order to prevent devices with the same name (i.e. pBAD-cI-pOR1-gfp) from being overwritten
    operon_id[device_name+'_'+device_id] = []
    for operons in operon_device:
        operons_id = operons[0]
        plasmid_id = operons[1]
        if device_id == plasmid_id:
            operon_id[device_name+'_'+device_id].append(operons_id)


global seen_interactor
seen_interactor = {}
for operator in operators:
    seen_interactor[operator[0]] = operator[1]


global operon_output
operon_output = dp.select('ootr',['operon_id','interactor_id'])
operon_output = {}
for opr in operon_output:
    if opr[0] not in operon_output:
        operon_output[opr[0]] = []
        operon_output[opr[0]].append(opr[1])
    else:
        operon_output[opr[0]].append(opr[1])


global operon_input
operon_input = dp.select('oitr',['operon_id','interactor_id'])
operon_input = {}
for opr in operon_input:
    if opr[0] not in operon_input:
        operon_input[opr[0]] = []
        operon_input[opr[0]].append(opr[1])
    else:
        operon_input[opr[0]].append(opr[1])



def get_outputs():
  
    #ignore this comment   
    device_output = {}
    for device in operon_id:
        operon_list = operon_id[device]
        device_output[device] = []
        chem_species = []
        for op_er in operon_list:
            if op_er in operon_output:
                interm_list = operon_output[op_er]
                chem_spec = chem_spec + interm_list
        for species in chem_species:
            #some operons have no output
            if species == 'none':
                device_output[device].append((species,'none'))
            else:
                device_output[device].append((species,seen_interactor[species]))
    return device_output    


def get_inputs():
    device_input = {}
    for device in operon_id:
        operon_list = operon_id[device]
        device_input[device] = []
        chem_spec = []
        for op_er in operon_list:
            if op_er in operon_input:
                interm_list = operon_input[op_er]
                chem_spec = chem_spec + interm_list
        for spec in chem_spec:
            #pCONST no input
            if spec == 'none':
                device_input[device].append((spec,'none'))
            else:
                device_input[device].append((spec, seen_interactor[spec]))    
    return device_input
    
    
def get_transitions():

    inputs  = operon_input
    outputs = operon_output
    device_operon = operon_id 
    device_trans = {}
    for device in device_operon:
        operon_list  = device_operon[device]
        #prevents similar keys from being overwritten 
        operon_counter = 1
        for operon in operon_list:
            device_name  = device+'_%d'%operon_counter
            device_trans[device_name] = []
            if operon in inputs:
                device_trans[device_name].append(tuple(inputs[operon]))
            if operon in outputs:
                device_trans[device_name].append(tuple(outputs[operon]))
            operon_counter+=1    
    return device_trans           
                
                
                
def get_sbol():
  
    operon_table = dp.select('operon',['id', 'name', 'sbol_image_path'])
    device_table  = operon_id
    operon_sbol = {}
    device_sbol = {}
    for operons in operon_table:
        operon_sbol[operons[0]] = operons[2]
    for device in device_table:
        dev_split = device.split('_')
        #using "d" to distinguish device,chemical specie, and transition id (imperative when contructing edges)
        device_id = "d"+dev_split[1]
        operon_list  = device_table[device]
        device_sbol[device_id] = []
        for operon in operon_list:
            if operon in operon_sbol:
                device_sbol[device_id].append(operon_sbol[operon])
        #converting sbol-path=list into a single string separated  by ','
        device_sbol[device_id] = ",".join(device_sbol[device_id])         
    return device_sbol       
        

def get_network():
   
    import networkx as nx
    device_trans = get_transitions()
    graph=nx.DiGraph()
    #counter used to assign new transitions 
    trans_counter=0
    edge_counter = 0
    edges = {}
    transitions = {}
    #a transition is assigned according to a device's amount of operons 
    for device in device_trans:
        device_attributes = device.split('_')
        device_id  = "d"+device_attributes[1]
        #input_output = [(inputs),(outputs)]
        input_output = device_trans[device]
        #some device input(s)/output(s) have yet to be populated
        if len(input_output) == 0:
            pass
        else:    
            inputs = list(input_output[0])
            outputs = list(input_output[1])
            if len(inputs) == 2:
                trans_name = 'AND'
                trans_id = 't%d'%trans_counter
                for input_ in inputs:
                    if input_ == 'none':
                        input_id = 'none'
                    else:
                        input_id  = "i"+input_
                    #creating networkx edge
                    graph.add_edge(input_id,trans_id)
                    graph.add_edge(trans_id,device_id)
                    #storing edge for JSON graph
                    edges[edge_counter] = (input_id, trans_id)
                    edge_counter+=1
                    edges[edge_counter] = (trans_id, device_id)
                    edge_counter+=1
                transitions[trans_id] = trans_name 
                trans_counter+=1
                if len(outputs) == 2:
                    trans_name  = 'IF_AND'
                    trans_id  = 't%d'%trans_counter
                    for output in outputs:
                        if output == 'none':
                            output_id = 'none'
                        else:
                            output_id  = "i"+output
                        graph.add_edge(device_id,trans_id)
                        graph.add_edge(trans_id, output_id)
                        edges[edge_counter] = (device_id, trans_id)
                        edge_counter+=1
                        edges[edge_counter] = (trans_id, output_id)
                        edge_counter+=1    
                    transitions[trans_id] = trans_name   
                    trans_counter+=1
                elif len(outputs) == 1:
                    trans_name = 'IF_AND'
                    trans_id = 't%d'%trans_counter
                    if outputs[0] == 'none':
                        output_id = 'none'
                    else:
                        output_id  = "i"+outputs[0]
                    graph.add_edge(device_id, trans_id)
                    graph.add_edge(trans_id, output_id)
                    edges[edge_counter] = (device_id, trans_id)
                    edge_counter+=1
                    edges[edge_counter] = (trans_id, output_id)
                    edge_counter+=1
                    transitions[trans_id] = trans_name
                    trans_counter+=1
            elif len(inputs) == 1:
                trans_name  = 'OR/NOT'
                trans_id = 't%d'%trans_counter
                if inputs[0] == 'none':
                    input_id = 'none'
                else:    
                    input_id  = "i"+inputs[0]
                graph.add_edge(input_id, trans_id)
                graph.add_edge(trans_id, device_id)
                edges[edge_counter] = (input_id, trans_id)
                edge_counter+=1
                edges[edge_counter] = (trans_id, device_id)
                edge_counter+=1
                transitions[trans_id] = trans_name
                trans_counter+=1
                if len(outputs) == 2:
                    trans_name  = 'IF_OR/NOT'
                    trans_id  = 't%d'%trans_counter
                    for output in outputs:
                        if output == 'none':
                            output_id = 'none'
                        else:
                            output_id  = "i"+output
                        graph.add_edge(device_id,trans_id)
                        graph.add_edge(trans_id, output_id)
                        edges[edge_counter] = (device_id, trans_id)
                        edge_counter+=1
                        edges[edge_counter] = (trans_id, output_id)
                        edge_counter+=1    
                    transitions[trans_id] = trans_name   
                    trans_counter+=1
                elif len(outputs) == 1:
                    trans_name = 'IF_OR/NOT'
                    trans_id = 't%d'%trans_counter
                    if outputs[0] == 'none':
                        output_id = 'none'
                    else:
                        output_id  = "i"+outputs[0]
                    graph.add_edge(device_id, trans_id)
                    graph.add_edge(trans_id, output_id)
                    edges[edge_counter] = (device_id, trans_id)
                    edge_counter+=1
                    edges[edge_counter] = (trans_id, output_id)
                    edge_counter+=1
                    transitions[trans_id] = trans_name
                    trans_counter+=1
    coordinates = nx.graphviz_layout(graph,prog='sfdp')
    return (edges,coordinates,transitions)   
        
        

def get_json(): 
   #assigning variables appropriately
    edges,coordinates,transitions = get_network()      
    #sbol_paths have yet to be populated
    #device_sbol = get_sbol()  
    abs_file_path = paths.file_path('C:\Users\Fernando\Desktop\Net_Viz','JSON_GRAPH.txt')
    #file header
    with open(abs_file_path,'w') as graph_net_file:
        graph_net_file.write('{\n')
        graph_net_file.write('    "data" : {\n')
        graph_net_file.write('    "selected" : true,\n')
        graph_net_file.write('    "name" : "Network_Graph"\n')
        graph_net_file.write('    },\n')
        graph_net_file.write('    "elements":{\n')
        
        #Constructing device nodes
        graph_net_file.write('        "nodes":[\n')
        for device in devices:
            device_id  = "d"+device[0]
            device_name = device[1]            
            if device_id not in coordinates:
                pass
            else:
                xy_coord = coordinates[device_id]
                x_coord = xy_coord[0]
                y_coord = xy_coord[1] 
                #sbol_path = device_sbol[device_id]
                graph_net_file.write('            {\n')
                graph_net_file.write('                "data":{\n')
                graph_net_file.write('                    "class": "Device Species",\n')
                graph_net_file.write('                    "SUID": %s,\n'%device_id)
                graph_net_file.write('                    "ID": "%s",\n'%device_id)
                graph_net_file.write('                    "Name": "%s",\n'%device_name)
                #TBD
                #graph_net_file.write('                    "Composition": %s\n'%sbol_path)
                #graph_net_file.write('                    "Miriam_ID": "%s",\n'%device[2])
                graph_net_file.write('                    "Title": "%s",\n'%device[3])
                graph_net_file.write('                    "Authors": "%s",\n'%device[4])
                graph_net_file.write('                    "Journal": "%s"\n'%device[5])
                graph_net_file.write('                    "Year": "%s"\n'%device[6])
                graph_net_file.write('                },\n')
                graph_net_file.write('                "position":{\n')
                graph_net_file.write('                    "x": %d,\n'%x_coord)
                graph_net_file.write('                    "y": %d\n'%y_coord)
                graph_net_file.write('                },\n')
                graph_net_file.write('                "selected": false\n')
                graph_net_file.write('            },\n') 
        
        #Constructing Operator Nodes
        for operator in operators:
            operator_id  = "i"+operator[0]
            operator_name  = operator[1]
            #operator_type  = operator[2]
            if operator_id not in coordinates:
                pass
            else:    
                xy_coord = coordinates[operator_id]
                x_coord = xy_coord[0]
                y_coord = xy_coord[1]
                graph_net_file.write('            {\n')
                graph_net_file.write('                "data":{\n')
                graph_net_file.write('                    "class": "Chemical Species",\n')
                graph_net_file.write('                    "SUID": %s,\n'%operator_id)
                graph_net_file.write('                    "ID": "%s",\n'%operator_id)
                graph_net_file.write('                    "Name": "%s",\n'%operator_name)
                #graph_net_file.write('                    "Type": "%s"\n'%operator_type)
                graph_net_file.write('                },\n')
                graph_net_file.write('                "position":{\n')
                graph_net_file.write('                    "x": %d,\n'%x_coord)
                graph_net_file.write('                    "y": %d\n'%y_coord)
                graph_net_file.write('                },\n')
                graph_net_file.write('                "selected": false\n')
                graph_net_file.write('            },\n') 
        
        #Constructing Transition Nodes
        for transition in transitions:
            trans_id = transition
            trans_type = transitions[transition] 
            if trans_id not in coordinates:
                pass
            else:
                xy_coord = coordinates[trans_id]
                x_coord = xy_coord[0]
                y_coord = xy_coord[1]
                graph_net_file.write('            {\n')
                graph_net_file.write('                "data":{\n')
                graph_net_file.write('                    "class": "Transition Species",\n')
                graph_net_file.write('                    "SUID": %s,\n'%trans_id)
                graph_net_file.write('                    "ID": "%s",\n'%trans_id)
                graph_net_file.write('                    "Type": "%s"\n'%trans_type)
                graph_net_file.write('                },\n')
                graph_net_file.write('                "position":{\n')
                graph_net_file.write('                    "x": %d,\n'%x_coord)
                graph_net_file.write('                    "y": %d\n'%y_coord)
                graph_net_file.write('                },\n')
                graph_net_file.write('                "selected": false\n')
                graph_net_file.write('            },\n') 
        graph_net_file.write('        ],\n') 
        
        #Constructing Edge Nodes
        graph_net_file.write('        "edges":[\n')
        edge_counter = 0
        for edge in edges:
            edge_id = "e"+str(edge)
            edge_coord = edges[edge]
            source = edge_coord[0]
            target = edge_coord[1]
            #Last ']' cannot be followed by a ','
            if edge_counter == len(edges)-1:
                graph_net_file.write('            {\n')
                graph_net_file.write('                "data":{\n')
                graph_net_file.write('                    "ID": "%s",\n'%edge_id)
                graph_net_file.write('                    "source": %s,\n'%source)
                graph_net_file.write('                    "target": "%s",\n'%target)
                graph_net_file.write('                },\n')
                graph_net_file.write('                "selected": false\n')
                graph_net_file.write('            }\n') 
                graph_net_file.write('        ]\n')  
            else:
                edge_counter+=1
                graph_net_file.write('            {\n')
                graph_net_file.write('                "data":{\n')
                graph_net_file.write('                    "ID": "%s",\n'%edge_id)
                graph_net_file.write('                    "source": %s,\n'%source)
                graph_net_file.write('                    "target": "%s",\n'%target)
                graph_net_file.write('                },\n')
                graph_net_file.write('                "selected": false\n')
                graph_net_file.write('            },\n')    
        
        #Closing Braces         
        graph_net_file.write('    }\n')     
        graph_net_file.write('}')
