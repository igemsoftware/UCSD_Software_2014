"""
Subtitle

Descriptive paragraph

******************************************************************************
@author: Joaquin Reyna, University of California, San Diego
         Huwate(Kwat) Yeerna, University of California, San Diego
******************************************************************************
"""

import networkx as nx

import sbider_database as db

def resize_network(total_subnetwork_nodes, total_whole_nodes = 550): 
    """Resize the network."""
    return 10000* total_subnetwork_nodes/total_whole_nodes


def get_input_transition_species_dictionary(cursor):
    """
    Retrieves all rows pertaining to the sbider inputTranstion
    table using these values the dictionary is created.

    Argument(s):
        cursor - sqlite3 cursor object instance

    Return:
        A dictionary mapping input transition id to a species id list.
    """

    input_transitions_species_dict = {}
    input_transition_species_list = db.db_select(cursor, "InputTransitionSpecies", ["it_id", "spe_id"])
    input_transition_species_list = input_transition_species_list.fetchall()
    inserted_it_ids = []
    for it_id, spe_id in input_transition_species_list:
        if it_id not in inserted_it_ids:
            input_transitions_species_dict[it_id] = [spe_id]
            inserted_it_ids.append(it_id)
        else:
            input_transitions_species_dict[it_id].append(spe_id)
    return input_transitions_species_dict


def list_of_lists(list_of_tups):
    """Creates a list of lists from a list of tuples.

    Return:
        A list with list values.

    """

    list_of_lsts = []
    for tup in list_of_tups:
        list_of_lsts.append(list(tup))
    return list_of_lsts


def list_of_tuples(list_of_lsts):
    """Creates a list of tuples from a list of lists.

    Return:
        A list with tuple values.
    """

    list_of_tups = []
    for lst in list_of_lsts:
        list_of_tups.append(tuple(lst))
    return list_of_tups


def unique_node_list(nodes_list):
    """
    Removal of duplicate nodes from the node_list.

    Argument(s):
        node_list - list of node information stored as list (list of lists).

    Return:
        A list of unique nodes.
        For example:
        [ ["node_id_1", "node_field_2", "node_field_3"], ["node_id_2", "node_field_2", "node_field_3", ...], ...]
    """

    uniq_node_list = []
    used_node_id_list = []
    for node_ in nodes_list:
        if node_ not in used_node_id_list:
            uniq_node_list.append(node_)
            used_node_id_list.append(node_)
    return uniq_node_list


def add_node_id_abbreviation(node_, abbrev, index):
    """Adds an id abbreviation to a node.

    Argument(s):
        node - list representing node information.
        abbrev - string abbreviation.
        index - integer indicating which value to abbreviate.

    Return:
        A node with the abbreviation added to the given index.
        For example: [ "abbreviation_node_id", "node_field_2", "node_field_3", ...]
    """

    node_[index] = abbrev + node_[index]
    return node_


def add_node_list_id_abbreviation(node_list, abbrev, id_index):
    """Adds an id abbreviation to a list of nodes.

    Argument(s):
        node_list - list containing nodes.
        abbrev - string abbreviation.
        index - integer indicating which value to abbreviate.

    Return:
        A node_list the abbreviation added to the given index
        of every node.
        For example: [ [ "abbreviation_node_id_1", "node_field_2", "node_field_3", ...],
                       [ "abbreviation_node_id_2", "node_field_2", "node_field_3", ...], ...]

    """

    for index, node_ in enumerate(node_list):
        node_list[index] = add_node_id_abbreviation(node_, abbrev, id_index)
    return node_list


def merge_list_of_lists(list_of_lsts):
    """merges_lists within a list."""
    condensed_list = []
    for lst in list_of_lsts:
        condensed_list.extend(lst)
    return condensed_list


def get_node_from_id(cursor, node_table_name, node_id, node_id_type):
    """Query the database using the node_id for node.

    Argument(s):
        cursor - sqlite3 cursor object
        node_table_name - table_name where node information exists
        node_id - string representation of node_id
        node_id_type - the type of node being used from the sbider database.

    Return:
        A tuple of information representing the node.

    """

    node_cursor = db.db_select(cursor, node_table_name, "*", [node_id_type], ["="], [node_id], [""])
    node_ = node_cursor.fetchone()
    node_ = list(node_)
    return node_


