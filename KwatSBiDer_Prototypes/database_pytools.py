import sqlite3
import math
import itertools as it

def list_is_type(lst, typ):
    if type(lst) != list:
        raise TypeError("lst is not a list")
    return all(isinstance(x,typ) for x in lst)



def uniquely_merge_list_of_lists(list_of_lists):
    """
    Merge unique elements from lists within a list.
    
    Argument:
        list_of_lists - a list that contains multiple lists.
    
    Return:
        a new list that contains unique elements from all lists within a list of lists.
    """
    ###print "uniquely_merge_list_of_lists(list_of_lists): list_of_lists: ", list_of_lists
    
    if type(list_of_lists) == list and len(list_of_lists) > 0 and list_is_type(list_of_lists, list) == True:
        merged_list = list(list_of_lists[0])
        for a_list in list_of_lists[1::]:
                for e in a_list:
                    if e not in merged_list:
                        merged_list.append(e)
        return merged_list
    else:
        raise TypeError("uniquely_merge_list_of_lists(list_of_lists): list_of_lists should be in the form: [[],[],... ]")



def uniquely_merge_multiple_list_of_lists(list_of_lists_of_lists):
    
    if type(list_of_lists_of_lists) == list and len(list_of_lists_of_lists) > 0 and list_is_type(list_of_lists_of_lists, list) == True:
        merged_list_of_lists = []
        for a_list_of_lists in list_of_lists_of_lists:
            
            ###print "uniquely_merge_multiple_list_of_lists(list_of_lists_of_lists): a_list_of_lists: ", a_list_of_lists
            
            
            a_merged_list_of_lists = uniquely_merge_list_of_lists(a_list_of_lists)
            for e in a_merged_list_of_lists:
                if e not in merged_list_of_lists:
                    merged_list_of_lists.append(e)
        return merged_list_of_lists
    else:
        raise TypeError("uniquely_merge_multiple_list_of_lists(list_of_lists_of_lists): list_of_lists_of_lists should be in the form: [[[]],[[]],... ]")



def elements_match(list_of_lists, lst):
    return set(lst).issubset(uniquely_merge_list_of_lists(list_of_lists))



def get_matching_list(list_of_lists, lst):
    """
    Get any list that match a specified list.
    """
    if type(lst) != list:
        raise TypeError("get_matching_list(list_of_lists, lst): lst is not a list object")    
    elif type(list_of_lists) == list and len(list_of_lists) > 0 and list_is_type(list_of_lists, list) == True:
            
        ###print "get_matching_list(...): list_of_lists - lst:", list_of_lists, " - ", lst

        matching_list = []
        for a_list in list_of_lists:

            ###print a_list

            if all([x in lst for x in a_list]) == True:
                matching_list.append(a_list)
        return matching_list
    else:
        raise TypeError("get_matching_list(list_of_lists, lst): list_of_lists should be in the form: [[],[],... ]")



def match_any_list(list_of_lists, lst):
    """
    Check if a list matches any of lists within a list.
    """
        
    ###print "match_any_list(...): list_of_lists - lst:", list_of_lists, " - ", lst
    
    if get_matching_list(list_of_lists, lst) == []:
        return False
    else:
        return True



def reverse_index(sequence, element):
    """
    Find the last index of an element in a sequence.
    """

    for i, e in enumerate(reversed(sequence)):
        if element == e:
            return len(sequence) - 1 - i
    else:
        raise ValueError("r_index(sequence, element): element not in the sequence")



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


def split_by(sequence, element):
    """
    Split a sequence by a given element and store elements
    before and after the element into a dictionary
    """
    
    element_index = sequence.index(element)
    
    sequence_before_element = sequence[:element_index:1]
    sequence_after_element = sequence[element_index + 1::1]
    
    return {0: sequence_before_element, 1: sequence_after_element}


def format_values(value_list):
    
    formatted_value_list = []
    for value in value_list:
        if isinstance(value, unicode):
            formatted_value_list.append(str(value))
        elif math.isnan(value):
            formatted_value_list.append("na")
        else:
            formatted_value_list.append(value)
    return formatted_value_list


def db_open(database_file):
    """
    Connect to a database or create a database if it does not already
    exist.
    """
    # delete all .db files in current directory
    
    connection = sqlite3.connect(database_file)
    connection.text_factory = str
    cursor = connection.cursor()
    return connection, cursor



