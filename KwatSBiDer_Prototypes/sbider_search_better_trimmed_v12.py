
# coding: utf-8

# In[1]:

import itertools as it
import matplotlib.pyplot as plt
import networkx as nx
import weakref


# In[2]:

class node(object):
    def __init__(self, value):
        self.value = value
        ###print "node.__init__(self, value): self, value:", value, type(value)
        self.children = []
        self.parent = None
    
    def __repr__(self, level=0):
        ret = "\t"*level+repr(self.value)+"\n"
        for child in self.children:
            ret += child.__repr__(level+1)
        return ret
    
    def append_child(self, obj):
        ###print "append_child: obj: \t", obj, type(obj)
        children_values = []
        for child in self.children:
            children_values.append(child.value)
        obj_value = obj.value
        if obj_value not in children_values:
            self.children.append(obj)
            if type(obj) == node:
                ###print "append_child: obj is an instance of node"
                obj.parent = self
            ###else:
                ###print "append_child: obj", obj, "is NOT an instance of node"
    
    def get_all_leaf(self):
        leaf_list = []
        ###print "get_all_leaf: self.children:", self.children, len(self.children)
        if len(self.children) > 0:
            for child_node in self.children:                
                leaf_list.extend(child_node.get_all_leaf())
            ###print "get_all_leaf: returning leaf_list: before merge \t", leaf_list
            leaf_list = uniquely_merge_multi_dimentional_list_of_lists(leaf_list)
            ###print "get_all_leaf: returning leaf_list: after merge \t", leaf_list
            ###print "@get_all_leaf: returning leaf_list: \t", leaf_list, type(leaf_list)
            return leaf_list
        ###print "@get_all_leaf: no children so returning self: \t", self, type(self)
        return [self]
    
    def get_path_from_all_leaf(self):
        print "*get_path_from_all_leaf: self", self
        path_list = []
        leaf_list = self.get_all_leaf()
        print "**get_path_from_all_leaf: leaf_list \n", leaf_list, len(leaf_list)
        
        if len(leaf_list) == 1 and self in leaf_list:
            path_list.append([self.value])
            return path_list
    
        elif len(leaf_list) > 0:
            for leaf in leaf_list:
                path = []
                print "***get_path_from_all_leaf: a leaf in leaf_list:", leaf, type(leaf)
                path.append(leaf.value)
                pointer_node = leaf
                while pointer_node.parent != self:
                    path.append(pointer_node.parent.value)
                    pointer_node = pointer_node.parent
                path.append(self.value)
                path_list.append(path)
            return path_list
        else:
            return []


# In[3]:

def remove_duplicates_within_list(seq):
    seen = set()
    seen_add = seen.add
    return [ x for x in seq if not (x in seen or seen_add(x))]


# In[4]:

def list_is_type(lst, typ):
    """
    Check if all elements in a list is the same specified type.
    """
    
    if type(lst) != list:
        raise TypeError("list_is_type(lst, typ): lst is not a list")
    elif len(lst) <= 0:
        raise ValueError("list_is_type(lst, typ): lst is empty")
    return all(isinstance(x,typ) for x in lst)


# In[5]:

def remove_duplicated_lists_within_a_list_of_lists(list_of_lists):
    """
    Removes any duplicated lists, which contain same elements in same order, within a list of lists.
    """
    
    if type(list_of_lists) == list and len(list_of_lists) > 0 and list_is_type(list_of_lists, list) == True:
        list_of_lists.sort()
        trimmed = list(list_of_lists for list_of_lists,_ in it.groupby(list_of_lists))
        return trimmed
    else:
        raise TypeError("remove_duplicated_lists_within_a_list_of_lists(list_of_lists): list_of_lists should be in the form: [[],[],... ]")


# In[6]:

def uniquely_merge_list_of_lists(list_of_lists):
    """
    Merge unique elements from lists within a list.
    
    Argument:
        list_of_lists - a list that contains multiple lists.
    
    Return:
        a new list that contains unique elements from all lists within a list of lists.
    """   
    
    if type(list_of_lists) == list and len(list_of_lists) > 0:
        
        if list_is_type(list_of_lists, list) == True:
            remove_duplicated_lists_within_a_list_of_lists(list_of_lists)
            merged_list = list(list_of_lists[0])
            for a_list in list_of_lists[1::]:
                    for e in a_list:
                        if e not in merged_list:
                            merged_list.append(e)
            return merged_list
        else:
            return list(list_of_lists)
    else:
        return list_of_lists
        raise TypeError("uniquely_merge_list_of_lists(list_of_lists): list_of_list must be a non-empty list")


# In[7]:

def uniquely_merge_multi_dimentional_list_of_lists(multi_dimentional_list_of_lists):
    final_merged_list = uniquely_merge_list_of_lists(multi_dimentional_list_of_lists)
    if type(final_merged_list) == list and len(final_merged_list) > 0 and list_is_type(final_merged_list, list) == True:
        return uniquely_merge_multi_dimentional_list_of_lists(final_merged_list)
    else:
        return final_merged_list


# In[8]:

def elements_match(list_of_lists, lst):
    return set(lst).issubset(uniquely_merge_multi_dimentional_list_of_lists(list_of_lists))


# In[9]:

def get_matching_list(list_of_lists, lst):
    """
    Get any list that match a specified list.
    """
    
    if type(lst) != list:
        raise TypeError("get_matching_list(list_of_lists, lst): lst is not a list object")    
    elif type(list_of_lists) == list and len(list_of_lists) > 0 and list_is_type(list_of_lists, list) == True:
        matching_list = []
        for a_list in list_of_lists:
            if all([x in lst for x in a_list]) == True:
                matching_list.append(a_list)
        return matching_list
    else:
        raise TypeError("get_matching_list(list_of_lists, lst): list_of_lists should be in the form: [[],[],... ]")


# In[10]:

def match_any_list(list_of_lists, lst):
    """
    Check if a list matches any of lists within a list.
    """
            
    if get_matching_list(list_of_lists, lst) == []:
        return False
    else:
        return True


# In[11]:

def reverse_index(sequence, element):
    """
    Find the last index of an element in a sequence.
    """

    for i, e in enumerate(reversed(sequence)):
        if element == e:
            return len(sequence) - 1 - i
    else:
        raise ValueError("r_index(sequence, element): element not in the sequence")


# In[12]:

def remove_parentheses(sequence):
    """
    remove the outer most parentheses '()' 
    and returns the token afte the ')'
    """

    ###print "remove_parentheses(sequence): sequence:", sequence
    
    first_opener_idx_assigned = False
    started = False
    counter = 0
    
    for idx, e in enumerate(sequence):
        
        ###print "remove_parentheses(sequence): idx, e:", idx, e
        
        if e == '(':
            if started == False:
                started = True
            counter = counter + 1
        elif e == ')':
            if started == False:
                raise ValueError("remove_parentheses(sequence):                                 ')' without '('")
            counter = counter - 1
        if started == True:
            if first_opener_idx_assigned == False:
                first_opener_idx = idx
                first_opener_idx_assigned = True
            if counter == 0:
                sequence.pop(idx)
                if idx < len(sequence):
                    element_after_last_closer = sequence[idx]
                else:
                    element_after_last_closer = None
                sequence.pop(first_opener_idx)
                return element_after_last_closer
    else:
        raise ValueError("remove_parentheses(sequence):                         sequence is empty")


# In[13]:

def split_by(sequence, element):
    """
    Split a sequence by a given element and store elements
    before and after the element into a dictionary
    """
    
    element_index = sequence.index(element)
    
    sequence_before_element = sequence[:element_index:1]
    sequence_after_element = sequence[element_index + 1::1]
    
    return {0: sequence_before_element, 1: sequence_after_element}