def get_node1_list_from_node2_id(cursor, node1_node2_relationship_table, node2_id, node2_id_type,
                                 node1_table_name, node1_id_type):
    """Query the database to find all node1's from node2's id.
        It's possible to have multiple node1's map to node2.

    Argument(s):
        cursor - sqlite3 cursor object
        node1_node2_relationship_table - table_name relating node1 and node2
        node2_id - string representation of node1_id
        node2_id_type - node2_id type being used in the sbider database
        node1_table_name - table_name where node information exists
        node1_id_type - node1_id type being used in the sbider database

    Return:
        A list of nodes representing all node1's related to node2.
 
    """

    node_id = db.db_select(cursor, node1_node2_relationship_table,
                           [node1_id_type],
                           [node2_id_type],
                           ["="],
                           ["'" + node2_id + "'"],
                           [""])

    node_id_list = node_id.fetchall()
    node_id_list = list_of_lists(node_id_list)

    node_list = []
    for node_info in node_id_list:
        node_ = get_node_from_id(cursor, node1_table_name, node_info[0], node1_id_type)
        node_ = list(node_)
        node_list.append(node_)
    return node_list


def add_edge_id_abbreviation(edge, abbrev1, abbrev2, index1=0, index2=0):
    return (abbrev1 + edge[0], abbrev2 + edge[1])


def add_edge_list_id_abbreviation(edge_list, abbrev1, abbrev2, index1=0, index2=0):
    edge_list_abbrev = []
    for edge in edge_list:
        edge_list_abbrev.append(add_edge_id_abbreviation(edge, abbrev1, abbrev2, index1, index2))
    return edge_list_abbrev


def determine_operon_activated_input_transition(cursor, starting_species_list, operon_id, input_transition_id_dict):
    """Determining which input transition is activating an operon.

    Argument(s):
        cursor - sqlite3 cursor object
        starting_species_list - a list of species activating an operon
        operon_id - sbider based operon id
        id_id_dict - dictionary mapping input transitions to corresponding species

    Return:
        A list of transitions that activate the operon (from operon_id).
        For example: ["it_1", "it_2", ...]

    """
    starting_species_set = set(tuple(starting_species_list))
    it_trans_id_list = db.db_select(cursor, "OperonInputTransition", ["it_id"], ["ope_id"], ["="],
                                    ["'" + operon_id + "'"], [""])
    it_trans_id_list = it_trans_id_list.fetchall()
    it_trans_id_list = list_of_lists(it_trans_id_list)
    it_trans_id_list = merge_list_of_lists(it_trans_id_list)

    activated_it_id_list = []
    for it_trans_id in it_trans_id_list:

        activating_species_set = set(input_transition_id_dict[it_trans_id])

        if starting_species_set.issuperset(activating_species_set):
            activated_it_id_list.append(it_trans_id)
    return activated_it_id_list


def create_operon_node(cursor, operon_id):
    """Create an operon node from the corresponding operon_id.

    Argument(s):
        cursor - sqlite 3 cursor object.
        operon_id - sbider based operon id

    Return:
        A tuple with operon node information as a tuple
        (id abbrevation included) and the corresponding
        operon id.
        For example: ( ("ope_1-1", "pLux-->gfp", "sbol_image_path_1"), "1-1" )

    """

    operon_node = get_node_from_id(cursor, "Operon", "'" + operon_id + "'", "ope_id")

    operon_node_abbrev = add_node_id_abbreviation(operon_node, "ope_", 0)

    return operon_node_abbrev, operon_id


def create_input_transition_nodes(cursor, starting_species_list, operon_id, input_transition_id_dict):
    """Create input transition nodes list from the corresponding operon_id.

    Argument(s):
        cursor - sqlite3 cursor object
        starting_species_list - a list of species activating an operon
        operon_id - sbider based operon id
        input_transition_id_dict - dictionary mapping input transitions to corresponding species

    Return:
        A tuple of input transition nodes list (with abbreviation) and
        input transition id list.
        For example:
        ( [ ("ope_1-1", "pLux-->gfp", "sbol_image_path_1"), ("ope_2-1", "pLambda-->gfp", "sbol_image_path_2"), ... ],
          ["1-1", "2-1", ...] )

    """

    activated_it_ids = determine_operon_activated_input_transition(cursor, starting_species_list, operon_id,
                                                                   input_transition_id_dict)

    it_node_abbrev_list = []
    activated_it_id_list = []
    for activated_it_id in activated_it_ids:
        it_node = db.db_select(cursor, "InputTransition", "*", ["it_id"], ["="], [activated_it_id], [""])
        it_node = list(it_node.fetchone())
        it_node_abbrev = add_node_id_abbreviation(it_node, "it_", 0)
        it_node_abbrev_list.append(it_node_abbrev)
        activated_it_id_list.append(activated_it_id)

    return it_node_abbrev_list, activated_it_id_list


