"""
Subtitle

Descriptive paragraph

******************************************************************************
@author: Joaquin Reina, University of California, San Diego
         Huwate(Kwat) Yeerna, University of California, San Diego
******************************************************************************
"""

import networkx as nx
import sbider_database as db


def get_input_transition_species_dictionary(cursor):
    input_transitions_species_dict = {}
    input_transition_species_list = db.db_select(cursor, "InputTransitionSpecies", ["it_id", "spe_id"])
    it_id_list = []
    for it_id, spe_id in input_transition_species_list:
        if it_id not in it_id_list:
            input_transitions_species_dict[it_id] = [spe_id]
            it_id_list.append(it_id)
        else:
            input_transitions_species_dict[it_id].append(spe_id)
    return input_transitions_species_dict


def list_of_lists(list_of_tuples):
    """Convert list of tuples to list of lists"""
    list_of_lists = []
    for tup in list_of_tuples:
        list_of_lists.append(list(tup))


    return list_of_lists


def unique_node_list(node_list):
    """Duplicate nodes values are removed from the node_list"""
    unique_node_list = []
    used_node_id_list = []
    for node in node_list:
        if node not in used_node_id_list:

            unique_node_list.append(node)
            used_node_id_list.append(node)
    return unique_node_list


def list_of_tuples(list_of_lists):
    """Convert list of lists to list of tuples."""
    list_of_tuples = []
    for lst in list_of_lists:
        list_of_tuples.append(tuple(lst))


    return list_of_tuples


def add_node_id_abbreviation(node, abbrev, index):
    """Adds an id abbreviation to node."""
    node[index] = abbrev + node[index]
    return node


def add_node_list_id_abbreviation(node_list, abbrev, index):
    """Adds an id abbreviation to a list of nodes."""
    for node in node_list:
        node = add_node_id_abbreviation(node, abbrev, index)
    return node_list


def add_edge_id_abbreviation(edge, abbrev1, abbrev2, index1=0, index2=0):
    return (abbrev1 + edge[0], abbrev2 + edge[1])


def add_edge_list_id_abbreviation(edge_list, abbrev1, abbrev2, index1=0, index2=0):
    edge_list_abbrev = []
    for edge in edge_list:
        edge_list_abbrev.append(add_edge_id_abbreviation(edge, abbrev1, abbrev2, index1, index2))
    return edge_list_abbrev


def merge_list_of_lists(list_of_lists):
    condensed_list = []
    for lst in list_of_lists:
        condensed_list.extend(lst)
    return condensed_list


def get_node_from_id(cursor, node_table_name, node_id, node_id_type):


    node_cursor = db.db_select(cursor, node_table_name, "*", [node_id_type], ["="], [node_id], [""])


    node = node_cursor.fetchone()


    node = list(node)


    return node


def get_node_list_from_other_node_id(cursor, node_other_node_relationship_table, other_node_id, other_node_id_type,
                                     node_table_name, node_id_type):
    node_id = db.db_select(cursor, node_other_node_relationship_table,
                           [node_id_type],
                           [other_node_id_type],
                           ["="],
                           ["'" + other_node_id + "'"],
                           [""])


    node_id_list = node_id.fetchall()
    node_id_list = list_of_lists(node_id_list)


    node_list = []
    for node_id in node_id_list:

        node = get_node_from_id(cursor, node_table_name, node_id[0], node_id_type)


        node = list(node)
        node_list.append(node)
    return node_list


def determine_operon_activated_input_transition(cursor, starting_species_list, operon_id, it_id_dict):
    """Determining which input transition is activating the operon."""
    starting_species_set = set(tuple(starting_species_list))
    it_trans_id_list = db.db_select(cursor, "OperonInputTransition", ["it_id"], ["ope_id"], ["="],
                                    ["'" + operon_id + "'"], [""])
    it_trans_id_list = it_trans_id_list.fetchall()
    it_trans_id_list = list_of_lists(it_trans_id_list)
    it_trans_id_list = merge_list_of_lists(it_trans_id_list)


    activated_it_id_list = []
    for it_trans_id in it_trans_id_list:



        activating_species_set = set(it_id_dict[it_trans_id])



        if starting_species_set.issuperset(activating_species_set):
            activated_it_id_list.append(it_trans_id)
    return activated_it_id_list
