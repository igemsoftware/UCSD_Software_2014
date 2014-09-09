import sql_pytools as sqlpy
import sqlite3
import pandas as pd
# Suggestion: it may be better to pass in a cursor object. That way you don't have to be
# connecting and reconnecting all of the time. 
# Suggestion #2: Might also think about making a class that quickly can capture the bool
# logic that is happening. This would make transitions objects. 
# Suggestion #3: In order to capture bool logic for or you may need a list that 
# separates transitions by the or placement. 
# Suggestion #4: May need make methods that also return only the name of each genetic part

#def database_open(database = "SBiDer_v1.db"):
def open(database):
    global conn 
    conn = sqlite3.connect(database)
    conn.text_factory = str
    global sql 
    sql = conn.cursor()
    
def print_table(table_name):
    cur = custom("SELECT * FROM " + table_name)
    table_list = cur.fetchall()
    for row in table_list:
        print row
    
def make_db(database):
    #Setting up all of the csv names to extract the data
    info_names = ["plasmid", "operon", "part", "interactor", "input", "output", "opr", "optr", "oitr", "ootr"]

    #Creating tables of genetic constructs and interactors
    plasmid = 'CREATE TABLE plasmid (id VARCHAR(50), name VARCHAR(50), miriam_id VARCHAR(50), title VARCHAR(50), authors VARCHAR(50), journal VARCHAR(50), year VARCHAR(50));'
    operon = 'CREATE TABLE operon (id VARCHAR(50), name VARCHAR(50), sbol VARCHAR(50));'
    part = 'CREATE TABLE part (id VARCHAR(50), name VARCHAR(50));'
    interactors = 'CREATE TABLE interactor (id VARCHAR(50),name VARCHAR(50), type VARCHAR(50));'
    #Creating tables of transitions that are used for the petri nets
    inputt = 'CREATE TABLE input (id VARCHAR(50), interactor_id VARCHAR(50), repressor bool);'
    output = 'CREATE TABLE output (id VARCHAR(50), interactor_id VARCHAR(50));'    
    #Creating tables of relationships
    opr = 'CREATE TABLE opr (id VARCHAR(50), operon_id VARCHAR(50), plasmid_id VARCHAR(50), direction VARCHAR(50), Main NUM(10));'
    optr = 'CREATE TABLE optr (id VARCHAR(50), operon_id VARCHAR(50), part_id VARCHAR(50), position NUM(10));'
    #can use input.txt
    oitr = 'CREATE TABLE oitr (id VARCHAR(50), operon_id VARCHAR(50), interactor_id VARCHAR(50));'
    #can use output.txt
    ootr = 'CREATE TABLE ootr (id VARCHAR(50), operon_id VARCHAR(50), interactor_id VARCHAR(50));'
    
    
    #care. If you actually do this then you WILL OVERRIDE the current database. 
    table_list =[plasmid, operon, part, interactors, opr, optr, oitr, ootr, inputt, output]
    for table in table_list:
        custom(table)

#Declaring list global variables for integration with accession functions

plasmid_table = ["ID", "Name", "Miriam_ID"]
operon_table = ["ID", "Name", "Image_Path"]
part_table = ["ID", "Name"]
interactor_table = ["ID", "Name","Repressor"]
opr_table = ["ID", "Operon_ID", "Plasmid_ID"]
optr_table = ["ID", "Operon_ID", "Part_ID", "Position"]
oitr_table = ["ID", "Operon_ID", "Input_ID"]
ootr_table = ["ID", "Operon_ID", "Output_ID"]
input_trans_table = ["ID", "Input", "Repressor"]
output_trans_table = ["ID", "Output"]
    
#--------------------DB Accessions--------------------#                
def select(table_name, col_names = ["ID"], w_col = None, w_opt = None,
    w_var = None,w_bool = None, group = False, h_col = None, h_bool = None, 
    h_value = None):
    """Pulls data from the corresponding table
    Args:
        table_name: table you wish to pull data from
        col_names: list of numbers indexing the table columns
        w_col: column names for where clause
        w_opt: operator for where clause
        w_var: variable for where clause 
        w_bool: boolean for where clause
        group: group name for GROUP BY caluse
        h_col: group specifier
        
    Returns:
        A list of tuples corresponding with column data
    
    Examples:
        ex 1. Pulling multiple columns from the Plasmid table
            select('plasmid', [0,1])
        
            returned is [("p_001", "pOR"), ("p_002", "pAND"), ...]
            
        ex 2. Pulling a single column from the part table
            select('part', [0])
            
            returned is [("pt_001"), ("pt_002"), ...]
            CAUTION: When working with result make sure you recognize you 
            have a list with tuples of single values. User unlist function
            to fix this. 
            
        ex 3. Pulling very specific data. To do so you have to use the optional
            parameters w_col, w_opt, w_var and w_bool.
            select("itr", [0,1], 2, "!=", True)) 
    """
    command = sqlpy.sql_select(table_name,col_names, w_col, w_opt, w_var,
        w_bool, group, h_col, h_bool, h_value)
    sql.execute(command)
    return sql.fetchall()
    
def insert(table_name,cols,new_row):
    """Inserts data into the given database table
    Args:
        table_name, that table that you wish to insert into
        cols, the columns that you want to insert into
        new_row, the values that correspond to the columns
    
    Examples:
        ex 1. 
    """
    command = sqlpy.sql_insert(table_name, cols,new_row)
    print "\n" * 3
    print command
    sql.execute(command)
    
#def update():
    
def custom(command):
    """Execute a custom made sql command
    Return:
    """
    return sql.execute(command)
    
def close():
    conn.commit()
    sql.close()
    
    