def db_close(connection, cursor):
    """Close a database."""
    
    connection.commit()
    cursor.close()



def make_sql_insert_command(table_name, table_header_list, insert_data_list):
    '''Make SQL insert command.'''
    
    ###print "insert_data_list:", insert_data_list
    insert_data_list_formatted = list(insert_data_list)
    ###print "insert_data_list_formatted:", insert_data_list_formatted
    
    sql_insert_into = 'INSERT INTO ' + table_name
    ###print "sql_insert_into:", sql_insert_into
    
    sql_insert_header = '(' + ','.join(table_header_list) + ')'
    ###print "sql_insert_header:", sql_insert_header
    
    for index in range(len(insert_data_list_formatted)):
        if isinstance(insert_data_list_formatted[index], str):
            insert_data_list_formatted[index] = "'" + insert_data_list_formatted[index] + "'"  
        else:
            insert_data_list_formatted[index] = str(insert_data_list_formatted[index])      
                                            
    sql_values = 'Values (' + ','.join(insert_data_list_formatted) + ')'
    ###print "sql_values:", sql_values
    
    sql_insert_command = sql_insert_into + '\n\t' + sql_insert_header + '\n\t' + sql_values + ';'
    ###print "sql_insert_command:", sql_insert_command
    
    return sql_insert_command

def make_sql_select_command(table_name, table_header_list, where_columns = None, where_options = None,
    where_values = None, where_bools = None, group = None, having_columns = None, having_bools = None, 
    having_values = None):
    '''Make SQL select command.
    
    @param table_header_list - list of columns to be selected
    @param where_columns - column names for where clause
    @param where_options - operator for where clause
    @param where_values - variable for where clause 
    @param where_bools - boolean for where clause
    @param group - group name for GROUP BY caluse
    @param having_columns'''
    
    # check whether argument is valid or not
    # all the where_variables must be all None or same size where_bool is less by 1
    if (where_columns is not None and where_options is not None and where_values is not None and where_bools is not None):
        if (len(where_columns) != len(where_options) and len(where_options) != len(where_values) and len(where_values) != (len(where_bools) - 1)):
            raise Exception("Invalid argument")
    elif(where_columns is not None or where_options is not None or where_values is not None or where_bools is not None):
            raise Exception("Invalid argument")

    # must have a table name
    if ( table_name is None or len(table_name) == 0):
	raise Exception("a table name must be provided.")

    sql_select_command = "SELECT "
    if table_header_list == "*":
	sql_select_command += " * "
    else:
	for table_header_index in range(len(table_header_list)):
	    sql_select_command += table_header_list[table_header_index]
	    if (table_header_index != len(table_header_list) - 1):
		sql_select_command += ", "
	    else:
		sql_select_command += " "
    sql_select_command += "\n" + "FROM " + table_name + " "

    if where_columns is not None :
	sql_select_command += "\n"+"WHERE "
	for where_index in range(len(where_columns)):

	    ###print "where_index:", where_index

	    sql_select_command += where_columns[where_index] + " " + where_options[where_index] + " " + str(where_values[where_index]) + " "
	    if where_index < len(where_bools):
		sql_select_command += where_bools[where_index] + " "

    if group is not None:
	sql_select_command += "\n" + "GROUP BY " + group

    if having_columns is not None and having_bools is not None and having_values is not None:
	sql_select_command += "\n" + "HAVING " + having_columns + " " +  having_bools + " " + str(having_values)
    sql_select_command +=";"

    return sql_select_command