def create_output_transition_node(cursor, operon_id):
    """Create output transition nodes from the corresponding operon_id.

    Argument(s):
        cursor - sqlite3 cursor object
        operon_id - sbider based operon id

    Return:
        A list of tuples with operon node information.

    """
    ot_node = get_node1_list_from_node2_id(cursor, "OperonOutputTransition", operon_id, "ope_id",
                                           "OutputTransition", "ot_id")[0]
    ot_id = ot_node[0]

    ot_node_abbrev = add_node_id_abbreviation(ot_node, "ot_", 0)

    return ot_node_abbrev, ot_id


def create_input_species_nodes(cursor, it_id):
    """Create species nodes from the corresponding it_id."""

    it_species_nodes = get_node1_list_from_node2_id(cursor, "InputTransitionSpecies", it_id, "it_id",
                                                    "Species", "spe_id")
    it_species_nodes = it_species_nodes

    it_species_ids = [spe_id[0] for spe_id in it_species_nodes]
    it_species_nodes_abbrev = [add_node_id_abbreviation(spe_node, "spe_", 0) for spe_node in it_species_nodes]
    it_species_nodes_abbrev = [tuple(tup) for tup in it_species_nodes_abbrev]

    return it_species_nodes_abbrev, it_species_ids


def create_output_species_nodes(cursor, ot_id):
    """Create species nodes from the corresponding ot_id."""

    ot_species_nodes = get_node1_list_from_node2_id(cursor, "OutputTransitionSpecies", ot_id, "ot_id",
                                                    "Species", "spe_id")

    ot_species_nodes = ot_species_nodes

    ot_species_ids = [spe_id[0] for spe_id in ot_species_nodes]
    ot_species_nodes_abbrev = [add_node_id_abbreviation(spe_node, "spe_", 0) for spe_node in ot_species_nodes]
    ot_species_nodes_abbrev = [tuple(tup) for tup in ot_species_nodes_abbrev]

    return ot_species_nodes_abbrev, ot_species_ids


def nx_node_coordinates_dictionary(node_id_list, edge_list):
    """Creates a dictionary of node coordinates using spring layout from networkx.

    Argument(s):
        node_id_list - ids of nodes for positioning
        edge_list - all edges between nodes stored in a tuple as follows,
                    (source_node_id, target_node_id)

    Return:
        A dictionary mapping

    """

    json_graph = nx.Graph()
    add_node_values_to_nxgraph(json_graph, node_id_list)
    json_graph.add_edges_from(edge_list)
    node_coor_dictionary = nx.spring_layout(json_graph)
    return node_coor_dictionary


def add_node_values_to_nxgraph(nxgraph, node_list):
    """Extracts the node id and enters it into nxGraph."""

    for node_ in node_list:
        nxgraph.add_node(node_[0])


