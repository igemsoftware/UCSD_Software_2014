import sql_pytools as sqlpy
import sqlite3
# Suggestion: it may be better to pass in a cursor object. That way you don't have to be
# connecting and reconnecting all of the time. 
# Suggestion #2: Might also think about making a class that quickly can capture the bool
# logic that is happening. This would make transitions objects. 
# Suggestion #3: In order to capture bool logic for or you may need a list that 
# separates transitions by the or placement. 
# Suggestion #4: May need make methods that also return only the name of each genetic part

conn = sqlite3.connect("h.db")
conn.text_factory = str
sql = conn.cursor()

#Declaring list global variables for integration with accession functions

plasmid_table = ["ID", "Name", "Miriam_ID", "Size"]
operon_table = ["ID", "Name", "Image_Path"]
part_table = ["ID", "Name"]
interactor_table = ["ID", "Name","Not_bool"]
opr_table = ["ID", "Operon_ID", "Plasmid_ID", "Main"]
optr_table = ["ID", "Operon_ID", "Part_ID", "Position"]
oitr_table = ["ID", "Operon_ID", "Input_Transition_ID"]
ootr_table = ["ID", "Operon_ID", "Output_Transition_ID"]
input_trans_table = ["ID", "Input", "NOT"]
output_trans_table = ["ID", "Output"]
    
#--------------------DB Accessions--------------------#                
def database_select(table_name, col_names = ["ID"], w_col = None, w_opt = None,
    w_var = None,w_bool = None, group = False, h_col = None, h_bool = None, 
    h_value = None):
    '''
    Pulls data from the desired table by specifying the table name and index cols
    Returns a list of tuples where each tuple has 
    @param table_name, table you wish to pull data from
    @param col_nums, list of numbers indexing the table columns
    @param w_col, column names for where clause
    @param w_opt, operator for where clause
    @param w_var, variable for where clause 
    @param w_bool, boolean for where clause
    @param group, group name for GROUP BY caluse
    @param h_col, group specifier
    
    Examples
        ex 1. Pulling multiple columns from the Plasmid table
            database_select('plasmid', [0,1])
        
            returned is [("p_001", "pOR"), ("p_002", "pAND"), ...]
            
        ex 2. Pulling a single column from the part table
            database_select('part', [0])
            
            returned is [("pt_001"), ("pt_002"), ...]
            CAUTION: When working with result make sure you recognize you 
            have a list with tuples of single values. User unlist function
            to fix this. 
            
        ex. 3 Pulling very specific data. To do so you have to use the optional
            parameters w_col, w_opt, w_var and w_bool.
            database_select("itr", [0,1], 2, "!=", True)) 
    '''
    command = sqlpy.sql_select(table_name,col_names, w_col, w_opt, w_var,
        w_bool, group, h_col, h_bool, h_value)
    sql.execute(command)
    return sql.fetchall()
    
def database_insert(table_name,cols,new_row):
    '''
    Allows you to insert data into any table. 
    @param table_name, that table that you wish to insert into
    @param cols, the columns that you want to insert into
    @param new_row, the values that correspond to the columns
    
    Examples
        ex 1. 
    '''
    command = sqlpy.sql_insert(table_name, cols,new_row)
    print "\n" * 10
    print command
    sql.execute(command)
    
def database_custom(command):
    return sql.execute(command)
    
def database_close():
    conn.commit()
    sql.close()
    
    
#--------------------Logic Accessions--------------------#        
def single_trans_to_bool(trans_ID):
    '''
    Determine the boolean logic of a single transition using the ID
    @param trans_ID, the transition for which logic is desired
    '''
    trans_list = sql.execute('''SELECT Interactor_ID, NOT/
        FROM input_trans WHERE Input_Transition_ID = ''' + trans_ID)
    return bool_trans(trans_list)

def single_operon_to_bool(operon_ID):
    '''
    Determine the boolean logic of a single operon using the ID
    @param operon_ID, the operon for which logic is desired
    '''
    operon_list = sql.execute('''SELECT Input_Transition_ID from oitr 
        where Operon_ID = ''' + operon_ID)
    operon_list = unlist_values(operon_list)
    operon_list = [single_trans_to_bool(x) for x in operon_list]
    if len(operon_list) == 1:
        return operon_list
    else:
        return ' OR '.join(operon_list)    

def database_to_trans_logic():
    '''
    Determine the boolean logic for all transitions in the database
    Collecting all of the transition-interactor information inside of a dictionary 
        #Key: trans_ID
        #Value: List of [[interactor1, not_boolean1], [interactor2, not_boolean2], ...]
    '''  
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
            
def database_to_bool_operon():
    '''
    Determine the boolean logic of the whole operon
    '''
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
    trans_logic_dict = database_to_trans_logic()
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
    '''
    Determine the boolean logic of transition based on interactor
    @param interactor, list of paired lists with interactor ID and NOT boolean
    SUGGESTIONS: will need to convert from the interactor_ID to the 
    interactor_name at some point. Will have to query sql to do so.
    I think it's better to query than to make a whole new dictionary
    with key: interactor_ID value: interactor_name
    '''
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
    '''
    Return a list of column names
    '''
    columns= []
    for nums in col_nums:
        try:
            columns.append(col_nums[nums])
        except:
            raise Exception("Table is " + len(columns_list) + ''' long. Tried to 
                access non-existant index ''' + nums)
    return columns
    
def unlist_values(to_list):
    '''
    Stringify values in a list that are within a list
    @param to_list, a list with lists of single values
    '''
    return [''.join(x) for x in to_list]
    
#--------------------Accessions,working--------------------#        
def database_to_json():
    '''
    Obtain nodes and edge information and parse into json
    '''
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
        

def database_to_pigeon():
    '''
    Obtain operon information and parse into pigeonCAD string commands
    '''   
    pass
    