def make_sql_update_command(table_name, table_header_list, update_data_list, where_column = "", 
                            where_option = "", where_value = ""):
    """Makes SQL update command
    @param table_name - Updating table
    @param table_header_list - Selected columns
    @param where_columns - Where column names
    @param where_options - List of operators
    @param where_values - variable for where clause 
    @param where_bools - boolean for where clause"""
    
    sql_update = 'UPDATE ' + table_name
    
    update_values_list = []
    for column_name, update_value in zip(table_header_list, update_data_list):
        #print "column_name, update_value:", column_name, update_value
        update_values_list.append(str(column_name) + ' = ' + str(update_value))
        
    ###print "\nfilled update_values_list:", update_values_list
    '''for item in update_values_list:
        print item
    '''
        
    sql_update_values = 'SET ' + ', '.join(update_values_list)
    
    ###print "\nsql_update_values:", sql_update_values
    '''for item in sql_update_values:
        print item
    '''
    
    sql_where = ""
    if where_column != "":
        sql_where = "\n" + " ".join(['WHERE', where_column, where_option, where_value])
    
    '''for where_column_name, where_value , where_op, index in 
            zip(where_columns, where_values, where_options, range(len(where_columns) + 1)):
            if i < len(where_columns) - 1:
                hold = sql_where + ' '.join([where_column_name,where_option,str(where_value)]) + ' ' + w_conts[index]
            else:
                hold = sql_where + ' '.join([where_column_name,where_option,str(where_value)]) + ' ' 
            sql_where = hold 
        return update_command + '\n\t' + set_str + '\n\t' + where_str + ';'''
    
    
    sql_update_command  = sql_update + "\n" + sql_update_values + sql_where + ";"
    
    ###print "update_command:\n", sql_update_command
    
    return sql_update_command



def make_sql_delete_command(table_name):
    sql_delete_command = "DELETE FROM %s;" % table_name
    return sql_delete_command



def make_sql_drop_command(table_name):
    sql_drop_command = "DROP TABLE %s;" % table_name
    return sql_drop_command



def db_create_table(cursor):
    """Make tables for sbider.db"""
    
    ###db_drop_all_table(cursor)

    species = '''CREATE TABLE Species (spe_id VARCHAR(50), 
                                       name VARCHAR(50), 
                                       type VARCHAR(50));'''
    
    plasmid = '''CREATE TABLE Plasmid (pla_id VARCHAR(50), 
                                       name VARCHAR(50), 
                                       miriam_id VARCHAR(50));'''
    
    operon = '''CREATE TABLE Operon (ope_id VARCHAR(50), 
                                     name VARCHAR(50),
                                     image VARCHAR(50));'''
    
    po = '''CREATE TABLE PlasmidOperon (ope_id VARCHAR(50), 
                                        pla_id VARCHAR(50),
                                        direction VARCHAR(50));'''
    
    oit = '''CREATE TABLE OperonInputTransition (it_id VARCHAR(50), 
                                                 ope_id VARCHAR(50));'''
    
    it = '''CREATE TABLE InputTransition (it_id VARCHAR(50), 
                                          logic VARCHAR(50));'''
    
    in_ = '''CREATE TABLE InputTransitionSpecies (in_id VARCHAR(50), 
                                                  it_id VARCHAR(50), 
                                                  spe_id VARCHAR(50),
                                                  reverse BOOL);'''
    
    oot = '''CREATE TABLE OperonOutputTransition (ot_id VARCHAR(50),
                                                  ope_id VARCHAR(50));'''
    
    ot = '''CREATE TABLE OutputTransition (ot_id VARCHAR(50), 
                                           logic VARCHAR(50))'''
    
    out = '''CREATE TABLE OutputTransitionSpecies (out_id VARCHAR(50), 
                                                   ot_id VARCHAR(50),
                                                   spe_id VARCHAR(50));'''
    
    login = '''CREATE TABLE User (user_id VARCHAR(50), 
                                  first_name VARCHAR(50),
                                  last_name VARCHAR(50),
                                  email VARCHAR(50),
                                  password VARCHAR(50));'''
    
    table_list =[species,plasmid, operon, po, oit, it, in_, oot, ot, out, login]
    for table in table_list:        
        cursor.execute(table)
    return cursor



def db_drop_table(cursor, table_name):
    """Drop a table."""
    
    sql_drop_command = make_sql_drop_command(table_name)
    cursor.execute(sql_drop_command)
    return cursor



def db_drop_all_table(cursor):
    """Drop all tables."""
    
    table_name_list = ["Species", 
                       "Plasmid", 
                       "Operon", 
                       "PlasmidOperon", 
                       "OperonInputTransition", 
                       "InputTransition", 
                       "InputTransitionSpecies", 
                       "OperonOutputTransition", 
                       "OutputTransition", 
                       "OutputTransitionSpecies", 
                       "User"]
    
    ###print "table_name_list", table_name_list
    
    for table_name in table_name_list:
        
        sql_drop_command = make_sql_drop_command(table_name)
    
        cursor.execute(sql_drop_command)
    
    return cursor