def get_path_json_array(cursor, starting_species_list, operon_paths_list):
    """Generate json array for node highlighting."""

    all_species_paths_ids = []
    all_it_paths_ids = []
    all_operon_paths_ids = []
    all_ot_paths_ids = []
    all_edge_paths_ids = []

    operon_input_transition_dictionary = get_input_transition_species_dictionary(cursor)

    for operon_path in operon_paths_list:
        path_species_nodes, path_it_nodes, path_operon_nodes, \
        path_ot_nodes, path_edges = \
            create_subnetwork_path(cursor, starting_species_list, operon_path, operon_input_transition_dictionary)

        path_species_ids = [spe_node[0] for spe_node in path_species_nodes]

        path_it_ids = [it_node[0] for it_node in path_it_nodes]
        path_operon_ids = [operon_node[0] for operon_node in path_operon_nodes]
        path_ot_ids = [ot_node[0] for ot_node in path_ot_nodes]
        path_edges_ids = [edge[0] + "-" + edge[1] for edge in path_edges]

        all_species_paths_ids.append(path_species_ids)
        all_it_paths_ids.append(path_it_ids)
        all_operon_paths_ids.append(path_operon_ids)
        all_ot_paths_ids.append(path_ot_ids)
        all_edge_paths_ids.append(path_edges_ids)

    species_json_array = '''"speciesId": ''' + str(all_species_paths_ids).replace("'", '"') + ","
    input_transitions_json_array = '"inputTransitionsId": ' + str(all_it_paths_ids).replace("'", '"') + ","
    operons_json_array = '"operonsId": ' + str(all_operon_paths_ids).replace("'", '"') + ","
    output_transitions_json_array = '"outputTransitionsId": ' + str(all_ot_paths_ids).replace("'", '"') + ","
    edges_json_array = '"edgesId": ' + str(all_edge_paths_ids).replace("'", '"')

    to_return = species_json_array + input_transitions_json_array + operons_json_array + \
                output_transitions_json_array + edges_json_array

    return to_return


def create_subnetwork_path(cursor, starting_species_list, operon_path, it_trans_dict):
    """
    Creating a subnetwork path.
    :rtype : object
    :param cursor:
    :param starting_species_list: 
    :param operon_path: 
    :param it_trans_dict: 
    """
    species_set = set()
    input_transition_set = set()
    operon_set = set()
    output_transition_set = set()
    edge_path_list = []
    current_species_list = starting_species_list

    for operon in range(len(operon_path)):

        operon_id = operon_path[operon]

        operon_node_abbrev, _ = create_operon_node(cursor, operon_id)

        operon_set.add(tuple(operon_node_abbrev))


        # Creating the input transition node (MULT ONES)
        it_node_abbrev_list, it_id_list = create_input_transition_nodes(cursor, current_species_list,
                                                                        operon_id, it_trans_dict)
        for it_node_abbrev, it_id in zip(it_node_abbrev_list, it_id_list):
            input_transition_set.add(tuple(it_node_abbrev))
            edge_path_list.append([it_node_abbrev[0], operon_node_abbrev[0]])

            # Creating the input species nodes and inputTransitionSpecies
            it_species_nodes_abbrev, _ = create_input_species_nodes(cursor, it_id)
            for it_species_node_abbrev in it_species_nodes_abbrev:
                species_set.add(tuple(it_species_node_abbrev))
                edge_path_list.append([it_species_node_abbrev[0], it_node_abbrev[0]])


        # Creating the output transitio nodes (ONLY ONE)
        ot_node_abbrev, ot_id = create_output_transition_node(cursor, operon_id)
        output_transition_set.add(tuple(ot_node_abbrev))
        edge_path_list.append([operon_node_abbrev[0], ot_node_abbrev[0]])
        ot_species_nodes_abbrev, ot_species_id_list = create_output_species_nodes(cursor, ot_id)

        for ot_species_node_abbrev in ot_species_nodes_abbrev:
            species_set.add(tuple(ot_species_node_abbrev))
            edge_path_list.append([ot_node_abbrev[0], ot_species_node_abbrev[0]])

        current_species_list = ot_species_id_list

    edge_path_list = list_of_tuples(edge_path_list)

    return species_set, input_transition_set, operon_set, output_transition_set, edge_path_list


def get_subnetwork(cursor, list_of_operon_paths):
    species_subnetwork_set = set()
    input_transition_subnetwork_set = set()
    operon_subnetwork_set = set()
    output_transition_subnetwork_set = set()
    source_id_target_id_set = set()

    it_id_dict = get_input_transition_species_dictionary(cursor)

    starting_species_list = list_of_operon_paths.pop(0)

    for operon_path in list_of_operon_paths:
        species_set, input_transition_set, operon_set, output_transition_set, edge_path_list = create_subnetwork_path(
            cursor, starting_species_list, operon_path, it_id_dict)

        species_subnetwork_set = species_subnetwork_set.union(species_set)
        input_transition_subnetwork_set = input_transition_subnetwork_set.union(input_transition_set)
        operon_subnetwork_set = operon_subnetwork_set.union(operon_set)
        output_transition_subnetwork_set = output_transition_subnetwork_set.union(output_transition_set)
        source_id_target_id_set = source_id_target_id_set.union(set(edge_path_list))

    species_subnetwork_list = list_of_lists(species_subnetwork_set)
    input_transition_subnetwork_list = list_of_lists(input_transition_subnetwork_set)
    operon_subnetwork_list = list_of_lists(operon_subnetwork_set)
    output_transition_subnetwork_list = list_of_lists(output_transition_subnetwork_set)
    source_id_target_id_list = list_of_lists(source_id_target_id_set)

    toreturn = get_path_json_array(cursor, starting_species_list, list(list_of_operon_paths))

    return species_subnetwork_list, input_transition_subnetwork_list, \
           operon_subnetwork_list, output_transition_subnetwork_list, \
           source_id_target_id_list, toreturn


