
# coding: utf-8

# In[1]:

import sys
import subprocess as sp
import SBiDer_helper
import sbider_database as db
import sbider_parser as parser
import sbider_searcher as searcher
import sbider_grapher as grapher


# In[2]:

print("Testing python package NetworkX...")

try:
    output = sp.check_output(['pip', 'show', 'networkx'])

except:
    print("Testing python package networkx failed.\n")
else:
    print("Testing python package networkx passed.\n")


# In[3]:

print("Testing database access and query...")

def testRunSBiDer(directory_path, user_query, indirect=False):

    # Access database
    database_file = directory_path + "/SBiDer.db"
    conn, cur = db.db_open(database_file)

    # Dictionary of fragmented user inputs that satisfy user query
    logic_dictionary = parser.parse_logic(cur, user_query)

    # Dictionaries of: Operon <-> InputSpecies, Operon <-> OutputSpecies, and Operon <-> Repressor
    input_dictionary, output_dictionary = db.make_ope_id_spe_id_dics(cur)
    repressor_dictionary = db.make_ope_id_rep_spe_id_dic(cur)
    #rint("** input dictionary")
    #BiDer_helper.printplus(input_dictionary)
    #rint("** output dictionary")
    #BiDer_helper.printplus(output_dictionary)
    #rint("** repressor dictionary")
    #BiDer_helper.printplus(repressor_dictionary)

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
        
        return all_operon_path == [[('21', '22'), ['72-3'], ['82-1']]]

    
## Test run SBiDer

path = "/cellar/users/hyeerna/BInf/SBiDer/CircuitNetwork/web"
user_input ="laci and iptg = yfp"
indirect_flag = False

if testRunSBiDer(path, user_input, indirect_flag):
    print("Testing database access and query passed.\n")
else:
    print("Testing database access and query failed.\n")

