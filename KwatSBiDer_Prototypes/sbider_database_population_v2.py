
# coding: utf-8

# In[1]:

import sqlite3
import subprocess
import math
import pandas as pd
import itertools as it
import matplotlib.pyplot as plt
import networkx as nx


# In[2]:

def extend_list_of_lists(list_of_lists):
    """Extend lists within a list."""
    
    extended_list = []
    for lst in list_of_lists:
        extended_list.extend(lst)
    return list(set(extended_list))


# In[3]:

def format_values(value_list):
    """Convert list values into accessible types."""
    formatted_value_list = []
    for value in value_list:
        if isinstance(value, unicode):
            
            #print 'value unicode (before):', value
            
            formatted_value_list.append(str(value))
            
            #print 'value unicode (before):', value
            
        elif math.isnan(value):
            
            #print 'value nan (before):', value
            
            formatted_value_list.append("na")

        else:
            formatted_value_list.append(value)
            
    #print 'formatted_value_list:', formatted_value_list 
    
    return formatted_value_list


# In[4]:

def db_open(database_file):
    '''Connect to a database or create a database if it does not already
    exist.'''
    
    #subprocess.call(["rm", "-r", "*.db"])

    connection = sqlite3.connect(database_file)
    connection.text_factory = str
    cursor = connection.cursor()
    
    return connection, cursor


# In[5]:

def db_close(connection, cursor):
    """Close a database."""
    
    connection.commit()
    cursor.close()


# In[6]:

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
    
    ###print "sql_command:", sql_command
    
    return sql_insert_command


# In[4]:

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
    if table_header_list == "*":
        return "SELECT * FROM " + table_name
    
    else:
        # check whether argument is valid or not
        # all the where_variables must be all None or same size where_bool is less by 1
        if (where_columns is not None and where_options is not None and where_values is not None         and where_bools is not None):
            if (len(where_columns) != len(where_options) and len(where_options) != len(where_values)            and len(where_values) != (len(where_bools) - 1)):
                raise Exception("Invalid argument")
        elif(where_columns is not None or where_options is not None or where_values is not None          or where_bools is not None):
                raise Exception("Invalid argument")

        # must have a table name
        if ( table_name is None or len(table_name) == 0):
            raise Exception("a table name must be provided.")

        sql_select_command = "SELECT "

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


# In[8]:

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


# In[9]:

def make_sql_delete_command(table_name):
    sql_delete_command = "DELETE FROM %s;" % table_name
    return sql_delete_command


# In[10]:

def make_sql_drop_command(table_name):
    
    sql_drop_command = "DROP TABLE %s;" % table_name
    
    return sql_drop_command


# In[11]:

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
    
    table_list =[species,plasmid, 
                 operon, 
                 po, 
                 oit, 
                 it, 
                 in_, 
                 oot, 
                 ot, 
                 out, 
                 login]
    
    for table in table_list:        
        cursor.execute(table)
        
    return cursor


# In[12]:

def db_drop_table(cursor, table_name):
    """Drop a table."""
    
    sql_drop_command = make_sql_drop_command(table_name)
    
    cursor.execute(sql_drop_command)
    
    return cursor


# In[13]:

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


# In[14]:

def db_print_table(cursor, table_name):
    """Print a table."""
    
    cursor.execute("SELECT * FROM " + table_name)
    rows = cursor.fetchall()
    for row in rows:
        print row


# In[15]:

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


# In[16]:

def db_get_species_id_from_name(cursor, species_name):
    a_cur = db_select(cursor, 
                      "Species",
                      ["spe_id"], 
                      ["name"], 
                      ["="], 
                      ["'%s'" % species_name.lower()], 
                      "")
    return a_cur.fetchone()[0]


# In[17]:

def db_get_species_name_from_id(cursor, species_id):
    a_cur = db_select(cursor, 
                     "Species",
                     ["name"], 
                     ["spe_id"], 
                     ["="], 
                     [species_id], 
                     "")
    return a_cur.fetchone()[0]


# In[18]:

def db_get_operon_id_from_name(cursor, operon_name):
   a_cur = db_select(cursor, 
                     "Operon",
                     ["ope_id"], 
                     ["name"], 
                     ["="], 
                     ["'%s'" % operon_name], 
                     "")
   return a_cur.fetchone()[0]