def create_operon_node(cursor, operon_id):
    """Create operon nodes from the corresponding operon_id."""


    operon_node = get_node_from_id(cursor, "Operon", "'" + operon_id + "'", "ope_id")


    operon_node_abbrev = add_node_id_abbreviation(operon_node, "ope_", 0)



    return operon_node_abbrev, operon_id


def create_input_transition_nodes(cursor, starting_species_list, operon_id, it_id_dict):
    """Create input transition nodes from the corresponding operon_id."""

    activated_it_ids = determine_operon_activated_input_transition(cursor, starting_species_list, operon_id, it_id_dict)


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
    """Create input transition nodes from the corresponding operon_id."""

    ot_node = get_node_list_from_other_node_id(cursor, "OperonOutputTransition", operon_id, "ope_id",
                                               "OutputTransition", "ot_id")[0]
    ot_id = ot_node[0]

    ot_node_abbrev = add_node_id_abbreviation(ot_node, "ot_", 0)



    return ot_node_abbrev, ot_id


def create_input_species_nodes(cursor, it_id):
    """Create species nodes from the corresponding it_id."""

    it_species_nodes = get_node_list_from_other_node_id(cursor, "InputTransitionSpecies", it_id, "it_id",
                                                        "Species", "spe_id")
    it_species_nodes = it_species_nodes

    it_species_ids = [spe_id[0] for spe_id in it_species_nodes]
    it_species_nodes_abbrev = [add_node_id_abbreviation(spe_node, "spe_", 0) for spe_node in it_species_nodes]
    it_species_nodes_abbrev = [tuple(tup) for tup in it_species_nodes_abbrev]


    return it_species_nodes_abbrev, it_species_ids


def create_output_species_nodes(cursor, ot_id):
    """Create species nodes from the corresponding ot_id."""

    ot_species_nodes = get_node_list_from_other_node_id(cursor, "OutputTransitionSpecies", ot_id, "ot_id",
                                                        "Species", "spe_id")

    ot_species_nodes = ot_species_nodes


    ot_species_ids = [spe_id[0] for spe_id in ot_species_nodes]
    ot_species_nodes_abbrev = [add_node_id_abbreviation(spe_node, "spe_", 0) for spe_node in ot_species_nodes]
    ot_species_nodes_abbrev = [tuple(tup) for tup in ot_species_nodes_abbrev]


    return ot_species_nodes_abbrev, ot_species_ids


def nx_node_coor_dictionary(node_list, edge_list):
    """Creates a dictionary of node positions using spring layout from networkx."""

    json_graph = nx.Graph()
    add_node_values_to_nxGraph(json_graph, node_list)
    json_graph.add_edges_from(edge_list)
    node_coor_dictionary = nx.spring_layout(json_graph)
    return node_coor_dictionary


def add_node_values_to_nxGraph(nxGraph, node_list):
    """Extracts the node id and enters it into nxGraph."""

    for node in node_list:
        nxGraph.add_node(node[0])


def create_subnetwork_path(cursor, starting_species_list, operon_path, it_trans_dict):
    """Creating a subnetwork path."""

    species_set = set()
    input_transition_set = set()
    operon_set = set()
    output_transition_set = set()
    edge_path_list = []
    current_species_list = starting_species_list


    for operon in range(len(operon_path)):

        operon_id = operon_path.pop(0)

        operon_node_abbrev, _ = create_operon_node(cursor, operon_id)

        operon_set.add(tuple(operon_node_abbrev))

        it_node_abbrev_list, it_id_list = create_input_transition_nodes(cursor, current_species_list,
                                                                        operon_id, it_trans_dict)
        for it_node_abbrev, it_id in zip(it_node_abbrev_list, it_id_list):
            it_id_abbrev = it_node_abbrev[0]
            input_transition_set.add(tuple(it_node_abbrev))
            edge_path_list.append([it_node_abbrev[0], operon_node_abbrev[0]])

        ot_node_abbrev, ot_id = create_output_transition_node(cursor, operon_id)
        ot_id_abbrev = ot_node_abbrev[0]
        output_transition_set.add(tuple(ot_node_abbrev))
        edge_path_list.append([operon_node_abbrev[0], ot_node_abbrev[0]])



        for it_node_abbrev, it_id in zip(it_node_abbrev_list, it_id_list):
            it_species_nodes_abbrev, _ = create_input_species_nodes(cursor, it_id)
            for it_species_node_abbrev in it_species_nodes_abbrev:
                species_set.add(tuple(it_species_node_abbrev))
                edge_path_list.append([it_species_node_abbrev[0], it_node_abbrev[0]])




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
    source_id_target_id_paths = []
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

    return species_subnetwork_list, input_transition_subnetwork_list, operon_subnetwork_list, output_transition_subnetwork_list, source_id_target_id_list


