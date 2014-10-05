"""
Subtitle

Descriptive paragraph

******************************************************************************
@author: Huwate(Kwat) Yeerna, University of California, San Diego
         Joaquin Reyna, University of California, San Diego
******************************************************************************
"""

import sys

import sbider_database as db
import sbider_parser as parser
import sbider_searcher as searcher
import sbider_grapher as grapher


def build_sbider_network(directory_path, user_query, indirect=False):
    database_file = directory_path + "/sbider.db"
    conn, cur = db.db_open(database_file)

    logic_dictionary = parser.parse_logic(cur, user_query)
    input_dictionary, output_dictionary = db.make_ope_id_spe_id_dics(cur)
    repressor_dictionary = db.make_ope_id_rep_spe_id_dic(cur)

    all_operon_path = []
    for input_species, output_species_list in logic_dictionary.items():

        operon_path_per_start_species = [input_species]
        for output_species in output_species_list:
            print "\t build_sbider_network: getting operon path:", input_species, "--->", output_species, "="
            operon_path_list = searcher.get_sbider_path(input_dictionary,
                                                        repressor_dictionary,
                                                        output_dictionary,
                                                        list(input_species),
                                                        output_species,
                                                        indirect)
            for operon_path in operon_path_list:
                print "\t\t build_sbider_network: operon path =>", operon_path

            operon_path_per_start_species.extend(operon_path_list)

        all_operon_path.append(operon_path_per_start_species)


        path_json = grapher.create_subnetwork_json_string(cur, operon_path_per_start_species)
        return path_json


if __name__ == "__main__":
    # print "main: sys.argv",  sys.argv
    path = sys.argv[1]
    last_argv = str(sys.argv[-1]).lower()
    # print "main: last_argv", last_argv

    if last_argv == 't':
        user_input = " ".join(sys.argv[2:-1:])
        indirect_flag = True

    elif last_argv == 'f':
        user_input = " ".join(sys.argv[2:-1:])
        indirect_flag = False

    else:
        user_input = " ".join(sys.argv[2::])
        indirect_flag = False

    # print "main: path:", path
    # print "main: user_input:", user_input
    # print "main: indirect_flag:", indirect_flag

    final_path_json = build_sbider_network(path, user_input, indirect_flag)
    print >> sys.stderr, final_path_json



# End of sbider_network_builder.py