# In[19]:

def db_get_operon_name_from_id(cursor, operon_id):
   a_cur = db_select(cursor, 
                    "Operon",
                    ["name"], 
                    ["ope_id"], 
                    ["="], 
                    [operon_id], 
                    "")
   return a_cur.fetchone()[0]


# In[20]:

def db_get_plasmid_id_from_name(cursor, plasmid_name):
   a_cur = db_select(cursor, 
                     "Plasmid",
                     ["pla_id"], 
                     ["name"], 
                     ["="], 
                     ["'%s'" % plasmid_name.lower()], 
                     "")
   return a_cur.fetchone()[0]


# In[21]:

def db_get_plasmid_name_from_id(cursor, plasmid_id):
   a_cur = db_select(cursor, 
                    "Plasmid",
                    ["name"], 
                    ["pla_id"], 
                    ["="], 
                    [plasmid_id], 
                    "")
   return a_cur.fetchone()[0]


# In[22]:

def db_select(cursor, table_name, table_header_list, where_columns = None, where_options = None,
    where_values = None,where_bools = None, group = None, having_columns = None, having_bools = None, 
    having_values = None):
    """Select from a table.
    Args:
        table_name: table you wish to pull data from
        col_names: list of numbers indexing the table columns
        w_col: column names for where clause
        w_opt: operator for where clause
        w_var: variable for where clause 
        w_bool: boolean for where clause
        group: group name for GROUP BY caluse
        h_col: group specifier
    """
    
    sql_command = make_sql_select_command(table_name, table_header_list, where_columns, where_options,
    where_values,where_bools, group, having_columns, having_bools, having_values)
    
    ###print "db_select(...) sql_command:", sql_command
    
    cursor.execute(sql_command)
    
    return cursor


# In[23]:

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


# In[24]:

def db_update(cursor, table_name, table_header_list, update_data_list, 
    where_column = "", where_option = "", where_value = ""):
    """Update."""
    
    sql_command = make_sql_update_command(table_name, table_header_list, update_data_list, 
        where_column, where_option, where_value)
    
    print "sql_command:", sql_command
    
    cursor.execute(sql_command)
    
    return cursor


# In[25]:

def db_delete(cursor, table_name):
    cursor.execute(make_sql_delete_command(table_name))


# In[26]:

def db_custom(cursor, sql_command):
    """Do whatever."""
    cursor.execute(sql_command)
    
    return cursor


# In[2]:

conn, cur = db_open("sbider_fixing.db")
source_data = pd.io.excel.read_excel(
'/Users/K/Desktop/sbider_project/sbider_excel/sbider_database_09212014.xlsx','database')
db_create_table(cur)


# In[ ]:

def db_populate_species(cursor, sbider_data):
    
    db_delete(cursor, "Species")
    
    domain = sbider_data[['Domain']]
    range_ = sbider_data[['Range']]
    
    ###print "domain:\n\n", domain
    ###print "range_:\n\n", range_
    ###print "domain list\n:", domain.values.T.tolist()[0]
    ###print "range list\n:", range_.values.T.tolist()[0]
    
    species = set(domain.values.T.tolist()[0] + range_.values.T.tolist()[0])
        
    inserted_species_set = set([])
    
    count = 1
    
    for row in species:
        
        ###print "row:", row
        
        row = format_values([row])
        
        ###print "row after format:", row
        ###print "row[0]:",row[0]
        
        # list to string, and split by comma
        split_row = row[0].split(',')
        
        ###print "split_row:", split_row

        for spe in split_row:
            stripped_lower_species = spe.strip().lower()

            if stripped_lower_species not in inserted_species_set:
                
                db_insert(cursor, 'Species', ['spe_id', 'name'], [count, stripped_lower_species])

                ###print "spe_id   spe_name:\t",count," ", stripped_lower_species
                ###print "inserted_species_set:", inserted_species_set

                inserted_species_set.add(stripped_lower_species)

                ###print "inserted_species_set:", inserted_species_set

                count = count + 1


# In[ ]:

db_populate_species(cur, source_data)