def get_whole_network(cursor):
    """Whole network data prep for json."""

    #*****Gathering all nodes
    species_nodes_list = db.db_select(cursor, "Species", ["spe_id", "name", "type"])
    species_nodes_list = species_nodes_list.fetchall()
    species_nodes_list = list_of_lists(species_nodes_list)
    species_nodes_list_abbrev = add_node_list_id_abbreviation(species_nodes_list, "spe_", 0)


    input_transition_nodes_list = db.db_select(cursor, "InputTransition", ["it_id", "logic"])
    input_transition_nodes_list = input_transition_nodes_list.fetchall()
    input_transition_nodes_list = list_of_lists(input_transition_nodes_list)
    input_transition_nodes_list_abbrev = add_node_list_id_abbreviation(input_transition_nodes_list, "it_", 0)


    operon_nodes_list = db.db_select(cursor, "Operon", ["ope_id", "name", "image"])
    operon_nodes_list = operon_nodes_list.fetchall()
    operon_nodes_list = list_of_lists(operon_nodes_list)
    operon_nodes_list_abbrev = add_node_list_id_abbreviation(operon_nodes_list, "ope_", 0)


    output_transition_nodes_list = db.db_select(cursor, "OutputTransition", ["ot_id"])
    output_transition_nodes_list = output_transition_nodes_list.fetchall()
    output_transition_nodes_list = list_of_lists(output_transition_nodes_list)
    output_transition_nodes_list_abbrev = add_node_list_id_abbreviation(output_transition_nodes_list, "ot_", 0)

    species_nodes_list_abbrev, input_transition_nodes_list_abbrev, operon_nodes_list_abbrev, output_transition_nodes_list_abbrev


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


    all_edges = species_input_transition_edge_list_abbrev + input_transition_operon_edge_list_abbrev + operon_output_transition_edge_list_abbrev + output_transition_species_edge_list_abbrev


    return (species_nodes_list_abbrev, input_transition_nodes_list_abbrev, operon_nodes_list_abbrev,
            output_transition_nodes_list_abbrev, all_edges)


