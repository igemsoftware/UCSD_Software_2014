"""Subtitle

Descriptive paragraph

******************************************************************************
@author: Huwate Yeerna, University of California, San Diego
******************************************************************************

"""



import sys
import matplotlib.pyplot as plt
import networkx as nx



def traverse(input_dictionary, output_dictionary,
             input_species_list, output_species_list,
             path_queue,
             final_operon_path_list, final_species_path_list):
    """Construct genetic interaction path.

    Argument(s):
        input_dictionary -
        output_dictionary -
        input_species_list -
        output_species_list -
        path_queue -
        final_operon_path_list -
        final_species_path_list -

    Return:
        description
    """

    (visited_operon_list, visited_species_list) = path_queue.pop(0)

    # visited species become input species
    an_input_species_list = list(visited_species_list)

    ###print "\tan_input_species_list:",an_input_species_list

    # searches for operons activated by current input species
    for an_operon in set(input_dictionary.keys()) - set(visited_operon_list):

        ###print "\t\tan_operon & potential output species:",an_operon,\
                ###"&",input_dictionary[an_operon]
        ###print "\t\tcan",an_input_species_list,"activate",\
                ###input_dictionary[an_operon],"???"
        if is_activated(input_dictionary[an_operon], an_input_species_list) ==\
                                                                        True:

            ###print "\t\t\tyes!"

            # store activated operon and its unique outout
            a_visited_operon_list = list(visited_operon_list) + [an_operon]
            a_visited_species_list = unite_lists([visited_species_list,\
                                                  output_dictionary[an_operon]])

            ###print "\t\t\ta_visited_operon_list:",a_visited_operon_list
            ###print "\t\t\ta_visited_species_list",a_visited_species_list
            ###print "\t\t\toutput_species_list:",output_species_list

            # if output speices is found, include this operon and\
            # species path lists in the final operon and species paths
            if set(output_species_list).issubset(a_visited_species_list):

                ###print "\t\t\t\toutput species found!"

                final_operon_path_list.append(a_visited_operon_list)
                final_species_path_list.append(a_visited_species_list)

            # if output species is not found, include this operon and\
            # species path lists in path queue
            else:

                ###print "\t\t\t\toutput species not found..."

                path_queue.append((a_visited_operon_list,\
                                   a_visited_species_list))

    ###print "\t\tfinal path_queue:",path_queue

    return path_queue, final_operon_path_list, final_species_path_list



def get_path(input_dictionary, output_dictionary,
             input_species_list, output_species_list):
    """Get path from input species to output species.

    Argument(s):
        input_dictionary -
        outout_dictionary -
        input_species_list -
        output_species_list -

    Return:
        description
    """

    input_operon_list = []
    path_queue = [(input_operon_list, input_species_list) ]

    final_operon_path_list = []
    final_species_path_list = []

    while path_queue != []:

        ###print "\nget_path: path queue:",path_queue

        path_queue,\
        final_operon_path_list,\
        final_species_path_list = traverse(input_dictionary,
                                           output_dictionary,
                                           input_species_list,
                                           output_species_list,
                                           path_queue,
                                           final_operon_path_list,
                                           final_species_path_list)

    return final_operon_path_list, final_species_path_list





if __name__ == '__main__':
     get_path(argv[1:5:1])