def db_print_table(cursor, table_name):
    """Print a table."""
    
    cursor.execute("SELECT * FROM " + table_name)
    rows = cursor.fetchall()
    for row in rows:
        print row



def db_print_all_table(cursor):
    """Print all table."""
    
    db_print_table(cursor, "Species")
    db_print_table(cursor, "Plasmid")
    db_print_table(cursor, "Operon")
    db_print_table(cursor, "PlasmidOperon")
    db_print_table(cursor, "OperonInputTransition")
    db_print_table(cursor, "InputTransition")
    db_print_table(cursor, "InputTransitionSpecies")
    db_print_table(cursor, "OperonOutputTransition")
    db_print_table(cursor, "OutputTransition")
    db_print_table(cursor, "OutputTransitionSpecies")
    db_print_table(cursor, "User")



def db_get_species_id_from_name(cursor, species_name):
    a_cur = db_select(cursor, 
                      "Species",
                      ["spe_id"], 
                      ["name"], 
                      ["="], 
                      ["'%s'" % species_name.lower()], 
                      "")
    return a_cur.fetchone()[0]



def db_get_species_name_from_id(cursor, species_id):
    a_cur = db_select(cursor, 
                     "Species",
                     ["name"], 
                     ["spe_id"], 
                     ["="], 
                     [species_id], 
                     "")
    return a_cur.fetchone()[0]



def db_get_operon_id_from_name(cursor, operon_name):
   a_cur = db_select(cursor, 
                     "Operon",
                     ["ope_id"], 
                     ["name"], 
                     ["="], 
                     ["'%s'" % operon_name], 
                     "")
   return a_cur.fetchone()[0]



def db_get_operon_name_from_id(cursor, operon_id):
   a_cur = db_select(cursor, 
                    "Operon",
                    ["name"], 
                    ["ope_id"], 
                    ["="], 
                    [operon_id], 
                    "")
   return a_cur.fetchone()[0]



def db_get_plasmid_id_from_name(cursor, plasmid_name):
   a_cur = db_select(cursor, 
                     "Plasmid",
                     ["pla_id"], 
                     ["name"], 
                     ["="], 
                     ["'%s'" % plasmid_name.lower()], 
                     "")
   return a_cur.fetchone()[0]



def db_get_plasmid_name_from_id(cursor, plasmid_id):
   a_cur = db_select(cursor, 
                    "Plasmid",
                    ["name"], 
                    ["pla_id"], 
                    ["="], 
                    [plasmid_id], 
                    "")
   return a_cur.fetchone()[0]



def db_select(cursor, table_name, table_header_list, where_columns = None, where_options = None,
    where_values = None,where_bools = None, group = None, having_columns = None, having_bools = None, 
    having_values = None):
    """
    Select from a table.
    
    Argument(s):
        table_name: table you wish to pull data from
        col_names: list of numbers indexing the table columns
        w_col: column names for where clause
        w_opt: operator for where clause
        w_var: variable for where clause 
        w_bool: boolean for where clause
        group: group name for GROUP BY caluse
        h_col: group specifier
        
    Return:
        
    """
    
    sql_command = make_sql_select_command(table_name, table_header_list, where_columns, where_options,
    where_values,where_bools, group, having_columns, having_bools, having_values)
    
    ###print "db_select(...) sql_command:", sql_command
    
    cursor.execute(sql_command)
    
    return cursor



def db_insert(cursor, table_name, table_header_list, insert_data_list):
    """Insert into a table.
    
    Args:
        table_name, that table that you wish to insert into
        cols, the columns that you want to insert into
        new_row, the values that correspond to the columns
    
    Examples:
        ex 1. Inserting into plasmid table and filling in all the columns. 
    """
    
    sql_command = make_sql_insert_command(table_name, table_header_list, insert_data_list)
    
    ###print "db_insert(...) sql_command", sql_command
    
    cursor.execute(sql_command)
    
    return cursor



def db_update(cursor, table_name, table_header_list, update_data_list, 
    where_column = "", where_option = "", where_value = ""):
    """Update."""
    
    sql_command = make_sql_update_command(table_name, table_header_list, update_data_list, 
        where_column, where_option, where_value)
    
    print "sql_command:", sql_command
    
    cursor.execute(sql_command)
    
    return cursor