def create_json_network(json_file_path, species_nodes_list, input_transitions_nodes_list,
                        operon_nodes_list, output_transitions_nodes_list, source_id_target_id_list):
    """Writes the whole network json."""

    node_list = species_nodes_list + input_transitions_nodes_list + operon_nodes_list + output_transitions_nodes_list
    node_coor_dictionary = nx_node_coor_dictionary(node_list, source_id_target_id_list)

    f = open(json_file_path, 'w')
    numRuns = 0

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

    for node in species_nodes_list:

        node[2] = "None"

        f.write('\n\t\t\t{')
        f.write('\n\t\t\t\t"data":{')
        f.write('\n\t\t\t\t\t"id":"' + node[0] + '",')
        f.write('\n\t\t\t\t\t"name":"' + node[1] + '",')
        f.write('\n\t\t\t\t\t"type":"' + node[2] + '"')
        f.write('\n\t\t\t\t},')

        f.write('\n\t\t\t\t"position":{')
        f.write('\n\t\t\t\t\t"x":' + str(node_coor_dictionary[node[0]][0] * x_coor_factor) + ',')
        f.write('\n\t\t\t\t\t"y":' + str(node_coor_dictionary[node[0]][1] * y_coor_factor))
        f.write('\n\t\t\t\t},')
        f.write('\n\t\t\t\t"classes":"species')
        f.write('",')

        f.write('\n\t\t\t\t"selected":false')
        f.write('\n\t\t\t},')
        numRuns += 1

    numRuns = 0
    for node in input_transitions_nodes_list:
        f.write('\n\t\t\t{')
        f.write('\n\t\t\t\t"data":{')
        f.write('\n\t\t\t\t\t"id":"' + node[0] + '",')
        f.write('\n\t\t\t\t\t"logic":"' + node[1] + '"')
        f.write('\n\t\t\t\t},')

        f.write('\n\t\t\t\t"position":{')
        f.write('\n\t\t\t\t\t"x":' + str(node_coor_dictionary[node[0]][0] * x_coor_factor) + ',')
        f.write('\n\t\t\t\t\t"y":' + str(node_coor_dictionary[node[0]][1] * y_coor_factor))
        f.write('\n\t\t\t\t},')
        f.write('\n\t\t\t\t"classes":"input transition')
        f.write('",')

        f.write('\n\t\t\t\t"selected":false')
        f.write('\n\t\t\t},')
        numRuns += 1

    numRuns = 0
    for node in operon_nodes_list:

        node[2] = "None"

        node[0] = node[0].replace(",", "-")

        f.write('\n\t\t\t{')
        f.write('\n\t\t\t\t"data":{')
        f.write('\n\t\t\t\t\t"id":"' + node[0] + '",')
        f.write('\n\t\t\t\t\t"SBOL":"' + node[2] + '",')
        f.write('\n\t\t\t\t\t"name":"' + node[1] + '"')
        f.write('\n\t\t\t\t},')

        f.write('\n\t\t\t\t"position":{')
        f.write('\n\t\t\t\t\t"x":' + str(node_coor_dictionary[node[0]][0] * x_coor_factor) + ',')
        f.write('\n\t\t\t\t\t"y":' + str(node_coor_dictionary[node[0]][1] * y_coor_factor))
        f.write('\n\t\t\t\t},')


        f.write('\n\t\t\t\t"classes":"operon')
        f.write('",')

        f.write('\n\t\t\t\t"selected":false')
        f.write('\n\t\t\t},')

        numRuns += 1

    numRuns = 0
    for node in output_transitions_nodes_list:
        f.write('\n\t\t\t{')
        f.write('\n\t\t\t\t"data":{')
        f.write('\n\t\t\t\t\t"id":"' + str(node[0]) + '"')
        f.write('\n\t\t\t\t},')

        f.write('\n\t\t\t\t"position":{')



        f.write('\n\t\t\t\t\t"x":' + str(node_coor_dictionary[node[0]][0] * x_coor_factor) + ',')
        f.write('\n\t\t\t\t\t"y":' + str(node_coor_dictionary[node[0]][1] * y_coor_factor))
        f.write('\n\t\t\t\t},')
        f.write('\n\t\t\t\t"classes":"output transition')
        f.write('",')

        f.write('\n\t\t\t\t"selected":false')
        f.write('\n\t\t\t}')
        if numRuns < len(output_transitions_nodes_list) - 1:
            f.write(',')
        numRuns += 1

    device_number = 0
    f.write('\n\t\t],')
    f.write('\n\t\t"edges":[')

    edge_id = 0
    for edge in source_id_target_id_list:

        f.write('\n\t\t\t{')
        f.write('\n\t\t\t\t"data":{')
        f.write('\n\t\t\t\t\t"id":"' + str(edge_id + 50) + '",')
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


def create_whole_network_json():
    """Generates the whole network json."""

    conn, cursor = db.db_open("sbider.db")
    json_info = get_whole_network(cursor)
    create_json_network("sbider_whole_network.json", *json_info)
    db.db_close(conn, cursor)


def create_subnetwork_json(cursor, list_of_operon_paths, json_file_name="subnetwork_test.json"):
    """Generates the subnetwork json."""

    operon_input_transition_dictionary = get_input_transition_species_dictionary(cursor)
    json_info = get_subnetwork(cursor, list_of_operon_paths)
    create_json_network(json_file_name, *json_info)