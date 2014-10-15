import sbider_database as db

import sbider_grapher as sg

import sys

import os

import shutil

import random

import numpy as np

import math

import sbml_update as su

import Gen_Network as gn


def db_test():
    conn, cur = db.db_open("sbider_test_2.db")
    return conn, cur




def reset_db(original_db = "sbider.db", test_db_file = "sbider_test_2.db"):
    os.remove(test_db_file)
    shutil.copyfile(original_db, test_db_file)




def get_last_row_id(cursor, table_name):
    """Get the last inserted rowid."""
    last_id = cursor.execute("SELECT rowid FROM %s" % table_name).fetchall()
    last_id = len(last_id)
    return last_id
    




def select_last_inserted_table_id(cursor, table_name, table_id_type):
    """Select the last inserted row."""
    
    last_id = get_last_row_id(cursor, table_name)        
    last_entry = cursor.execute("SELECT {} FROM {} WHERE rowid = {}".format(table_id_type, table_name, last_id))    
    last_entry = last_entry.fetchone()
        
    return last_entry[0]




def select_last_inserted_table_row(cursor, table_name):
    """Select the last inserted row."""
    
    last_id = get_last_row_id(cursor, table_name)    
    last_entry = cursor.execute("SELECT * FROM {} WHERE rowid = {}".format(table_name, last_id))    
    last_entry = last_entry.fetchone()
    
    return last_entry




def make_new_id(id_string):
    """Convert old string id to old string id + 1."""

    new_id = int(id_string) + 1
    return str(new_id)




def check_species_name_in_database(cursor, species_name):
    """Safely return species id or None."""
    try:
        species_id = cursor.execute("SELECT spe_id FROM Species WHERE name = '%s'" % species_name.lower())
        species_id = species_id.fetchone()[0]
        return species_id
    
    except TypeError:
        return ""






def make_sbol_string_db_update(input_list, direction):
    """ Make an sbol string using uploading information."""
    color_list=np.linspace(1,14,14)
    random_color_list=[]
    for next in color_list:
        random_color_list.append(int(next))
    
    if direction.lower() == 'l':
        direction='<'
    else:
        direction = ''
        
    output_string=''
    for species in input_list:
        first_character=species[0]
        species = species[1::]
        
        if first_character == 'p':
            output_string=output_string + direction + 'p ' + species + ' ' +             str(random_color_list.pop(random.randrange(0,len(random_color_list)))) + '\n'

        else:
            output_string=output_string + direction + 'c ' + species +  ' ' +             str(random_color_list.pop(random.randrange(0,len(random_color_list)))) + '\n'

    output_string=output_string + direction + 't ' +     str(random_color_list.pop(random.randrange(0,len(random_color_list)))) +'\n# Arcs'  

    return output_string


def make_sbol_file(output_species_list, promoter_list, prev_operon_direction, operon_id):
    """Insert and make the sbol file."""
    
    sbol_list = promoter_list + ["c" + data[0] for data in output_species_list]            
    sbol_string = make_sbol_string_db_update(sbol_list, prev_operon_direction)
    write_sbol_file(operon_id, sbol_string)
    
    return sbol_file


def write_sbol_file(operon_id, sbol_string):
    """Write out sbol string to file."""
    
    file_name = "operon_sbol_" + operon_id + ".txt"
    write_to_file(sbol_string, file_name)


def write_to_file(string_to_write, file_name):
    """Write a file."""
    #f_path = os.getcwd() + "/path/to/sbml_folder/" + file_name
    f_path = os.getcwd() + "/" + file_name
    f_handle = open(f_path, 'w')
    f_handle.write(string_to_write)
    f_handle.close()
    return 