# In[50]:

def grammar_0(cursor, tokens):
    '''grammar_0:= grammar_1 > grammar_1'''

    ###print "grammar_0(tokens): tokens:",tokens
    
    if '>' not in tokens:
        raise ValueError("grammar_0(tokens): no output")
        
    else:
        input_output_dictionary = split_by(tokens, '>')
        
    return grammar_output(grammar_1(cursor, input_output_dictionary[0]), grammar_1(cursor, input_output_dictionary[1]))


# In[51]:

def grammar_1(cursor, tokens):
    '''grammar_1:= grammar_2 or grammar_1 | grammar_2 and grammar_1 | grammar_2'''

    ###print "grammar_1(tokens): tokens:",tokens
    
    if len(tokens) > 1 and tokens[1] == 'or':
        # grammar_2 or grammar_1
        
        ###print "grammar_1(tokens): detected 'or'"
        
        # splits tokens by the first occuring 'or' and stores the tokens before and after the 'or' in a dictionary
        or_dictionary = split_by(tokens, 'or')
        return grammar_or(grammar_2(cursor, or_dictionary.get(0)), grammar_1(cursor, or_dictionary.get(1)))
    
    elif len(tokens) > 1 and tokens[1] == 'and':
        # grammar_2 and grammar_1
        
        ###print "grammar_1(tokens): detected 'and'"
        
        # splits tokens by the first occuring 'and' and stores the tokens before and after the 'and' in a dictionary
        and_dictionary = split_by(tokens, 'and')
        return grammar_and(grammar_2(cursor, and_dictionary.get(0)), grammar_1(cursor, and_dictionary.get(1)))            
    
    else:
        # grammar_2
        
        # delegates to grammar_2
        return grammar_2(cursor, tokens)


# In[52]:

def grammar_2(cursor, tokens):
    '''grammar_2:= (grammar_1) or grammar_1 | (grammar_1) and grammar_1 | (grammar_1) | interactor''' 

    ###print "grammar_2(tokens): tokens:",tokens
    
    if len(tokens) <= 0:
        raise ValueError("Invalid Syntax")
        
    elif tokens[0] == "(":
        # (grammar_1) or grammar_1 | (grammar_1) and grammar_1| (grammar_1)
        
        ###print "grammar_2(tokens): detected '('"
        
        # token after the last occuring ')'
        token_after_last_closer = remove_parentheses(tokens)
        
        if token_after_last_closer == 'or':    
            # splits tokens by the first occuring 'or' and stores the tokens before and after the 'or' in a dictionary
            
            or_dictionary = split_by(tokens, 'or')
            return grammar_or(grammar_1(cursor, or_dictionary.get(0)), grammar_1(cursor, or_dictionary.get(1)))
        
        elif token_after_last_closer == 'and':
            # splits tokens by the first occuring 'and' and stores the tokens before and after the 'and' in a dictionary
            
            and_dictionary = split_by(tokens, 'and')
            return grammar_and(grammar_1(and_dictionary.get(0)), grammar_1(and_dictionary.get(1)))
        
        else:
            # delegates to interactor
            return grammar_1(cursor, tokens)
        
    else:
        # interactor
        
        # delegates to interactor
        return interactor(cursor, tokens)


# In[53]:

def interactor(cursor, token):
    '''species'''
    
    ###print "interactor(token): token:", token    

    species = token[0]
    
    ###print "interactor(token): species:", species
    ###print "interactor(token): species id:", db_get_species_id_from_name(cursor, species)
    return [[db_get_species_id_from_name(cursor, species)]]


# In[54]:

def grammar_output(tokens1, tokens2):                                                                      
    """Grammar for '>'.                                                                              
    
    Argument(s):
        tokens1 - desctiption                                                                              
        tokens2 - desctiption                                                                              
        
        
    Return:                                                                                                
        return description                                                                                 
    """                                                                                                    
    
    grammar_output_dict = {}                                                                               
    
    ###print "grammar_output(tokens1, tokens2): tokens1 - tokens2:", tokens1, " - ", tokens2
    ###print "grammar_output(tokens1, tokens2): tokens1 - tokens2:", type(tokens1), " - ", type(tokens2)
    for token1 in tokens1:
        grammar_output_dict[tuple(token1)] = tuple(tokens2)                                                      
        
    return grammar_output_dict


# In[55]:

def grammar_or(tokens1, tokens2):
    '''or'''
    
    ###print "grammar_or(tokens1, tokens2): tokens1 - tokens2:", tokens1, " - ", tokens2
    
    return tokens1 + tokens2


# In[56]:

def grammar_and(tokens1, tokens2):
    '''and'''

    grammar_and_output = []
    
    ###print "grammar_and(tokens1, tokens2): tokens1 - tokens2:", tokens1, " - ", tokens2
    
    for token1 in tokens1:
        for token2 in tokens2:
            print [token1,token2]
            grammar_and_output.append( uniquely_merge_list_of_lists( [token1,token2] ))
    
    ###print "grammar_and(tokens1, tokens2): grammar_and_output:", grammar_and_output
    
    return grammar_and_output


# In[57]:

def parse_logic(cursor, logic_input):
    '''parse a logic input into atomized and equivalent logics'''
    
    ###print "parse_logic(logic_input): logic_input:", logic_input
    
    split_logic_input = logic_input.split()
        
    ###print "parse_logic(logic_input): split_logic_input:", split_logic_input
    
    # begins recursive logic parse
    return grammar_0(cursor, split_logic_input)


# In[58]:

def draw_plot(G):
    """
    draw and plot a graph
    
    @param - graph: graph to be drawn and plotted
    @param - start: list of input species
    @param - end: list of output species
    """
    nx.draw(G,
            node_size=400,
            node_color='#A0CBE2',
            font_size=10,
            font_color='blue',
            width=1,
            edge_color='blue',
            style='dotted',
            arrows=False)
    
    '''
    ###print "start_list:",start_list
    
    # position is stored as node attribute data for random_geometric_graph
    pos=nx.spring_layout(G)
        
    ###print "pos:",pos
    
    # list of nodes
    operon_path = pos.keys()
    
    labels = {}
    for operon in operon_path:
        labels[operon] = str(operon)
    
    ###print "operon_path:",operon_path
    
    if len(start_list) > 0:
        ncenter = start_list[0]
    else:
        ncenter = pos.keys()[len(pos.keys()) - 1]
    
    # color by path length from node near center
    dis=nx.single_source_shortest_path_length(G,ncenter)
    
    print "dis:", dis
    
    plt.figure(figsize=(10,10))
    
    nx.draw_networkx_edges(G,pos,nodelist=[ncenter],alpha=0.4)
    nx.draw_networkx_nodes(G,pos,nodelist=dis.keys(),
                           node_size=800,
                           node_color=dis.values(),
                           cmap=plt.cm.Reds_r)
    nx.draw_networkx_labels(G,pos,labels,font_size=16)

    
    plt.xlim(-0.05,1.05)
    plt.ylim(-0.05,1.05)
    plt.axis('off')
    '''
    
    plt.show()
    
    #plt.savefig() #.png


# In[59]:

def expand_graph(graph, path_list):
    '''expand networkx graph
    
    @param - graph: graph to be extended
    @param - path_list: list representation of path'''
    
    graph.add_path(path_list)


# In[60]:

def make_graph_from_path_list(path_list):
    '''make networkx graph
    
    @param - path_list: list representation of path
    @return - networkx directed graph'''
    
    graph = nx.DiGraph()
    
    if len(path_list) < 2:
        graph.add_nodes_from(path_list)
    else:
        graph.add_path(path_list)
        
    return graph


# In[61]:

def make_graph_from_path_dictionaries(in_path_dic_in, out_path_dic):
    '''make networkx graph
    
    @param - in_path_dic_in: dictionary representation of input path
    @param - out_path_dic: dictionary representation of output path
    @return - networkx directed graph'''
    
    graph = nx.DiGraph()
            
    for plasmid, input_species_list in in_path_dic_in.items():
        for species in input_species_list:
            graph.add_edge(species, plasmid)
    
    for plasmid, output_species_list in out_path_dic.items():
        for species in output_species_list:
                graph.add_edge(plasmid, species)
                
    return graph


# In[62]:

def search_sbider_path_memory(input_dictionary, activated_paths, from_operon):
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "~IN search_sbider_path_memory~"
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print
    print
    
    print "search_sbider_path_memory: activated_paths:", activated_paths
    print
    
    activated_ope_dic = {}
    activated_spe_dic = {}
    
    for path_idx, ope_spe_path in enumerate(activated_paths):
        activated_ope_dic[path_idx] = ope_spe_path[0] # ope
        activated_spe_dic[path_idx] = ope_spe_path[1] # spe
    
    
    print "search_sbider_path_memory: from_operon:", from_operon, type(from_operon)
    final_operon_requirement = input_dictionary[from_operon]
    
    activating_ope_list = []
    
    for path_idx, spe_produced in activated_spe_dic.items():
        for a_spe_produced in spe_produced:
            for and_spe_required in final_operon_requirement:
                if a_spe_produced in and_spe_required:
                    activating_ope_list.extend(activated_ope_dic.get(path_idx))
    
    print "search_sbider_path_memory: activating_ope_list:", activating_ope_list
    return activating_ope_list


# In[63]:

def build_sbider_path_memory_tree(input_dictionary, activated_paths, start_operon):
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "~IN build_sbider_path_memory_tree~"
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print
    print
    
    print "build_sbider_path_memory_tree: activated_paths:", activated_paths
    print
    
    root_ope = node(start_operon)

    temp_queue_ope = []
    temp_queue_ope.append(root_ope)
    
    temp_memory = []
        
    while len(activated_paths) > 0 and len(temp_queue_ope) > 0:
        print "\t build_sbider_path_memory_tree: activated_paths in while loop:", activated_paths
        print "\t build_sbider_path_memory_tree: temp_queue_ope:", temp_queue_ope
        
        from_node = temp_queue_ope.pop(0)
        from_operon = from_node.value

        print "\t build_sbider_path_memory_tree: ENTERING--- search_sbider_path_memory"
        children_operon = search_sbider_path_memory(input_dictionary, activated_paths, from_operon)
        print "\t build_sbider_path_memory_tree: ---RETURNING search_sbider_path_memory"
        print
        
        if len(children_operon) > 0:
            for child_operon in children_operon:
                if child_operon not in temp_memory:
                    child_node = node(child_operon)
                    from_node.append_child(child_node)
                    temp_queue_ope.append(child_node)
                    temp_memory.append(child_operon)
                    print "\t\t build_sbider_path_memory_tree: root_ope UPDATED \n", root_ope
                    print "*" * 99

            print "build_sbider_path_memory_tree: path from all ope leaf \n", root_ope.get_path_from_all_leaf()
            print
    
    return root_ope.get_path_from_all_leaf()


# In[64]:

