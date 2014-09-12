def generate_positions():
    import pydot 
    import networkx as nx
    with open('C:\Users\Fernando\Desktop\GRAPH_NETWORK.txt','r') as network_file:
        #'with' after statement is executed, the file is ALWAYS closed, even if an error is encountered
        graph=pydot.Dot('Relationship_Graph',rankdir='LR', graph_type='digraph')
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
                #input_list length indicates device input
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
                        trans_node = pydot.Node('t%d'%counter, shape = 'box')
                        graph.add_node(trans_node)
                        in_trans_edge=pydot.Edge(intermediate,trans_node)
                        device_trans_edge=pydot.Edge(trans_node,device)
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
                            trans_node = pydot.Node('t%d'%counter, shape = 'box')
                            graph.add_node(trans_node)
                            in_trans_edge=pydot.Edge(intermediate,trans_node)
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
        pydot_to_netx = nx.from_pydot(graph)
        digraph = nx.DiGraph(pydot_to_netx)
        node_pos=nx.graphviz_layout(digraph,prog='sfdp')
        return node_pos            