# In[ ]:

def db_populate_plasmid(cursor, sbider_data):
    
    db_delete(cursor, "Plasmid")

    p_id_p_name = sbider_data[['P_ID','P_Name']]

    ###print "p_id_p_name:\n\n", p_id_p_name

    p_id_p_name_lists = p_id_p_name.values.T.tolist()
    
    ###print "p_id_p_name_lists:\n", p_id_p_name_lists

    p_id_p_name_list = [row for row in it.izip(*p_id_p_name_lists)]

    ###print "p_id_p_name_list:\n", p_id_p_name_list

    inserted_plasmid_set = set([])
    for row in p_id_p_name_list:
        row = format_values(row)
        
        ###print "row:", row
        
        if row[0] not in inserted_plasmid_set:

            ###print "pla_id   pla_name:\t", row[0], " ", row[1]

            db_insert(cursor, 'Plasmid', ['pla_id', 'name'], [row[0], row[1].lower()])
            inserted_plasmid_set.add(row[0])


# In[ ]:

db_populate_plasmid(cur, source_data)


# In[ ]:

def db_populate_operon(cursor, sbider_data):
    
    db_delete(cursor, "Operon")
    
    o_id_structure = sbider_data[['O_ID', 'Structure']]

    ###print "o_id_structure:\n\n", o_id_structure

    o_id_structure_lists = o_id_structure.values.T.tolist()

    ###print "o_id_structure_lists:\n", o_id_structure_lists

    o_id_structure_list = [row for row in it.izip(*o_id_structure_lists)]

    ###print "o_id_structure_list:\n", p_id_p_name_list

    inserted_operon_set = set([])
    for row in o_id_structure_list:
        row = format_values(row)
        
        ###print "row:", row
        
        if row[0] not in inserted_operon_set and row[0] != "na":

            ###print "o_id   structure:\t", row[0], " ", row[1]

            db_insert(cursor, 'Operon', ['ope_id', 'name'], row)
            inserted_operon_set.add(row[0])


# In[ ]:

db_populate_operon(cur, source_data)


# In[ ]:

def db_populate_plasmid_operon(cursor, sbider_data):
    
    db_delete(cursor, "PlasmidOperon")

    p_id_o_id_direction = sbider_data[['P_ID', 'O_ID', 'R/L']]

    ###print "p_id_o_id_direction:\n\n", p_id_o_id_direction

    p_id_o_id_direction_lists = p_id_o_id_direction.values.T.tolist()

    ###print "p_id_o_id_direction_lists:\n", p_id_o_id_direction_lists

    p_id_o_id_direction_list = [row for row in it.izip(*p_id_o_id_direction_lists)]

    ###print "p_id_o_id_direction_list:\n", p_id_o_id_direction_list

    inserted_plasmid_operon_set = set([])
    for row in p_id_o_id_direction_list:
        row = format_values(row)
        
        ###print "row:", row
        
        if row[1].strip() not in inserted_plasmid_operon_set and row[1] != "na":

            ###print "ope_id   pla_id   direction:\t", row[1], " ", row[0], " ", row[2]

            db_insert(cursor, 'PlasmidOperon', ['pla_id', 'ope_id', 'direction'], row)
            inserted_plasmid_operon_set.add(row[1])


# In[ ]:

db_populate_plasmid_operon(cur, source_data)


# In[28]:

def db_populate_operon_input_transition_species(cursor, sbider_data):
    
    db_delete(cursor, "OperonInputTransition")
    db_delete(cursor, "InputTransitionSpecies")
    db_delete(cursor, "InputTransition")

    o_id_domain = sbider_data[['O_ID', 'Domain']]

    ###print "o_id_domain:\n\n", o_id_domain

    o_id_domain_lists = o_id_domain.values.T.tolist()

    ###print "o_id_domain_lists:\n", o_id_domain_lists

    o_id_domain_list = [row for row in it.izip(*o_id_domain_lists)]

    ###print "o_id_domain_list:\n", o_id_domain_list

    in_id_count = 1
    it_id_count = 1
    for row in o_id_domain_list:
        row = format_values(row)

        ###print "row", row

        if row[0] != "na":

            ###print "o_id   domain:\t", row[0], " ", row[1]

            species_list = row[1].split(',')

            ###print "split_species:", species_list

            logic_counter = 0
            for species in species_list:

                ###print "Going into the species loop"

                stripped_lower_species = species.strip().lower()

                ###print "stripped_species:", stripped_species

                species_id = db_get_species_id_from_name(cursor, stripped_lower_species)
                db_insert(cursor,'InputTransitionSpecies', 
                          ['in_id', 'it_id', 'spe_id'],
                          [in_id_count, it_id_count, species_id])

                #print "in_id   it_id   spe_id:\t", in_id_count, " ", it_id_count, " ", spe_id

                in_id_count += 1
                logic_counter = logic_counter + 1
                
                ###print "logic counter:", logic_counter
                
            db_insert(cursor, 'OperonInputTransition', ['it_id','ope_id'], [it_id_count, row[0]])                    
            
            if logic_counter > 1:
                logic = "AND"
            else:
                logic = "OR"
                
            db_insert(cursor, 'InputTransition', ['it_id','logic'], [it_id_count, logic])
            logic_counter = 1
            it_id_count = it_id_count + 1


# In[29]:

db_populate_operon_input_transition_species(cur, source_data)


# In[ ]:

def db_populate_operon_output_transition_species(cursor, sbider_data):
    
    db_delete(cursor, "OperonOutputTransition")
    db_delete(cursor, "OutputTransitionSpecies")
    db_delete(cursor, "OutputTransition")
    
    ope_id_range = sbider_data[['O_ID', 'Range']]

    ###print "ope_id_range:\n\n", ope_id_range

    ope_id_range_lists = ope_id_range.values.T.tolist()

    ###print "ope_id_range_lists:\n", ope_id_range_lists

    ope_id_range_list = [row for row in it.izip(*ope_id_range_lists)]

    ###print "o_id_domain_list:\n", o_id_domain_list

    out_id_count = 1
    ot_id_count = 1
    
    #list of tuples(operon_id, range)
    inserted_operon_transition_list = [] 
    
    for row in ope_id_range_list:
        row = format_values(row)
        operon_transition = (row[0], row[1])
        ###print "row", row

        if row[0] != "na" and operon_transition not in inserted_operon_transition_list:

            ###print "row (none 'na')", row

            species_list = row[1].split(',')

            ###print "split_species:", species_list
            
            logic_counter = 0
            for species in species_list:
                stripped_lower_species = species.strip().lower()

                ###print "\tstripped_lower_species:", stripped_lower_species

                species_id = db_get_species_id_from_name(cursor, stripped_lower_species)
                
                ###print "\tspecies_id:", species_id
                
                db_insert(cursor,'OutputTransitionSpecies', 
                          ['out_id', 'ot_id', 'spe_id'],
                          [out_id_count, ot_id_count, species_id])

                ###print "out_id   ot_id   species_id:\t", out_id_count, " ", ot_id_count, " ", species_id

                out_id_count += 1
                logic_counter = logic_counter + 1
                
                ###print "logic counter:", logic_counter

            db_insert(cursor, 'OperonOutputTransition', ['ot_id','ope_id'], [ot_id_count, row[0]])                                
            
            if logic_counter > 1:
                logic = "AND"
            else:
                logic = "OR"
            
            db_insert(cursor, 'OutputTransition', ['ot_id','logic'], [ot_id_count, logic])
            logic_counter = 1
            ot_id_count = ot_id_count + 1
            inserted_operon_transition_list.append((row[0], row[1]))


# In[ ]:

db_populate_operon_output_transition_species(cur, source_data)


# In[ ]:

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


# In[ ]:

def make_output_ope_id_spe_id_dict(sql):
    output_ope_id_spe_id_dict = {}

    merged_ope_ot_spe = sql.execute('''SELECT OperonOutputTransition.ope_id, 
                                       OperonOutputTransition.ot_id,
                                       OutputTransitionSpecies.spe_id 
                                       FROM   OperonOutputTransition,
                                       OutputTransitionSpecies 
                                       WHERE  OperonOutputTransition.ot_id = OutputTransitionSpecies.ot_id''')

    ###print "merged_ope_ot_spe:",merged_ope_ot_spe
    ###print "merged_ope_ot_spe.fetchall():",merged_ope_ot_spe.fetchall()
    ###print "merged_ope_ot_spe.fetchone():",merged_ope_ot_spe.fetchone()
    previous_operon, previous_output_transition, previous_species = merged_ope_ot_spe.fetchone()

    ###print 'previous_operon, previous_output_transition, previous_species:\t',previous_operon,"",previous_output_transition,"",previous_species

    output_transition_list_idx = 0

    ###print 'output_transition_list_idx', output_transition_list_idx

    output_ope_id_spe_id_dict[previous_operon] = [[]]

    output_ope_id_spe_id_dict[previous_operon][output_transition_list_idx].append(previous_species.strip())

    ###print "output_operon_species_dictionary:",output_operon_species_dictionary

    for operon, output_transition, species in merged_ope_ot_spe.fetchall():
        
        ###print "\toperon, output_transition, species:\t", operon, "", output_transition, "", species

        if operon == previous_operon:

            if output_transition == previous_output_transition:

                output_ope_id_spe_id_dict[operon][output_transition_list_idx].append(species.strip())

                ###print "\n\n\toutput_operon_species_dictionary:", output_ope_id_spe_id_dict

            elif output_transition != previous_output_transition:
                output_transition_list_idx = output_transition_list_idx + 1

                output_ope_id_spe_id_dict[operon].append([])
                output_ope_id_spe_id_dict[operon][output_transition_list_idx].append(species.strip())

                previous_output_transition = output_transition

        else:
            output_transition_list_idx = 0
            output_ope_id_spe_id_dict[operon] = [[]]
            output_ope_id_spe_id_dict[operon][output_transition_list_idx].append(species.strip())

            previous_operon = operon
            previous_output_transition = output_transition   
        
    return output_ope_id_spe_id_dict


# In[ ]:

in_dic = make_input_ope_id_spe_id_dict(cur)

###for pair in in_dic.items():
    ###print pair


# In[ ]:

out_dic = make_output_ope_id_spe_id_dict(cur)

###for pair in in_dic.items():
    ###print pair


# dicts = make_ope_id_spe_id_dicts(cur)
# for dic in dicts:
#     print "#" * 90
#     for pair in dic:
#         print pair

# In[ ]:

def make_pla_name_spe_name_dicts(sql):
    
    plasmid_name_input_species_name_dictionary = {}
    plasmid_name_output_species_name_dictionary = {}
    
    operon_id_plasmid_name_dictionary = {}
    
    species_id_to_name_dictionary = {}
    
    sql_cursor = sql.execute('SELECT spe_id,name FROM Species')
    
    for spe_id, spe_name in sql_cursor.fetchall():
        species_id_to_name_dictionary[spe_id] = spe_name

    input_operon_species_dictionary, output_operon_species_dictionary = make_ope_id_spe_id_dicts(sql)

    merged_ope_id_pla_name = sql.execute('''SELECT PlasmidOperon.ope_id,
                                                   Plasmid.name
                                            FROM PlasmidOperon,
                                                 Plasmid
                                            WHERE PlasmidOperon.pla_id = Plasmid.pla_id''')

    ###print merged_ope_id_pla_name.fetchall()

    for ope_id, pla_name in merged_ope_id_pla_name.fetchall():

        ###print "ope_id, pla_name:",ope_id," ", pla_name

        operon_id_plasmid_name_dictionary[ope_id] = pla_name

    ###for pair in operon_id_plasmid_name_dictionary.items():
        ###print pair
        
    for operon_id, species_id_list in input_operon_species_dictionary.items():
        
        ###print "species_id_list:", species_id_list
        
        extended_species_id_list = extend_list_of_lists(species_id_list)
        
        ###print "extended_species_id_list,",extended_species_id_list

        plasmid_name = operon_id_plasmid_name_dictionary[operon_id]
        
        ###print "spe_id entering sql dict and the type is", spe_id, type(spe_id)
        ###print "db_get_species_id(sql,spe_id):",db_get_species_id(sql,spe_id)
        
        #print "Is spe_id in species_id_to_name_dictionary:", spe_id in species_id_to_name_dictionary
        
        plasmid_name_input_species_name_dictionary[plasmid_name] = [db_get_species_name_from_id(sql,spe_id) for spe_id in extended_species_id_list]
        #plasmid_name_input_species_name_dictionary[plasmid_name] = [species_id_to_name_dictionary[spe_id] for spe_id in extended_species_id_list]

    for operon_id, species_id_list in output_operon_species_dictionary.items():
        
        ###print "species_id_list:", species_id_list
        
        extended_species_id_list = extend_list_of_lists(species_id_list)
        
        ###print "extended_species_id_list:", extended_species_id_list
          
        plasmid_name = operon_id_plasmid_name_dictionary[operon_id]
        #spe_id = "'" + spe_id + "'"
        
        ###print "spe_id entering sql dict and the type is", spe_id, type(spe_id)
        ###print "db_get_species_id(sql,spe_id):",db_get_species_id(sql,spe_id)
        
        plasmid_name_input_species_name_dictionary[plasmid_name] = [db_get_species_name_from_id(sql,spe_id) for spe_id in extended_species_id_list]
        #plasmid_name_input_species_name_dictionary[plasmid_name] = [species_id_to_name_dictionary[spe_id] for spe_id in extended_species_id_list]
    return plasmid_name_input_species_name_dictionary,plasmid_name_output_species_name_dictionary