def build_indirect_sbider_path(input_dictionary,
                               output_dictionary,
                               input_species_list,
                               output_species_list,
                               path_queue,
                               final_operon_path_list,
                               
                               memory_operon,
                               memory_species,
                               
                               activated_paths):
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "~IN build_indirect_sbider_path~"
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print
    print
    
    print "build_indirect_sbider_path: path_queue:", path_queue, len(path_queue)
    print "build_indirect_sbider_path: memory_operon:", memory_operon 
    print "build_indirect_sbider_path: memory_species:", memory_species
    print "build_indirect_sbider_path: activated_paths:", activated_paths
    print
    print "\t build_indirect_sbider_path: operons yet to be visited:", set(input_dictionary.keys()) - set(memory_operon)
    temp_memory_species = []
    for an_operon in set(input_dictionary.keys()) - set(memory_operon):
        print "\t\t build_indirect_sbider_path: OPERON:", an_operon
        activation_requirement = input_dictionary[an_operon]
        print "\t\t build_indirect_sbider_path: Avtivation Requirement:", activation_requirement
        if match_any_list(activation_requirement, memory_species) == True:
            print "\t\t\t build_indirect_sbider_path: Avtivation!!! of", an_operon
            just_produced_species = output_dictionary[an_operon]
            just_produced_unique_species = uniquely_merge_multi_dimentional_list_of_lists(just_produced_species)            
            
            if match_any_list(just_produced_species, output_species_list):
                print "\t\t\t build_indirect_sbider_path: Match!!!!!!!!!"
                matched_input_requirement = get_matching_list(activation_requirement, memory_species)
                matched_unique_input_requirement = uniquely_merge_multi_dimentional_list_of_lists(matched_input_requirement)
                if len(activated_paths) > 1:
                    print "\t\t\t build_indirect_sbider_path: ENTERING--- build_sbider_path_memory_tree"
                    ope_path_backward = build_sbider_path_memory_tree(input_dictionary,
                                                                                     activated_paths,
                                                                                     an_operon,
                                                                                     )
                    print "\t\t\t build_indirect_sbider_path: ---RETURNING build_sbider_path_memory_tree"
                    print
                
                    print "\t\t\t\t build_direct_sbider_path: BEFORE ope:", final_operon_path_list
                    final_operon_path_list.extend(ope_path_backward)
                    print "\t\t\t\t build_direct_sbider_path: AFTER ope:", final_operon_path_list
            else:
                if an_operon not in memory_operon:

                    path_queue.append(([an_operon],just_produced_unique_species))
                    
                    memory_operon.append(an_operon)
                    memory_operon = remove_duplicates_within_list(memory_operon)
                    
                    temp_memory_species.extend(just_produced_unique_species)
                    
                    activated_paths.append([[an_operon],just_produced_unique_species])
            print  
    memory_species.extend(temp_memory_species)
    memory_species = remove_duplicates_within_list(memory_species)
    print

    # if there is activated operon, run sbider_path again.
    if len(path_queue) > 0:
        print "build_indirect_sbider_path: ReENTERING--- build_direct_sbider_path"
        build_direct_sbider_path(input_dictionary,
                                 output_dictionary,
                                 input_species_list,
                                 output_species_list,
                                 path_queue,
                                 final_operon_path_list,
                                 memory_operon,
                                 memory_species,
                                 activated_paths)


# In[65]:

def build_direct_sbider_path(input_dictionary,
                             output_dictionary,
                             input_species_list,
                             output_species_list,
                             path_queue,
                             final_operon_path_list,
                             memory_operon,
                             memory_species,
                             activated_paths,
                             indirect_flag):
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "~IN build_direct_sbider_path~"
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print
    print
    
    print "build_direct_sbider_path: path_queue:", path_queue, len(path_queue)
    print "build_direct_sbider_path: memory_operon:", memory_operon 
    print "build_direct_sbider_path: memory_species:", memory_species
    print "build_direct_sbider_path: activated_paths:", activated_paths
    print
    
    while len(path_queue) != 0:
        print "\t build_direct_sbider_path: path_queue in while-loop:", path_queue, len(path_queue)
        
        (previously_visited_operon_list, just_previously_produced_species_list) = path_queue.pop(0)
        
        print "\t build_direct_sbider_path: operons to be visited:", set(input_dictionary.keys()) - set(uniquely_merge_multi_dimentional_list_of_lists(previously_visited_operon_list))
        for an_operon in set(input_dictionary.keys()) - set(uniquely_merge_multi_dimentional_list_of_lists(previously_visited_operon_list)):
            print "\t\t build_direct_sbider_path: OPERON:", an_operon
            
            if an_operon not in memory_operon:
                activation_requirement = input_dictionary[an_operon]
                print "\t\t build_direct_sbider_path: Avtivation Requirement:", activation_requirement

                if match_any_list(activation_requirement, just_previously_produced_species_list) == True:
                    print "\t\t\t build_direct_sbider_path: Activation!!! of", an_operon

                    visited_operon_list = previously_visited_operon_list + [an_operon]

                    just_produced_species = output_dictionary[an_operon]
                    just_produced_unique_species = uniquely_merge_multi_dimentional_list_of_lists(just_produced_species)

                    if match_any_list(just_produced_species, output_species_list):
                        print "\t\t\t\t build_direct_sbider_path: Match!!!!!!!!!"
                        
                        if indirect_flag == False:
                            print "\t\t\t\t build_direct_sbider_path: BEFORE ope:", final_operon_path_list
                            final_operon_path_list.append(visited_operon_list)
                            print "\t\t\t\t build_direct_sbider_path: AFTER ope:", final_operon_path_list
                    else:
                        path_queue.append((visited_operon_list,just_produced_unique_species))
                        memory_operon.append(an_operon)
                        memory_operon = remove_duplicates_within_list(memory_operon)                        
                        memory_species.extend(just_produced_unique_species)
                        memory_species = remove_duplicates_within_list(memory_species)

                    activated_paths.append([[an_operon],just_produced_unique_species])                        
                   
        print "\t build_direct_sbider_path: exiting while loop for queue"
        print
    
    if indirect_flag == True:
        print "build_direct_sbider_path: ENTERING--- build_indirect_sbider_path"
        final_operon_path_list = build_indirect_sbider_path(input_dictionary,
                                   output_dictionary,
                                   input_species_list,
                                   output_species_list,
                                   path_queue,
                                   final_operon_path_list,
                                   memory_operon,
                                   memory_species,
                                   activated_paths)
        print "build_direct_sbider_path: ---RETURNING build_indirect_sbider_path"
        print
        
    return final_operon_path_list


# In[66]:

def get_sbider_path(inp_dic,
                    outp_dic,
                    inp_spe,
                    outp_spe,
                    indirect_flag=False):
    print "~~~~~~~~~~~~~~~~~~~~"
    print "~IN get_sbider_path~"
    print "~~~~~~~~~~~~~~~~~~~~"
    print
    print
    
    final_ope_path = []
    
    path_queue = [([],inp_spe)]
    
    memory_ope = []
    memory_spe = []
    memory_spe.extend(inp_spe)
    
    activated_paths = []
    
    print "get_sbider_path: ENTERING--- build_direct_sbider_path"
    build_direct_sbider_path(inp_dic,
                             outp_dic,
                             inp_spe,
                             outp_spe,
                             path_queue,
                             final_ope_path,
                             memory_ope,
                             memory_spe,
                             activated_paths,
                             indirect_flag)
    print "get_sbider_path: ---RETURNING build_direct_sbider_path"
    print
    
    print "get_sbider_path: final_ope_path: BEFORE", final_ope_path
    if len(final_ope_path) > 0:
        final_ope_path = remove_duplicated_lists_within_a_list_of_lists(final_ope_path)
    print "get_sbider_path: final_ope_path: AFTER", final_ope_path
    
    return final_ope_path, inp_spe





# In[68]:

def main(cur, user_input):
    logic_dictionary = parse_logic(cur, user_input)

    print "\nlogic_dictionary:", logic_dictionary

    for input_species, output_species_list in logic_dictionary.items():

        for output_species in output_species_list:

            print "Path:",input_species,"--->",output_species,"="

            operon_path_list = get_sbider_path(input_path_dictionary,
                                                                  output_path_dictionary,
                                                                  list(input_species),
                                                                  output_species,
                                                                  False)
            
    return operon_path_list, list(input_species)