def db_delete(cursor, table_name):
    cursor.execute(make_sql_delete_command(table_name))



def db_custom(cursor, sql_command):
    """Do whatever."""
    cursor.execute(sql_command)
    
    return cursor



def get_all_input_transition_species(cursor, input_transition_id):
    species_list = []
    species_list_unformatted = db_select(cursor, "InputTransitionSpecies", ["spe_id"], ["it_id"], ["="], ["'" + input_transition_id + "'"], [""])
    species_list_unformatted = species_list_unformatted.fetchall()
    
    ###print "species_list_unformatted:", species_list_unformatted
    
    for species_index in range(len(species_list_unformatted)):
        species_list.append(list(species_list_unformatted[species_index]))
        
    #print "(before) species_list:", species_list

    species_list = uniquely_merge_list_of_lists(species_list)
    
    #print "(after) species_list:", species_list
    
    return species_list



def get_all_output_transition_species(cursor, input_transition_id):
    species_list = []
    species_list_unformatted = db_select(cursor, "OutputTransitionSpecies", ["spe_id"], ["ot_id"], ["="], ["'" + input_transition_id + "'"], [""])
    species_list_unformatted = species_list_unformatted.fetchall()
    
    ###print "species_list_unformatted:", species_list_unformatted

    for species_index in range(len(species_list_unformatted)):
        species_list.append(list(species_list_unformatted[species_index]))
    
    #print "(before) species_list:", species_list

    species_list = uniquely_merge_list_of_lists(species_list)
    
    #print "(after) species_list:", species_list
        
    return species_list



def get_subnetwork(cursor, species_paths_list, operon_paths_list, input_transitions_paths_list, output_transitions_paths_list):
    
    #subnetwork = get_path(input_dictionary, output_dictionary, input_species_list, output_species_list)
    
    """Collecting subnetwork information."""
    # operon_paths_list, input_transitions_paths_list,\
    # output_transitions_paths_list, species_paths_list = get_path()

    # Operon Nodes Validation Done
    operon_ids_list = uniquely_merge_list_of_lists(operon_paths_list)
    operon_nodes_list = []
    for operon_id in operon_ids_list:
        operon_node = db_select(cursor,"Operon", ['ope_id', 'name', 'image'], ['ope_id'], ['='], [ "'" + operon_id + "'"], [""])
        operon_node = list(operon_node.fetchone())
        operon_node[0] = "ope_" + operon_node[0]
        operon_nodes_list.append(operon_node)
    
    # Species Nodes Validation Done
    species_ids_list = uniquely_merge_list_of_lists(species_paths_list)
    species_nodes_list = []
    for species_id in species_ids_list:
        
        #print "species_id:", species_id
        
        species_node = db_select(cursor, "Species", ['spe_id', 'name', 'type'], ['spe_id'], ['='], ["'" + species_id + "'"], [""])
        species_node = list(species_node.fetchone())
        species_node[0] = "spe_" + species_node[0]
        
        #print "species_node_id_abbreviated:", species_node
        
        species_nodes_list.append(species_node)
        
    # Input Transitions Validation Done
    input_transitions_id_list = uniquely_merge_list_of_lists(input_transitions_paths_list)
    input_transitions_nodes_list = []
    for input_transition_id in input_transitions_id_list:
        input_transitions_node = db_select(cursor,"InputTransition", ['it_id', 'logic'], ['it_id'], ['='], ["'" + input_transition_id + "'"], [""])
        input_transitions_node = list(input_transitions_node.fetchone())
        input_transitions_node[0] = "it_" + input_transitions_node[0]
        input_transitions_nodes_list.append(input_transitions_node)
        
    # Output Transitions Validation Done    
    output_transitions_id_list = uniquely_merge_list_of_lists(output_transitions_paths_list)
    output_transitions_nodes_list = []
    for output_transition_id in output_transitions_id_list:
        #output_transition_node = db_select(cursor,"OutputTransition", ['ot_id'], ['ot_id'], ['='], ["'" + output_transition_id + "'"], [""])
        #output_transition_node = list(output_transition_node.fetchone())
        #output_transitions_node_list.append(output_transitions_node)
        output_transitions_nodes_list.append(["ot_" + output_transition_id])
        
        
    source_id_target_id_list = []
    
    # operon_paths_list, input_transitions_paths_list,\
    # output_transitions_paths_list, species_paths_list
    
    for operon_path, input_transition_path, output_transition_path in    zip(operon_paths_list, input_transitions_paths_list, output_transitions_paths_list):

        for operon_id, input_transition_id, output_transition_id in zip(operon_path, input_transition_path, output_transition_path):

            #print "input_transition:", input_transition_id

            # adding all input_transition_species edges
            input_transition_species = get_all_input_transition_species(cur, input_transition_id)
            for species_id in input_transition_species:

                ###print "input_transition, species_id:", input_transition_id, ",",species_id

                source_id_target_id_list.append(["spe_" + species_id, "it_" + input_transition_id])

            #adding all input_transition_operon edges
            source_id_target_id_list.append(["it_" + input_transition_id, "ope_" + operon_id])

            #adding all output_transition_operon edges
            source_id_target_id_list.append(["ope_" + operon_id, "it_" + input_transition_id])

            #adding all output_transition_species edges
            output_transition_species = get_all_output_transition_species(cur, input_transition_id)
            for species_id in output_transition_species:

                ###print "output_transition, species_id:", output_transition_id, ",", species_id

                source_id_target_id_list.append(("ot_" + output_transition_id, "spe_" + species_id))
        
    
    return operon_nodes_list, species_nodes_list, input_transitions_nodes_list, output_transitions_nodes_list, source_id_target_id_list

