#--------------------Logic Accessions--------------------#        
def single_trans_to_bool(trans_ID):
    """
    Determine the boolean logic of a single transition using the ID
    @param trans_ID, the transition for which logic is desired
    """
    trans_list = sql.execute('''SELECT Interactor_ID, NOT/
        FROM input_trans WHERE Input_Transition_ID = ''' + trans_ID)
    return bool_trans(trans_list)

def single_operon_to_bool(operon_ID):
    """
    Determine the boolean logic of a single operon using the ID
    @param operon_ID, the operon for which logic is desired
    """
    operon_list = sql.execute('''SELECT Input_Transition_ID from oitr 
        where Operon_ID = ''' + operon_ID)
    operon_list = unlist_values(operon_list)
    operon_list = [single_trans_to_bool(x) for x in operon_list]
    if len(operon_list) == 1:
        return operon_list
    else:
        return ' OR '.join(operon_list)    

def to_trans_logic():
    """
    Determine the boolean logic for all transitions in the database
    Collecting all of the transition-interactor information inside of a dictionary 
        #Key: trans_ID
        #Value: List of [[interactor1, not_boolean1], [interactor2, not_boolean2], ...]
    """  
    trans_list = sql.execute("SELECT Interactor_ID, Input_Transition_ID, NOT")
    trans_dict = {}
    for trans in trans_list:
        trans_ID = trans[1]
        if trans_ID in trans_dict:
            trans_dict[trans_ID].append([trans[0]] + [trans[2]])
        else:
            trans_dict[trans_ID] = [trans[0]] + [trans[2]]
    
    #Collecting all of the transtion-interactor boolean inside a dictionary
        #Key: trans_ID
        #Value: boolean string
    trans_bool_dict = {}
    for trans_ID, interactors_list in trans_dict:
            if trans_ID in trans_bool_dict:
                trans_bool_dict[trans_ID].append(bool_trans(interactors_list))
            else:
                trans_bool_dict[trans_ID] = [bool_trans(interactors_list)]
    return interactors_list
            
def to_bool_operon():
    """
    Determine the boolean logic of the whole operon
    """
    operon_trans_list = sql.execute('grab all of the operons and transitions')
    for rlts in operon_trans_list:
        operon_ID = rlts[0] 
        if operon_ID in operon_trans_dict:
            operon_trans_dict[operon_ID].append(rlts[1])
        else:
            operon_trans_dict[operon_ID] = [rlts[1]]
            
    #Collecting a list of operon logic and returning a dictionary.
       #Key: operon_ID          
       #Value: operon logic
    trans_logic_dict = to_trans_logic()
    operon_logic_dict = []
    for operon_ID, trans_bools in operon_trans_dict.values():
        if len(trans_bools) == 1:
            operon_logic_dict[operon_ID] = trans_logic_dict[operon_ID]
        else:
            bool_string = ""
            for logic in trans_bools:
                bool_string += logic + " OR "
            bool_string = bool_string[0:-4:] #remove that annoying last " OR "
        operon_logic_dict[operon_ID] = bool_string
    return operon_logic_dict
    
#--------------------helpers--------------------#        
def bool_trans(interactor): 
    """
    Determine the boolean logic of transition based on interactor
    @param interactor, list of paired lists with interactor ID and NOT boolean
    SUGGESTIONS: will need to convert from the interactor_ID to the 
    interactor_name at some point. Will have to query sql to do so.
    I think it's better to query than to make a whole new dictionary
    with key: interactor_ID value: interactor_name
    """
    #single input, buffer transitions 
    if len(interactor) == 1 and interactor[0][1] != False:
        return "IF", interactor[0][0] #interactor[0][0] ID maybe also return the i_ID (or only it) and may not actually return
    #single input, not transition
    elif len(interactor) == 1 and interactor[0][1] == True:
        return "NOT", interactor[0][0] #interactor[0][0] maybe also return the i_ID
    #multiple input, and transition
    elif len(interactor) > 1:
        bool_string = ""
        i = 0
        for interactor in interactor.values():
            if i == 0:
                if interactor[0][1] == False:
                    bool_string += str(interactor[0][0])
                else:
                    bool_string += "NOT " + str(interactor[0][0])
            else: 
                if i == 0:
                    if interactor[0][1] == False:
                        bool_string += " AND " + str(interactor[0][0])
                    else:
                        bool_string += " AND NOT " + str(interactor[0][0])
        return bool_string
        
def pull_columns(col_nums):
    """
    Return a list of column names
    """
    columns= []
    for nums in col_nums:
        try:
            columns.append(col_nums[nums])
        except:
            raise Exception("Table is " + len(columns_list) + ''' long. Tried to 
                access non-existant index ''' + nums)
    return columns
    
def unlist_values(to_list):
    """
    Stringify values in a list that are within a list
    @param to_list, a list with lists of single values
    """
    return [''.join(x) for x in to_list]
    
#--------------------Accessions,working--------------------#        
def to_json():
    """
    Obtain nodes and edge information and parse into json
    """
    nodes_table = ["interactor", "input", "output", "operon"]
    edges_table = ["itr","",""]
    
    nodes_list = []
    sql.execute("SELECT blah_columns from interactor" )
    nodes_list.append(sql.fetchall())
    sql.execute("SELECT blah_columns from input" )
    nodes_list.append(sql.fetchall())
    sql.execute("SELECT blah_columns from output" )
    nodes_list.append(sql.fetchall())
    sql.execute("SELECT blah_columns from operon" )
    nodes_list.append(sql.fetchall())
    
    f#or table in nodes_table:
        

def to_pigeon():
    """
    Obtain operon information and parse into pigeonCAD string commands
    """   
    pass
    
def main():
    
    #if(osp.isfile())
    
    
    print "Made a new database. Thank god"

if __name__ == "__main__":
    main()