# In[ ]:

def split_by(sequence, element):
    '''split a sequence by a given element and store elements
    before and after the element into a dictionary'''
    
    element_index = sequence.index(element)
    
    sequence_before_element = sequence[:element_index:1]
    sequence_after_element = sequence[element_index + 1::1]
    
    return {0: sequence_before_element, 1: sequence_after_element}


# In[ ]:

def uniquely_unlist(list_of_lists):
    unlisted = set([])
    for a_list in list_of_lists:
        for e in a_list:
            unlisted.add(e)
    return list(unlisted)


# In[31]:

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


# In[32]:

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


# In[ ]:

def get_path(input_dictionary, output_dictionary, input_species_list, output_species_list):
    '''get path from input species to output species'''

    ###print "input_species_list:", input_species_list
    
    ###print type(input_species_list)
    
    path_queue = [ ([],[input_species_list]) ]
    visited_species_list = []

    final_operon_path_list = []
    final_species_path_list = []
    
    while path_queue != []:
        
        ###print "\nget_path: path queue:\n", path_queue
        
        ###print type(path_queue[0][1])

        path_queue, visited_species_list, final_operon_path_list, final_species_path_list = traverse(input_dictionary,
                                                                                                     output_dictionary,
                                                                                                     input_species_list,
                                                                                                     output_species_list,
                                                                                                     path_queue,
                                                                                                     visited_species_list,
                                                                                                     final_operon_path_list,
                                                                                                     final_species_path_list)
    return final_operon_path_list, final_species_path_list


# In[ ]:

def traverse(input_dictionary, output_dictionary,
             input_species_list, output_species_list,
             path_queue, visited_species_list,
             final_operon_path_list, final_species_path_list):
    '''construct path'''
    
    (visited_operon_list, precedently_visited_species_list) = path_queue.pop(0)
    
    ###print "\tprecedently_visited_species_list:",precedently_visited_species_list

    ###print "\tsearching for operons that can be activated by", precedently_visited_species_list
    # searches for operons activated by current input species
    for an_operon in set(input_dictionary.keys()) - set(visited_operon_list):
        
        ###print "\n\t\tpotential operon & its input species:\n\t\t",an_operon," & ",input_dictionary[an_operon]
        ###print "\t\t\tdoes species", precedently_visited_species_list, "match an_operon(ope_id:", an_operon, ")'s input species:", input_dictionary[an_operon],"???"
        if is_activated(input_dictionary[an_operon], precedently_visited_species_list) == True:

            
            ###print "\t\t\t!!!!!!!!!YES!!!!!!!!!!"
            
            ###print "\t\t\tcurrent visited_operon_list:", visited_operon_list
            ###print "\t\t\t#just activated operon:", an_operon
            # store activated operon
            a_visited_operon_list = list(visited_operon_list) + [an_operon]
            
            a_produced_species_list = output_dictionary[an_operon]
            
            ###print "\t\t\tcurrent visited_species_list:", visited_species_list
            ###print "\t\t\t#just produced species by", "operon(ope_id", an_operon, "):", a_produced_species_list
            # store produced speacies (unique)
            for a_produced_species in a_produced_species_list:
                visited_species_list = unite_lists([visited_species_list, a_produced_species])
                
            ###print "\t\t\t\t###a_visited_operon_list:", a_visited_operon_list
            ###print "\t\t\t\t###visited_species_list:", visited_species_list
            
            ###print "\t\t\t\tcan", output_species_list, "be found in", a_produced_species_list,"???"
            
            # if output speices is found, include this operon and species path lists in the 
            # final operon and species paths
            if is_produced(a_produced_species_list, output_species_list):
                
                ###print "\t\t\t\t\t!!!!!!!!!OUTPUT SPECIES FOUND!!!!!!!!!!\n"
                
                final_operon_path_list.append(a_visited_operon_list)
                final_species_path_list.append(uniquely_unlist(a_produced_species_list))
                
                ###print "\t\t\t\t\tfinal_operon_path_list:", final_operon_path_list
                ###print "\t\t\t\t\tfinal_species_path_list:", final_species_path_list
                ###print
                
            # If output species is not found, include this operon and species path lists in path queue
            else:
                
                ###print "\t\t\t\t\tthis activated operon(ope_id:", an_operon, ") does not produce output species........."
                ###print "\t\t\t\t\tand this path is to be continued later (appending in path_queue)"
                                                
                unique_visited_species_list = uniquely_unlist([species for species in a_produced_species_list if species not in visited_species_list])
                ###print "\t\t\t\t\tunique_visited_species_list:",unique_visited_species_list

                path_queue.append( (a_visited_operon_list,unique_visited_species_list) )
                ###print "\t\t\t\t\tupdated path_queue:", path_queue
    
    
    ###print "\n\n\n\t###final path_queue###\n",
    ###for a_queue_pair in path_queue:l
        ###print "\t", a_queue_pair
        ###print "\n"
    
    return path_queue, visited_species_list, final_operon_path_list, final_species_path_list


# visited_species_list = [1,2,3,4,5]
# 
# a_produced_species_list = [1,9,9]
# 
# unique_visited_species_list = [species for species in a_produced_species_list if species not in visited_species_list]
# 
# unique_visited_species_set = set(unique_visited_species_list)
# 
# 
# unique_visited_species_list = list(unique_visited_species_set)
# 
# print unique_visited_species_list

# In[ ]:

user_input = "LuxR and OHHL > gfp"

logic_dictionary = parse_logic(cur, user_input)

print "\nlogic_dictionary:", logic_dictionary

for input_species, output_species_list in logic_dictionary.items():
    for output_species in output_species_list:
    
        print "Path:",input_species,"--->",output_species,"="
        
        ###print type(input_species)
        ###print type(output_species)

        operon_path_list, species_path_list = get_path(input_path_dictionary,
                                                       output_path_dictionary,
                                                       input_species,
                                                       output_species)
        
        # operon path
        operon_path_subnetwork_list = []
        for operon_path in operon_path_list:
            print "operon_path:",operon_path
            operon_path_subnetwork_list.extend(operon_path)
        operon_path_subnetwork_graph = make_graph_from_path_list(operon_path_subnetwork_list)
        #draw_plot(operon_path_subnetwork_graph)
            
        # species path
        species_path_subnetwork_list = []
        for species_path in species_path_list:
            print "species_path:",species_path
            species_path_subnetwork_list.extend(species_path)
        species_path_subnetwork_list = make_graph_from_path_list(species_path_subnetwork_list)
        #draw_plot(species_path_subnetwork_list)


# In[ ]:

for key, val in output_path_dictionary_sbider.items():
    print key, " ---> ", val


# In[ ]:

db_print_table(cur, "OperonInputTransition")


# In[ ]:

db_print_table(cur, "OperonOutputTransition")


# In[ ]:

db_print_table(cur, "PlasmidOperon")


# In[ ]:

db_print_table(cur,"Operon")