def make_input_transition_sbml_file(input_species_list, transition_id, operon_id, trans_logic):
    input_species_id_repression_list = [("spe_" + data[0], data[2]) for data in input_species_list]            
    input_transition_sbml_list = [operon_id] + input_species_id_repression_list
    it_sbml_file_name = "it_sbml_{}".format(transition_id)             
    su.sbml_input_trans(transition_id,
                        input_species_id_repression_list,
                        "ope_" + operon_id,
                        trans_logic,
                        it_sbml_file_name)
   

def make_output_transition_sbml_file(output_species_list, transition_id, operon_id):
    """make the sbml."""
    os_abbrev_id_list = ["spe_" + data[-1] for data in output_species_list]
    ot_sbml_file_name = "ot_sbml_{}".format(transition_id) 
    su.sbml_output_trans(transition_id,\
                        os_abbrev_id_list,\
                        "ope_" + operon_id,\
                        ot_sbml_file_name)
    

def insert_new_plasmid(cursor, plasmid_name, miriam_id):
    """Insert new plasmid."""
    plasmid_id = select_last_inserted_table_id(cursor, "Plasmid", "pla_id")
    plasmid_id = make_new_id(plasmid_id)    
    db.db_insert(cursor, "Plasmid", ["pla_id", "name", "miriam_id"], [plasmid_id, plasmid_name, miriam_id])
    return plasmid_id


def insert_new_operon(cursor, plasmid_id, operon_name, direction):
    """Insert new operon."""
    operon_id = select_last_inserted_table_id(cursor, "Operon", "ope_id").replace("-", "")
    operon_id = make_new_id(operon_id)
    sbol = "operon_sbol_{}.png".format(operon_id)
    sbml = "operon_sbml_{}.txt".format(operon_id)
    db.db_insert(cursor, "PlasmidOperon", ["ope_id", "pla_id", "direction"], [operon_id, plasmid_id, direction])
    db.db_insert(cursor, "Operon", ["ope_id", "name", "sbol", "sbml"], [operon_id, operon_name, sbol, sbml]) 
    return operon_id


def insert_new_input_transition(cursor, operon_id, logic):
    """Insert new input transition."""
    
    it_id = select_last_inserted_table_id(cursor, "InputTransition", "it_id")
    it_id = make_new_id(it_id)
    sbml = "it_sbml_{}.txt".format(it_id)    
    db.db_insert(cursor, "OperonInputTransition", ["ope_id", "it_id"], [operon_id, it_id])
    db.db_insert(cursor, "InputTransition", ["it_id", "logic", "sbml"], [it_id, logic, sbml]) 
    
    return it_id


def insert_new_input_transition_species(cursor, it_id, species_name, species_type, species_repression):
    """Insert new input transition species."""
    
    check_db_species_id = check_species_name_in_database(cursor, species_name)
    if check_db_species_id ==  "":
        last_spe_id = select_last_inserted_table_id(cursor, "Species", "spe_id")
        spe_id = make_new_id(last_spe_id)        
        sbml = "species_sbml_{}.txt".format(spe_id)
        db.db_insert(cursor, "Species", ["spe_id", "name", "type", "sbml"],\
                     [spe_id, species_name.lower(), species_type.lower(), sbml]) 
	su.sbml_species(it_id, species_name, sbml)
    else:
        spe_id = check_db_species_id
        
    last_in_id = select_last_inserted_table_id(cursor, "InputTransitionSpecies", "in_id")
    in_id = make_new_id(last_in_id)
    db.db_insert(cursor, "InputTransitionSpecies", ["in_id", "it_id", "spe_id", "repression"], [in_id, it_id, spe_id, species_repression])
        
    return spe_id


def insert_new_output_transition(cursor, operon_id):
    #def insert_new_output_transition(cursor, logic, operon_id)
    """Insert new output transition."""
    ot_id = select_last_inserted_table_id(cursor, "OutputTransition", "ot_id")
    ot_id = make_new_id(ot_id)
    sbml = "ot_sbml_{}.txt".format(ot_id)
    db.db_insert(cursor, "OperonOutputTransition", ["ope_id", "ot_id"], [operon_id, ot_id])  
    db.db_insert(cursor, "OutputTransition", ["ot_id", "sbml"], [ot_id, sbml]) 
    #db.db_insert(cursor, "OutputTransition", ["ot_id", "logic", "sbml"], [ot_id, logic sbml]) 
    
    return ot_id