def create_subnetwork_json_string(cursor, list_of_operon_paths):
    """Generates the subnetwork json."""

    json_info = get_subnetwork(cursor, list_of_operon_paths)

    return create_json_network_string(*json_info)


def get_whole_network(cursor):
    """Whole network data prep for json."""

    species_nodes_list = db.db_select(cursor, "Species", ["spe_id", "name", "type"])
    species_nodes_list = species_nodes_list.fetchall()
    species_nodes_list = list_of_lists(species_nodes_list)
    species_nodes_list_abbrev = add_node_list_id_abbreviation(species_nodes_list, "spe_", 0)

    input_transition_nodes_list = db.db_select(cursor, "InputTransition", ["it_id", "logic"])
    input_transition_nodes_list = input_transition_nodes_list.fetchall()
    input_transition_nodes_list = list_of_lists(input_transition_nodes_list)
    input_transition_nodes_list_abbrev = add_node_list_id_abbreviation(input_transition_nodes_list, "it_", 0)

    operon_nodes_list = db.db_select(cursor, "Operon", ["ope_id", "name"])
    operon_nodes_list = operon_nodes_list.fetchall()
    operon_nodes_list = list_of_lists(operon_nodes_list)
    operon_nodes_list_abbrev = add_node_list_id_abbreviation(operon_nodes_list, "ope_", 0)

    output_transition_nodes_list = db.db_select(cursor, "OutputTransition", ["ot_id"])
    output_transition_nodes_list = output_transition_nodes_list.fetchall()
    output_transition_nodes_list = list_of_lists(output_transition_nodes_list)
    output_transition_nodes_list_abbrev = add_node_list_id_abbreviation(output_transition_nodes_list, "ot_", 0)

    species_input_transition_edge_list = db.db_select(cursor, "InputTransitionSpecies", ["spe_id", "it_id"])
    species_input_transition_edge_list = species_input_transition_edge_list.fetchall()
    species_input_transition_edge_list = list_of_lists(species_input_transition_edge_list)
    species_input_transition_edge_list_abbrev = add_edge_list_id_abbreviation(species_input_transition_edge_list,
                                                                              "spe_", "it_")

    input_transition_operon_edge_list = db.db_select(cursor, "OperonInputTransition", ["it_id", "ope_id"])
    input_transition_operon_edge_list = input_transition_operon_edge_list.fetchall()
    input_transition_operon_edge_list = list_of_lists(input_transition_operon_edge_list)
    input_transition_operon_edge_list_abbrev = add_edge_list_id_abbreviation(input_transition_operon_edge_list,
                                                                             "it_", "ope_")

    operon_output_transition_edge_list = db.db_select(cursor, "OperonOutputTransition", ["ope_id", "ot_id"])
    operon_output_transition_edge_list = operon_output_transition_edge_list.fetchall()
    operon_output_transition_edge_list = list_of_lists(operon_output_transition_edge_list)
    operon_output_transition_edge_list_abbrev = add_edge_list_id_abbreviation(operon_output_transition_edge_list,
                                                                              "ope_", "ot_")

    output_transition_species_edge_list = db.db_select(cursor, "OutputTransitionSpecies", ["ot_id", "spe_id"])
    output_transition_species_edge_list = output_transition_species_edge_list.fetchall()
    output_transition_species_edge_list = list_of_lists(output_transition_species_edge_list)
    output_transition_species_edge_list_abbrev = add_edge_list_id_abbreviation(output_transition_species_edge_list,
                                                                               "ot_", "spe_")

    all_edges = species_input_transition_edge_list_abbrev + input_transition_operon_edge_list_abbrev + \
                operon_output_transition_edge_list_abbrev + output_transition_species_edge_list_abbrev

    return (species_nodes_list_abbrev, input_transition_nodes_list_abbrev, operon_nodes_list_abbrev,
            output_transition_nodes_list_abbrev, all_edges)


