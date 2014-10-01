"""
Subtitle

Descriptive paragraph

******************************************************************************
@author: Huwate(Kwat) Yeerna, University of California, San Diego
******************************************************************************
"""

import sys
import sbider_database as db
import sbider_parser as parser
import sbider_searcher as searcher
import sbider_grapher as grapher


def build_sbider_network(user_query, indirect=False):
    database_file = \
        "/Users/valeriysosnovskiy/UCSD_IGEM/CircuitNetwork/web/SBiDer_Database/sbider.db"
    conn, cur = db.db_open(database_file)

    print "user_query:", user_query

    logic_dictionary = parser.parse_logic(cur, user_query)
    print "build_sbider_network: logic_dictionary", logic_dictionary

    input_dictionary, output_dictionary = db.make_ope_id_spe_id_dicts(cur)

    all_operon_path_list_per_start_species = []
    file_name_idx = 1
    for input_species, output_species_list in logic_dictionary.items():
        operon_path_list_per_start_species = [input_species]

        for output_species in output_species_list:
            print "\t Path:", input_species, "--->", output_species, "="

            operon_path_list = searcher.get_sbider_path(input_dictionary,
                                                        output_dictionary,
                                                        list(input_species),
                                                        output_species,
                                                        indirect)

            operon_path_list_per_start_species.extend(operon_path_list)

            for operon_path in operon_path_list:
                print "\t\t build_sbider_network: operon_path =>", operon_path

        all_operon_path_list_per_start_species.append(operon_path_list_per_start_species)

        file_name = "/Users/valeriysosnovskiy/UCSD_IGEM/CircuitNetwork/web/test_json_file_%d.json" % file_name_idx

        grapher.create_subnetwork_json(cur, operon_path_list_per_start_species, file_name)

        file_name_idx += 1


if __name__ == "__main__":

    user_input = sys.argv[1]

    if len(sys.argv) == 3 and (sys.argv[2].lower() == 'true' or sys.argv[2].lower() == 't'):
        indirect_flag = True
    else:
        indirect_flag = False


    build_sbider_network(user_input, indirect_flag)