def insert_new_output_transition_species(cursor, ot_id, species_name, species_type):
    """Insert new output transition species."""
    
    check_db_species_id = check_species_name_in_database(cursor, species_name.strip().lower())
    if check_db_species_id ==  "":
        last_spe_id = select_last_inserted_table_id(cursor, "Species", "spe_id")        
        spe_id = make_new_id(last_spe_id)
        sbml = "species_sbml_{}.txt".format(spe_id)
        db.db_insert(cursor, "Species", ["spe_id", "name", "type", "sbml"], [spe_id, species_name.lower(),                                                                             species_type.lower(), sbml]) 
	su.sbml_species(ot_id, species_name, sbml)
        
    else:
        spe_id = check_db_species_id
        
    last_out_id = select_last_inserted_table_id(cursor, "OutputTransitionSpecies", "out_id")
    out_id = make_new_id(last_out_id)
    db.db_insert(cursor, "OutputTransitionSpecies", ["out_id","ot_id", "spe_id"], [out_id, ot_id, spe_id])    
        
    return spe_id






def get_data_keyword(data_string):
    """Get the keyword belonging to data_string."""
    
    colon_index = data_string.index(":")
    return data_string[0:colon_index:]




def determine_parent_keyword(component_keyword):
    """Determine which is your parent keyword."""
        
    if component_keyword == "Operon":
        return "Plasmid"
        
    elif component_keyword == "InputTransition":
        return "Operon"
        
    elif component_keyword == "InputSpecies":
        return "InputTransition"
        
    elif component_keyword == "OutputTransition":
        return "Operon"
        
    elif component_keyword == "OutputSpecies":
        return "OutputTransition"
    
    else:
        return None




def determine_and_insert(connection, cursor, component_keyword, component_data = [], parent_component_id = ""):
    """Determine insertion method and insert into into the database."""

    
    if component_keyword == "Plasmid":
        data_id = insert_new_plasmid(cursor, *component_data)
        
    elif component_keyword == "Operon":
        data_id = insert_new_operon(cursor, parent_component_id, *component_data)
        operon_sbml = "operon_sbml_{}".format(data_id)
        su.sbml_operon(data_id, component_data[0], "123" + data_id, operon_sbml)
        
    elif component_keyword == "InputTransition":
        data_id = insert_new_input_transition(cursor, parent_component_id, *component_data)
        
    elif component_keyword == "InputSpecies":
        data_id = insert_new_input_transition_species(cursor, parent_component_id, *component_data)
        
    elif component_keyword == "OutputTransition":
        data_id = insert_new_output_transition(cursor, parent_component_id)
        
    elif component_keyword == "OutputSpecies":
        data_id = insert_new_output_transition_species(cursor, parent_component_id, *component_data)
        
    else:
        data_id = ""
    
    connection.commit()
    return data_id
        