def make_input_ope_id_spe_id_dict(sql):
    input_ope_id_spe_id_dict = {}

    merged_ope_it_spe = sql.execute('''SELECT OperonInputTransition.ope_id, 
                                              OperonInputTransition.it_id,
                                              InputTransitionSpecies.spe_id 
                                              FROM   OperonInputTransition,
                                              InputTransitionSpecies 
                                              WHERE  OperonInputTransition.it_id = InputTransitionSpecies.it_id''')

    ###print "merged_ope_it_spe:", merged_ope_it_spe
    ###print "merged_ope_it_spe.fetchall():", merged_ope_it_spe.fetchall()
    ###print "merged_ope_it_spe.fetchone():", merged_ope_it_spe.fetchone()

    previous_operon, previous_input_transition, previous_species = merged_ope_it_spe.fetchone()

    ###print 'previous_operon, previous_input_transition, previous_species:\t',previous_operon,"",previous_input_transition,"",previous_species

    input_transition_list_idx = 0

    ###print 'input_transition_list_idx', input_transition_list_idx

    input_ope_id_spe_id_dict[previous_operon] = [[]]

    input_ope_id_spe_id_dict[previous_operon][input_transition_list_idx].append(previous_species.strip())

    ###print "input_operon_species_dictionary:",input_operon_species_dictionary

    for operon, input_transition, species in merged_ope_it_spe.fetchall():
        
        ###print "\toperon, input_transition, species:\t", operon, "", input_transition, "", species

        if operon == previous_operon:

            if input_transition == previous_input_transition:

                input_ope_id_spe_id_dict[operon][input_transition_list_idx].append(species.strip())

                ###print "\n\n\tinput_operon_species_dictionary:",input_operon_species_dictionary

            elif input_transition != previous_input_transition:
                input_transition_list_idx = input_transition_list_idx + 1

                input_ope_id_spe_id_dict[operon].append([])
                input_ope_id_spe_id_dict[operon][input_transition_list_idx].append(species.strip())

                previous_input_transition = input_transition

        else:
            input_transition_list_idx = 0
            input_ope_id_spe_id_dict[operon] = [[]]
            input_ope_id_spe_id_dict[operon][input_transition_list_idx].append(species.strip())

            previous_operon = operon
            previous_input_transition = input_transition
    
    return input_ope_id_spe_id_dict




