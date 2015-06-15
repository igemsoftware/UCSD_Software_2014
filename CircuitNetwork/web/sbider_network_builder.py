"""
SBiDer main

******************************************************************************
@author: Huwate(Kwat) Yeerna, University of California, San Diego
         Joaquin Reyna, University of California, San Diego
******************************************************************************

Arguments:
    # 0=sbider_network_builder.py
    # 1=database path
    # 2=user input
    # 3=indirect flag

"""


import sys
import SBiDer_helper
import sbider_database as db
import sbider_parser as parser
import sbider_searcher as searcher
import sbider_grapher as grapher


sys.path+=['', '/bioinformatics/software/anaconda2.7/lib/python2.7/site-packages/openpyxl-1.6.2-py2.7.egg', '/bioinformatics/software/anaconda2.7/lib/python2.7/site-packages/psycopg2-2.5-py2.7-linux-x86_64.egg', '/bioinformatics/software/anaconda2.7/lib/python2.7/site-packages/matplotlib_venn-0.9-py2.7.egg', '/bioinformatics/software/anaconda2.7/lib/python27.zip', '/bioinformatics/software/anaconda2.7/lib/python2.7', '/bioinformatics/software/anaconda2.7/lib/python2.7/plat-linux2', '/bioinformatics/software/anaconda2.7/lib/python2.7/lib-tk', '/bioinformatics/software/anaconda2.7/lib/python2.7/lib-old', '/bioinformatics/software/anaconda2.7/lib/python2.7/lib-dynload', '/bioinformatics/software/anaconda2.7/lib/python2.7/site-packages', '/bioinformatics/software/anaconda2.7/lib/python2.7/site-packages/PIL', '/bioinformatics/software/anaconda2.7/lib/python2.7/site-packages/setuptools-0.6c11-py2.7.egg-info']


def build_sbider_network(directory_path, user_query, indirect=False):

    print("** build_sbider_network")

    # Access database
    database_file = directory_path + "/SBiDer.db"
    conn, cur = db.db_open(database_file)

    # Dictionary of fragmented user inputs that satisfy user query
    logic_dictionary = parser.parse_logic(cur, user_query)

    # Dictionaries of: Operon <-> InputSpecies & Operon <-> OutputSpecies
    input_dictionary, output_dictionary = db.make_ope_id_spe_id_dics(cur)

    print("** input dictionary")
    SBiDer_helper.printplus(input_dictionary)

    print("** output dictionary")
    SBiDer_helper.printplus(output_dictionary)

    # Dictionary of: Operon <-> Repressor
    repressor_dictionary = db.make_ope_id_rep_spe_id_dic(cur)

    print("** repressor dictionary")
    SBiDer_helper.printplus(repressor_dictionary)

    # Build operon path for each fragmented user input, which satisfies user query
    all_operon_path = []
    for input_species, output_species_list in logic_dictionary.items():

        operon_path_per_start_species = [input_species]
        for output_species in output_species_list:
            operon_path_list = searcher.get_sbider_path(input_dictionary,
                                                        repressor_dictionary,
                                                        output_dictionary,
                                                        list(input_species),
                                                        output_species,
                                                        indirect)

            operon_path_per_start_species.extend(operon_path_list)
        all_operon_path.append(operon_path_per_start_species)

        # Create JSON file needed to display the found genetic circuit
        path_json = grapher.create_subnetwork_json_string(cur, operon_path_per_start_species, database_file)

        return path_json


if __name__ == "__main__":

    path = sys.argv[1]

    last_argv = str(sys.argv[-1]).lower()

    if last_argv == 't':
        user_input = " ".join(sys.argv[2:-1:])
        indirect_flag = True

    elif last_argv == 'f':
        user_input = " ".join(sys.argv[2:-1:])
        indirect_flag = False

    else:
        user_input = " ".join(sys.argv[2::])
        indirect_flag = False

    print("*path "+path)
    print("*user input "+user_input)
    print("*indirect flag "+str(indirect_flag) +"\n")


    final_path_json = build_sbider_network(path, user_input, indirect_flag)
    print(final_path_json)


# End of sbider_network_builder.py