def insert_new_device(connection, cursor, device):
    """Inserts a new device into the database.
        Argument(s):
            connection - sqlite3 connection object
            cursor - sqlite3 cursor object
            device_string - whole device as a string
    """
    
    parent_ids_dict = {"Plasmid": "", "Operon": "", "InputTransition": "", "OutputTransition": "" }
    input_species_list = []
    output_species_list = []
    promoter_list = []
    sbol_files = []
    
    
    for component in device:
        component_keyword = get_data_keyword(component)
        component_data = component.replace(component_keyword + ":", "")
        component_data = component_data.split(",")
        
        if component_keyword == "Operon" and len(output_species_list) > 0:
            
            sbol_files.append(make_sbol_file(output_species_list,                                             promoter_list,                                             prev_operon_direction,                                             parent_ids_dict["Operon"]))
            prev_operon_direction = component_data[:-1:][0]


            ###sbml input transition file creation
            make_input_transition_sbml_file(input_species_list,                                       parent_ids_dict["InputTransition"],                                       parent_ids_dict["Operon"],                                       input_trans_logic)
     
            ###sbml output transition file creation
            make_output_transition_sbml_file(output_species_list,                                     parent_ids_dict["OutputTransition"],                                     parent_ids_dict["Operon"])
            
            input_species_list = []
            output_species_list = []
            promoter_list = []    
            
        ###Capturing the previous operon's direction for sbol    
        elif component_keyword == "Operon" and len(output_species_list) == 0:            
            prev_operon_direction = component_data[:-1:][0]
            
        ###Capturing the input transition logic for sbml
        if component_keyword == "InputTransition":
            input_trans_logic = component_data[0]
   
            
        #Update the database exclusively except for 4th level conditions      
        if component_keyword != "Plasmid":
            
            #Covering the insert for input transitions, operons, and output transitions 
            if component_keyword in ["InputTransition", "Operon", "OutputTransition"]:    
                parent_keyword = determine_parent_keyword(component_keyword)
                parent_id = parent_ids_dict[parent_keyword]
                component_id = determine_and_insert(connection, cursor, component_keyword, component_data, parent_id)
                parent_ids_dict[component_keyword] = component_id
                
            #keeping track of output and input transition information that will be used for the sbol image and as 
            #as well as input and output transition sbml txt. 
            elif component_keyword in ["InputSpecies", "OutputSpecies", "Promoter"]:
                #component_id = determine_and_insert(connection, cursor, component_keyword, component_data)
            
                if component_keyword == "InputSpecies":
                    input_species = list(component_data) + [component_id]
                    input_species_list.append(input_species)
                    parent_keyword = determine_parent_keyword(component_keyword)
                    parent_id = parent_ids_dict[parent_keyword]                    
                    component_id = determine_and_insert(connection, cursor, component_keyword, component_data, parent_id)
                    
                elif component_keyword == "OutputSpecies":
                
                    ###Capturing the outputtransion
                    if len(output_species_list) == 0:
                        parent_id = parent_ids_dict["Operon"]
                        component_id = determine_and_insert(connection, cursor, "OutputTransition", [], parent_id)
                        parent_ids_dict["OutputTransition"] = component_id
                        
                        
                    output_species = list(component_data) + [component_id]
                    output_species_list.append(output_species)
                    parent_keyword = determine_parent_keyword(component_keyword)
                    parent_id = parent_ids_dict[parent_keyword]
                    component_id = determine_and_insert(connection, cursor, component_keyword, component_data, parent_id)

                else:
                    promoter_list.append( "p" + component_data[0])
        else:
            plasmid_id = determine_and_insert(connection, cursor, component_keyword, component_data)
            parent_ids_dict["Plasmid"] = plasmid_id
            

    ###Covering the last sbol that has to be created. It would be skipped over becasue it is the last one otherwise. 
    sbol_files.append(make_sbol_file(output_species_list,                      promoter_list,                      prev_operon_direction,                      parent_ids_dict["Operon"]))
    
    make_input_transition_sbml_file(input_species_list,                               parent_ids_dict["InputTransition"],                               parent_ids_dict["Operon"],                               input_trans_logic)
    
    make_output_transition_sbml_file(output_species_list,                                     parent_ids_dict["OutputTransition"],                                     parent_ids_dict["Operon"])

   
       
    connection.commit()
    return ",".join(sbol_files)

def main():
    device_info = sys.argv[1::]
    conn, cur = db.db_open("sbider_test_2.db")
    sbol_files = insert_new_device(conn, cur, device_info)
    sg.create_json_whole_network_file("whole_network.json", cur)
    db.db_close(conn,cur)
    gn.create_whole_network_sbml()

    return sbol_files        

#reset_db()  
if __name__ == "__main__":
    main()