def create_network_json_file(cursor, file_name="whole_network.json"):
    """Generates the whole network json."""

    json_info = get_whole_network(cursor)

    create_json_network_file(file_name, *json_info)

	
def create_json_network_file(json_file_path, species_nodes_list, input_transitions_nodes_list,
                             operon_nodes_list, output_transitions_nodes_list, source_id_target_id_list,
                             database = "sbider.db"):
    """Writes the whole network json.
    :param json_file_path:
    :param species_nodes_list:
    :param input_transitions_nodes_list:
    :param operon_nodes_list:
    :param output_transitions_nodes_list:
    :param source_id_target_id_list:
    """

    node_list = species_nodes_list + input_transitions_nodes_list + operon_nodes_list + output_transitions_nodes_list
    node_coor_dictionary = nx_node_coordinates_dictionary(node_list, source_id_target_id_list)

    f = open(json_file_path, 'w')
    num_runs = 0

    x_coor_factor = resize_network(len(node_list), len(node_list))
    y_coor_factor = x_coor_factor

    f.write('{\n\t"data" : { ')
    f.write('\n\t"selected" : true,')
    f.write('\n\t"_Annotations": [] ,')
    f.write('\n\t"shared_name" : "Test.sif",')
    f.write('\n\t"SUID" : 52,')
    f.write('\n\t"name":"Test.sif"')
    f.write('\n\t},')
    f.write('\n\t"elements":{')
    f.write('\n\t\t"nodes":[')

    for node in species_nodes_list:
        node[2] = "None"
        species_sbml = "species_sbml_%s.txt" % node[0].replace("spe_", "")
        f.write('\n\t\t\t{')
        f.write('\n\t\t\t\t"data":{')
        f.write('\n\t\t\t\t\t"id":"' + node[0] + '",')
        f.write('\n\t\t\t\t\t"name":"' + node[1] + '",')
        f.write('\n\t\t\t\t\t"type":"' + node[2] + '",')
        f.write('\n\t\t\t\t\t"sbml":"' + species_sbml + '"')
        f.write('\n\t\t\t\t},')

        f.write('\n\t\t\t\t"position":{')
        f.write('\n\t\t\t\t\t"x":' + str(node_coor_dictionary[node[0]][0] * x_coor_factor) + ',')
        f.write('\n\t\t\t\t\t"y":' + str(node_coor_dictionary[node[0]][1] * y_coor_factor))
        f.write('\n\t\t\t\t},')
        f.write('\n\t\t\t\t"classes":"species')
        f.write('",')

        f.write('\n\t\t\t\t"selected":false')
        f.write('\n\t\t\t},')
        num_runs += 1

    num_runs = 0
    for node in input_transitions_nodes_list:
        it_sbml = "it_sbml_%s.txt" % node[0].replace("it_", "")
        f.write('\n\t\t\t{')
        f.write('\n\t\t\t\t"data":{')
        f.write('\n\t\t\t\t\t"id":"' + node[0] + '",')
        f.write('\n\t\t\t\t\t"logic":"' + node[1] + '",')
        f.write('\n\t\t\t\t\t"sbml":"' + it_sbml + '"')

        f.write('\n\t\t\t\t},')

        f.write('\n\t\t\t\t"position":{')
        f.write('\n\t\t\t\t\t"x":' + str(node_coor_dictionary[node[0]][0] * x_coor_factor) + ',')
        f.write('\n\t\t\t\t\t"y":' + str(node_coor_dictionary[node[0]][1] * y_coor_factor))
        f.write('\n\t\t\t\t},')
        f.write('\n\t\t\t\t"classes":"input transition')
        f.write('",')

        f.write('\n\t\t\t\t"selected":false')
        f.write('\n\t\t\t},')
        num_runs += 1

    operon_PMC = db.operon_PMC_dictionary(database)
    num_runs = 0

    for key in operon_PMC.keys():
        print key

    for node in operon_nodes_list:
        pmid = operon_PMC[node[0].replace("ope_", "")]
        operon_sbml = "operon_sbml_%s.txt" % node[0].replace("ope_", "")
        operon_sbol = "operon_sbol_%s.png" % node[0].replace("ope_", "")
        f.write('\n\t\t\t{')
        f.write('\n\t\t\t\t"data":{')
        f.write('\n\t\t\t\t\t"id":"' + node[0] + '",')
        f.write('\n\t\t\t\t\t"sbml":"' + operon_sbml + '",')
        f.write('\n\t\t\t\t\t"sbol":"' + operon_sbol + '",')
        f.write('\n\t\t\t\t\t"name":"' + node[1] + '",')
        f.write('\n\t\t\t\t\t"PMID":"' + pmid + '"')
        f.write('\n\t\t\t\t},')

        f.write('\n\t\t\t\t"position":{')
        f.write('\n\t\t\t\t\t"x":' + str(node_coor_dictionary[node[0]][0] * x_coor_factor) + ',')
        f.write('\n\t\t\t\t\t"y":' + str(node_coor_dictionary[node[0]][1] * y_coor_factor))
        f.write('\n\t\t\t\t},')

        f.write('\n\t\t\t\t"classes":"operon')
        f.write('",')

        f.write('\n\t\t\t\t"selected":false')
        f.write('\n\t\t\t},')

        num_runs += 1

    num_runs = 0
    for node in output_transitions_nodes_list:
        ot_sbml = "ot_sbml_%s.txt" % node[0].replace("ot_", "")
        f.write('\n\t\t\t{')
        f.write('\n\t\t\t\t"data":{')
        f.write('\n\t\t\t\t\t"id":"' + str(node[0]) + '",')
        f.write('\n\t\t\t\t\t"sbml":"' + ot_sbml + '"')

        f.write('\n\t\t\t\t},')

        f.write('\n\t\t\t\t"position":{')

        f.write('\n\t\t\t\t\t"x":' + str(node_coor_dictionary[node[0]][0] * x_coor_factor) + ',')
        f.write('\n\t\t\t\t\t"y":' + str(node_coor_dictionary[node[0]][1] * y_coor_factor))
        f.write('\n\t\t\t\t},')
        f.write('\n\t\t\t\t"classes":"output transition')
        f.write('",')

        f.write('\n\t\t\t\t"selected":false')
        f.write('\n\t\t\t}')
        if num_runs < len(output_transitions_nodes_list) - 1:
            f.write(',')
        num_runs += 1

    f.write('\n\t\t],')
    f.write('\n\t\t"edges":[')

    edge_id = 0
    for edge in source_id_target_id_list:

        f.write('\n\t\t\t{')
        f.write('\n\t\t\t\t"data":{')
        f.write('\n\t\t\t\t\t"id":"' + str(edge[0] + "-" + edge[1]) + '",')
        f.write('\n\t\t\t\t\t"source":"' + str(edge[0]) + '",')
        f.write('\n\t\t\t\t\t"target":"' + str(edge[1]) + '"')
        f.write('\n\t\t\t\t},')
        f.write('\n\t\t\t\t\t"selected":false')
        f.write('\n\t\t\t}')
        if edge_id < (len(source_id_target_id_list) - 1):
            f.write(',')
        edge_id += 1

    f.write('\n\t\t]')
    f.write('\n\t}\n}')

    f.close()