def make_output_ope_id_spe_id_dict(sql):
    output_ope_id_spe_id_dict = {}

    merged_ope_ot_spe = sql.execute('''SELECT OperonOutputTransition.ope_id, 
                                       OperonOutputTransition.ot_id,
                                       OutputTransitionSpecies.spe_id 
                                       FROM   OperonOutputTransition,
                                       OutputTransitionSpecies 
                                       WHERE  OperonOutputTransition.ot_id = OutputTransitionSpecies.ot_id''')

    ###print "merged_ope_ot_spe:", merged_ope_ot_spe
    ###print "merged_ope_ot_spe.fetchall():", merged_ope_ot_spe.fetchall()
    ###print "merged_ope_ot_spe.fetchone():", merged_ope_ot_spe.fetchone()
    
    # previous ope_id, ot_id, and spe_id
    previous_operon, previous_output_transition, previous_species = merged_ope_ot_spe.fetchone()

    ###print 'previous_operon, previous_output_transition, previous_species:\t',previous_operon,"",previous_output_transition,"",previous_species

    output_transition_list_idx = 0

    ###print 'output_transition_list_idx', output_transition_list_idx

    output_ope_id_spe_id_dict[previous_operon] = [[]]
    output_ope_id_spe_id_dict[previous_operon][output_transition_list_idx].append(previous_species.strip())

    ###print "output_operon_species_dictionary:", output_operon_species_dictionary

    # ope_id, ot_id, and spe_id
    for operon, output_transition, species in merged_ope_ot_spe.fetchall():
        
        ###print "\toperon, output_transition, species:\t", operon, " ", output_transition, " ", species

        if operon == previous_operon and not elements_match(output_ope_id_spe_id_dict[operon], [species]):            
            if output_transition == previous_output_transition:
                output_ope_id_spe_id_dict[operon][output_transition_list_idx].append(species.strip())                
            else:
                output_transition_list_idx = output_transition_list_idx + 1
                output_ope_id_spe_id_dict[operon].append([])
                output_ope_id_spe_id_dict[operon][output_transition_list_idx].append(species.strip())
        else:
            output_transition_list_idx = 0
            output_ope_id_spe_id_dict[operon] = [[]]
            output_ope_id_spe_id_dict[operon][output_transition_list_idx].append(species.strip())
        
            previous_operon = operon
            previous_output_transition = output_transition  
        
    return output_ope_id_spe_id_dict
def make_ope_id_spe_id_dicts(cursor):
    return make_input_ope_id_spe_id_dict(cursor), make_output_ope_id_spe_id_dict(cursor)



def make_plasmid_species_name_dictionary(cursor, operon_id_plasmid_name_dictionary, operon_species_dictionary):
    plasmid_species_name_dictionary = {}
    for operon_id, species_id_list in operon_species_dictionary.items():
            uniquely_merge_spe_id_list = uniquely_merge_list_of_lists(species_id_list)
            plasmid_name = operon_id_plasmid_name_dictionary[operon_id]
            plasmid_species_name_dictionary[plasmid_name] =\
                [db_get_species_name_from_id(cursor, spe_id) for spe_id in uniquely_merge_spe_id_list]
    return plasmid_species_name_dictionary





def make_pla_name_spe_name_dicts(cursor):
    
    plasmid_name_input_species_name_dictionary = {}
    plasmid_name_output_species_name_dictionary = {}
    
    operon_id_plasmid_name_dictionary = {}
    species_id_to_name_dictionary = {}

    input_operon_species_dictionary, output_operon_species_dictionary = make_ope_id_spe_id_dicts(cursor)
        
        
    # make operon_id plasmid_name dictionary
    merged_ope_id_pla_name = cursor.execute('''SELECT PlasmidOperon.ope_id,
                                                   Plasmid.name
                                            FROM PlasmidOperon,
                                                 Plasmid
                                            WHERE PlasmidOperon.pla_id = Plasmid.pla_id''')
    for ope_id, pla_name in merged_ope_id_pla_name.fetchall():
        operon_id_plasmid_name_dictionary[ope_id] = pla_name
        
    input_plasmid_species_name_dictionary = make_plasmid_species_name_dictionary(cursor,
                                                                                 operon_id_plasmid_name_dictionary,
                                                                                 input_operon_species_dictionary)
    output_plasmid_species_name_dictionary = make_plasmid_species_name_dictionary(cursor,
                                                                                  operon_id_plasmid_name_dictionary,
                                                                                  output_operon_species_dictionary)
    return input_plasmid_species_name_dictionary, output_plasmid_species_name_dictionary
