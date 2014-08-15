'''
//Script Details:
    >Petri Net inspired visualization 
    >JSON graph convertion
    >Dot file generation 

Disclaimer: Network fails to capture Transcription factors or "implict" outputs 

Disclaimer: Transitions not representative of Boolean Logic. However the Boolean Logic
            	   of most devices was kept in mind when creating (transition,I/O) edges.
            	    Input Transitions: Boolean Logic was considered
            	    Output Transitions: Drives Genetic Expression of Primary Output thus 
            	    there was no Boolean Logic to consider  


***************************

@author: Fernando Contreras
@email: f2contre@gmail.com
@project: iGEM_Software_Design

***************************

//Modules and Import Purpose:
    >NetworkX:
        'Python language software package for the creation, manipulation, and 
        study of the structure, dynamics, and functions of complex networks.'
        
        Purpose: Intermediate step used to convert Pydot graph to Networkx graph 
        and subsequently to a JSON graph and Dot file
    
    >Pydot: 
        Python's Graphviz interface, graph visualization software
        
        Purpose: Construct network using CSV file as input 
    
    >JSON:
        Encodes Python objects as JSON strings,and decode JSON strings into 
        Python objects
        
        Purpose: Convert and serialize Python objects 

'''

import pydot
import networkx as nx
from networkx.readwrite import json_graph
import json 

with open('C:\Users\Fernando\Desktop\GRAPH_NETWORK.txt','r') as network_file:
    #'with' after statement is executed, the file is ALWAYS closed, even if an error is encountered
    graph=pydot.Dot('iGEM_Devices_&_Intermediates_Network',rankdir='LR', graph_type='digraph')
    #Dictionaries prevent unwanted (transition,output/input) edges from being duplicated
    devices={}
    single_source_input={}
    multi_source_input={}
    output_intermediates={}
    #counter used to assign new transitions 
    counter=0
    edges=network_file.readlines()
    for edge in edges:
        #parsing edges with ',' as the delimiter 
        network_list=edge.split(',')
        #device not in corresponding dict. indicates that we're working 
        #with (input,transition) and (transition,device) edges
        if network_list[0] not in devices:
            input_list=network_list
            #edge length indicates device input
            #len=2:one input, len>2: multiple inputs 
            if len(input_list)==2:
                intermediate=input_list[0]
                #removing '\n' from string 
                device=input_list[1].rstrip('\n')
                #checking for duplicate (intermediates,transition) edges
                if intermediate not in single_source_input:
                    #new intermediate=new transition,memoizing edge 
                    single_source_input[intermediate]='t%d'%counter
                    devices[device]='seen' 
                    in_trans_edge=pydot.Edge(intermediate,'t%d'%counter)
                    device_trans_edge=pydot.Edge('t%d'%counter,device)
                    counter+=1
                    graph.add_edge(in_trans_edge)
                    graph.add_edge(device_trans_edge)
                #(input,transition) edge exists 
                else:
                    devices[device]='seen'
                    device_trans_edge=pydot.Edge(single_source_input[intermediate],device)
                    graph.add_edge(device_trans_edge)
            #multiple inputs
            if len(input_list)>2: 
                intermediates=input_list[0:len(input_list)-1]#list of intermediates 
                device=input_list[len(input_list)-1].rstrip('\n')
                #checking for different combinations(order doesn't matter) Lara+aTc=aTc+Lara
                input_combination=''
                input_inv_combination=''
                for intermediate in intermediates:
                    input_combination=input_combination+intermediate
                    input_inverted_combination=intermediate+input_inv_combination
                #checking for duplicate combinations 
                if input_combination not in multi_source_input:
                    #new combination = new transition,memoizing new combination  
                    multi_source_input[input_combination]='t%d'%counter
                    multi_source_input[input_inverted_combination]='t%d'%counter
                    for intermediate in intermediates:
                        in_trans_edge=pydot.Edge(intermediate,'t%d'%counter)
                        graph.add_edge(in_trans_edge)
                    device_trans_edge=pydot.Edge('t%d'%counter,device)
                    devices[device]='seen'
                    counter+=1
                    graph.add_edge(device_trans_edge)
                #combination exists
                else:
                    devices[device]='seen'
                    device_trans_edge=pydot.Edge(multi_source_input[input_combination],device)
                    graph.add_edge(device_trans_edge)
        #working with (device,transition) and (transition,output) edges
        else:
            #network construction technique same as input,device,trans construct  
            output_list=network_list
            if len(output_list)==2: 
                intermediate=output_list[1].rstrip('\n')
                device=output_list[0]
                if intermediate not in output_intermediates:
                    output_intermediates[intermediate]='t%d'%counter
                    out_trans_edge=pydot.Edge('t%d'%counter,intermediate)
                    graph.add_edge(out_trans_edge)
                    device_trans_edge=pydot.Edge(device,'t%d'%counter)
                    graph.add_edge(device_trans_edge)
                    counter+=1
                else:
                    device_trans_edge=pydot.Edge(device,output_intermediates[intermediate])
                    graph.add_edge(device_trans_edge)
            if len(output_list)>2:
                intermediates=output_list[1:len(output_list)]
                intermediates[len(intermediates)-1]=intermediates[len(intermediates)-1].rstrip('\n')
                device=output_list[0]
                for intermediate in intermediates:
                    if intermediate not in output_intermediates:
                        output_intermediates[intermediate]='t%d'%counter
                        out_trans_edge=pydot.Edge('t%d'%counter,intermediate)
                        graph.add_edge(out_trans_edge)
                        device_trans_edge=pydot.Edge(device,'t%d'%counter)
                        graph.add_edge(device_trans_edge)
                        counter+=1
                    else: 
                        device_trans_edge=pydot.Edge(device,output_intermediates[intermediate])
                        graph.add_edge(device_trans_edge)
    '''Starting the file conversion'''

    from_pydot_to_nx=nx.from_pydot(graph)
    #outputs Multigraph which is undesirable thus implement the following statement
    #which generates a directed NetworkX graph 
    DG=nx.DiGraph(from_pydot_to_nx)
    #write dot file
    nx.write_dot(DG,"C:\Users\Fernando\Desktop\GRAPH_NETWORK.dot")
    #write png image of network 
    graph.write_png("C:\Users\Fernando\Desktop\png_images\GRAPH_NETWORK_2.png")
    #NetworkX to JSON graph 
    with open("C:\Users\Fernando\Desktop\JSON_2.txt", 'w') as outfile:
        #node-link format to serialize
        data = json_graph.node_link_data(DG)
        #returning JSON string which is then written to an output text file
        json.dump(data, outfile)