def create_json_network_string(species_nodes_list, input_transitions_nodes_list,
                               operon_nodes_list, output_transitions_nodes_list,
                               source_id_target_id_list, path_json_highlighter):
    to_return = ""
    """Writes the whole network json."""

    node_list = species_nodes_list + input_transitions_nodes_list + operon_nodes_list + output_transitions_nodes_list
    node_coor_dictionary = nx_node_coordinates_dictionary(node_list, source_id_target_id_list)

    num_runs = 0

    x_coor_factor = resize_network(len(node_list), len(node_list))
    y_coor_factor = x_coor_factor

    to_return += '{"data" : { '
    to_return += '"selected" : true,'
    to_return += '"_Annotations": [] ,'
    to_return += '"shared_name" : "Test.sif",'
    to_return += '"SUID" : 52,'
    to_return += '"name":"Test.sif"'
    to_return += '},'
    to_return += '"elements":{'
    to_return += '"nodes":['

    for node in species_nodes_list:
        species_sbml = "species_sbml_%s.txt" % node[0].replace("spe_", "")
        node[2] = "None"

        to_return += '{'
        to_return += '"data":{'
        to_return += '"id":"' + node[0] + '",'
        to_return += '"name":"' + node[1] + '",'
        to_return += '"type":"' + node[2] + '",'
        to_return += '"sbml":"' + species_sbml + '"'
        to_return += '},'

        to_return += '"position":{'
        to_return += '"x":' + str(node_coor_dictionary[node[0]][0] * x_coor_factor) + ','
        to_return += '"y":' + str(node_coor_dictionary[node[0]][1] * y_coor_factor)
        to_return += '},'
        to_return += '"classes":"species'
        to_return += '",'

        to_return += '"selected":false'
        to_return += '},'
        num_runs += 1

    num_runs = 0
    for node in input_transitions_nodes_list:
        it_sbml = "it_sbml_%s.txt" % node[0].replace("it_", "")

        to_return += '{'
        to_return += '"data":{'
        to_return += '"id":"' + node[0] + '",'
        to_return += '"logic":"' + node[1] + '",'
        to_return += '"sbml":"' + it_sbml + '"'
        to_return += '},'

        to_return += '"position":{'
        to_return += '"x":' + str(node_coor_dictionary[node[0]][0] * x_coor_factor) + ','
        to_return += '"y":' + str(node_coor_dictionary[node[0]][1] * y_coor_factor)
        to_return += '},'
        to_return += '"classes":"input transition'
        to_return += '",'

        to_return += '"selected":false'
        to_return += '},'
        num_runs += 1

    conn, cur = db.db_open("sbider.db")
    operon_PMC = db.operon_PMC_dictionary(cur)
    db.db_close(conn, cur)
    num_runs = 0

    for node in operon_nodes_list:
        pmid = operon_PMC[node[0].replace("ope_", "")]
        operon_sbml = "operon_sbml_%s.txt" % node[0].replace("ope_", "")
        operon_sbol = "operon_sbol_%s.png" % node[0].replace("ope_", "")

        to_return += '{'
        to_return += '"data":{'
        to_return += '"id":"' + node[0] + '",'
        to_return += '"sbml":"' + operon_sbml + '",'
        to_return += '"sbol":"' + operon_sbol + '",'
        to_return += '"name":"' + node[1] + '",'
        to_return += '"PMID":"' + pmid + '"'
        to_return += '},'

        to_return += '"position":{'
        to_return += '"x":' + str(node_coor_dictionary[node[0]][0] * x_coor_factor) + ','
        to_return += '"y":' + str(node_coor_dictionary[node[0]][1] * y_coor_factor)
        to_return += '},'

        to_return += '"classes":"operon'
        to_return += '",'

        to_return += '"selected":false'
        to_return += '},'

        num_runs += 1

    num_runs = 0
    for node in output_transitions_nodes_list:
        ot_sbml = "ot_sbml_%s.txt" % node[0].replace("ot_", "")

        to_return += '{'
        to_return += '"data":{'
        to_return += '"id":"' + str(node[0]) + '",'
        to_return += '"sbml":"' + ot_sbml + '"'
        to_return += '},'

        to_return += '"position":{'

        to_return += '"x":' + str(node_coor_dictionary[node[0]][0] * x_coor_factor) + ','
        to_return += '"y":' + str(node_coor_dictionary[node[0]][1] * y_coor_factor)
        to_return += '},'
        to_return += '"classes":"output transition'
        to_return += '",'

        to_return += '"selected":false'
        to_return += '}'
        if num_runs < len(output_transitions_nodes_list) - 1:
            to_return += ','
        num_runs += 1

    to_return += '],'
    to_return += '"edges":['

    edge_id = 0
    for edge in source_id_target_id_list:

        to_return += '{'
        to_return += '"data":{'
        to_return += '"id":"' + str(edge[0] + "-" + edge[1]) + '",'
        to_return += '"source":"' + str(edge[0]) + '",'
        to_return += '"target":"' + str(edge[1]) + '"'
        to_return += '},'
        to_return += '"selected":false'
        to_return += '}'
        if edge_id < (len(source_id_target_id_list) - 1):
            to_return += ','
        edge_id += 1

    to_return += ']'
    to_return += '},'
    to_return += path_json_highlighter + '}'

    return to_return

