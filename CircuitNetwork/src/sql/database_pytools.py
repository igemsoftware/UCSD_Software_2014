<<<<<<< HEAD
cimport sql_pytools as sqlpy
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
    """Opens the specified database by making a connection to it."""
    global conn 
    conn = sqlite3.connect(database)
    conn.text_factory = str
    global sql 
    sql = conn.cursor()
    
def close():
    """Closes the mostly recently opened database."""
    conn.commit()
    sql.close()
    
def make_db():
	plasmid = '''CREATE TABLE plasmid (id VARCHAR(50), name VARCHAR(50), 
		miriam_id VARCHAR(50), title VARCHAR(50), authors VARCHAR(50), 
		journal VARCHAR(50), year VARCHAR(50));'''
	operon = '''CREATE TABLE operon (id VARCHAR(50), name VARCHAR(50), 
		sbol VARCHAR(50));'''
	part = 'CREATE TABLE part (id VARCHAR(50), name VARCHAR(50));'
	interactors = '''CREATE TABLE interactor (id VARCHAR(50),name VARCHAR(50), 
		type VARCHAR(50));'''
	inputt = '''CREATE TABLE input (id VARCHAR(50), interactor_id VARCHAR(50),
		repressor bool);'''
	output = '''CREATE TABLE output (id VARCHAR(50), 
		interactor_id VARCHAR(50));'''    
	opr = '''CREATE TABLE opr (id VARCHAR(50), operon_id VARCHAR(50), 
		plasmid_id VARCHAR(50), direction VARCHAR(50), Main NUM(10));'''
	optr = '''CREATE TABLE optr (id VARCHAR(50), operon_id VARCHAR(50), 
		part_id VARCHAR(50), position NUM(10));'''
	oitr = '''CREATE TABLE oitr (id VARCHAR(50), operon_id VARCHAR(50), 
		interactor_id VARCHAR(50));'''
	ootr = '''CREATE TABLE ootr (id VARCHAR(50), operon_id VARCHAR(50), 
		interactor_id VARCHAR(50));'''
	login = '''CREATE TABLE login (id VARCHAR(50), email VARCHAR(50), 
		password VARCHAR(50));'''
	
	table_list =[plasmid, operon, part, interactors, opr, optr, oitr, ootr, inputt, output]
	for table in table_list:
		custom(table)
        
def insert(table_name,cols,new_row):
    """Inserts data into the given database table
    Args:
        table_name, that table that you wish to insert into
        cols, the columns that you want to insert into
        new_row, the values that correspond to the columns
    
    Examples:
        ex 1. Inserting into plasmid table and filling in all the columns. 
    """
    command = sqlpy.sql_insert(table_name, cols,new_row)
    print "\n" * 3
    print command
    sql.execute(command)
    
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
    
#def update():
    
def custom(command):
    """Execute a custom made sql command
    Return: A cursor object. If the sql command used produces a result such as
    the select command then this cursor object must be assigned to a 
    variable and the commmand fetchone() or fetchall() should be used. 
    
    Ex 1. 
    cur = cu 
    """
    return sql.execute(command)
        
def print_table(table_name):
    """Prints out the specified table for visualization purposes only."""
    cur = custom("SELECT * FROM " + table_name)
    table_list = cur.fetchall()
    for row in table_list:
        print row               
    
#--------------------Logic Accessions--------------------#        
def single_trans_to_bool(trans_ID):
    """Determine the boolean logic of a single transition using the ID
    Args:
        trans_ID: the transition for which logic is desired
    """
    trans_list = sql.execute('''SELECT Interactor_ID, NOT/
        FROM input_trans WHERE Input_Transition_ID = ''' + trans_ID)
    return bool_trans(trans_list)
=======
<<<<<<< HEAD
import sql_pytools
import sqlite3
>>>>>>> 211b09cae59c4cf4aa8686ac4e119bed925987a5

def single_operon_to_bool(operon_ID):
    """Determine the boolean logic of a single operon using the ID
    Args:
        operon_ID: the operon for which logic is desired
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
    """Determine the boolean logic for all transitions in the database
    Collecting all of the transition-interactor information inside 
    of a dictionary 
        #Key: trans_ID
        #Value: List of [[interactor1, not_boolean1], 
            [interactor2, not_boolean2], ...]
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
    """Determine the boolean logic of transition based on interactor
    
    Args:
        interactor: list of paired lists with interactor ID and NOT boolean
        
    SUGGESTIONS:
        convert from the interactor_ID to the interactor_name 
    """
    #single input, buffer transitions 
    if len(interactor) == 1 and interactor[0][1] != False:
        return "IF", interactor[0][0] 
    #single input, not transition
    elif len(interactor) == 1 and interactor[0][1] == True:
        return "NOT", interactor[0][0] 
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
    
         
def to_json_node():
    """
    Obtain nodes and edge information and parse into json
    """
    nodes_table = ["interactor", "input", "output", "operon"]
    
    interactor_list = []
    sql.execute("SELECT id, name from interactor" )
    interactor_list.extend(sql.fetchall())
    
    input_list = []
    sql.execute("SELECT id, name from input" )
    input_list.extend(sql.fetchall())
    
    output_list = []
    sql.execute("SELECT id, name from output" )
    output_list.extend(sql.fetchall())
    
    operon_list = []
    sql.execute("SELECT id, name from operon" )
    operon_list.extend(sql.fetchall())
    
    
    nodes_list = [interactor_list, input_list, output_list, operon_list]
    for ls in nodes_list:
        for node in interactor_list:
                json_str += to_json(node)

def to_json_edge():
    """
    Obtain nodes and edge information and parse into json
    """
    edges_table = ["input","output","oitr", "ootr"]
    
    interactor_list = []
    sql.execute("SELECT id, interactor_id from input" )
    interactor_list.extend(sql.fetchall())
    
    input_list = []
    sql.execute("SELECT id, interactor_id from output" )
    input_list.extend(sql.fetchall())
    
    output_list = []
    sql.execute("SELECT operon_id, input_id from oitr")
    output_list.extend(sql.fetchall())
    
    operon_list = []
    sql.execute("SELECT operon_id, output_id from ootr" )
    operon_list.extend(sql.fetchall())
    
    
    nodes_list = [interactor_list, input_list, output_list, operon_list]
    for ls in nodes_list:
        for node in interactor_list:
                json_str += to_json(node)
        
        
def to_network():
    """Making two dictionaries for the traversal.
    Returns:
       A tuple with two dictionaries. The first   
    """
    input_trans_dict = {}
    inputt = sql.execute("SELECT id, interactor_id from input")
    cur = inputt.fetchone()
    count = 1
    while isinstance(cur, tuple) is True:
        key = cur[0]
        if key in input_trans_dict:
            input_trans_dict[key].add(cur[1])
        else:
            input_trans_dict[key] = set([cur[1]])
        count += 1
        cur = inputt.fetchone()
        '''
<<<<<<< HEAD
        key: transition ID
        value: set with the inputs species. ex set(['a','b','c'])
        '''
    output_trans_dict = {}
    output = sql.execute("SELECT id, interactor_id from output")
    cur = output.fetchone()
    while isinstance(cur, tuple) is True:
        key = cur[0]
        if key in output_trans_dict:
            output_trans_dict[key].add(cur[1])
        else:
            output_trans_dict[key] = set([cur[1]])
        cur = output.fetchone()
    
    return input_trans_dict, output_trans_dict
    '''
    key: transition ID
    value: list with all the species produce by that operon/transition
    '''
    
def pull_columns(col_nums):
    """Returns a list of column names based on the index location"""
    columns= []
    for nums in col_nums:
        try:
            columns.append(col_nums[nums])
        except:
            raise Exception("Table is " + len(columns_list) + ''' long. Tried to 
                access non-existant index ''' + nums)
    return columns
    
def unlist_values(to_list):
    """Stringify values in a list that are within a list
    ARGS:
        to_list, a list with lists of single values
    """
    return [''.join(x) for x in to_list]

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
=======
    conn = sqlite3.connect('igemDatabase.db.txt')
=======
mport SQLInterface
import sqlite3

# Suggestion: it may be better to pass in a cursor object. That way you don't have to be
# connecting and reconnecting all of the time. 

# static variables for tables in the sql database
# actually I cannot hard code these variables we may not return every single column every single time
DEVICES_COLS = ['Name', 'Components', 'Authors', 'Article', 'Journal', 'Image_Path']
TRANSITIONS_COLS = ['Input', 'Output', 'Function']
INTERMEDIATES_COLS = ['Name', 'Type', 'Annotation']

def insert_into_database(devices_row = None, transitions_row = None, intermediates_row = None):
    '''
    param: cursor, need a connection to the sql database (using sqlite3) in order to insert.
    param: device, list with information in corresponding device table location.
    param: transition, list with information in the corresponding transition table location.
    param: intermediate, list with the information in the corresponding intermediate table location.
    '''
    conn = sqlite3.connect('igemDBdevice.db.txt')
>>>>>>> cad6433ea4b471adf416c7db14e7fa99beb76206
    cur = conn.cursor()
    if devices_row is not None and len(DEVICES_COLS) == len(devices_row):
        d = sql_insert('Devices', DEVICES_COLS, devices_row)
        cur.execute(d)
    if transitions_row is not None and len(TRANSITIONS_COLS) == len(transitions_row):
        t = sql_insert('Transitions', TRANSITIONS_COLS, transitions_row)
        cur.execute(t)
<<<<<<< HEAD
    if intermediates_row is not None and len(INTERMEDIATES_COLS) == len(intermediates_row):
        i = sql_insert('Intermediates', INTERMEDIATES_COLS, intermediates_row)
        cur.execute(i)
    cur.close()
    conn.commit()


def update_database(devices_row = None, transitions_row = None, intermediates_row = None):
    '''
        param: cursor, need a connection to the sql database (using sqlite3) in order to insert.
        param: device, list with information in corresponding device table location.
        param: transition, list with information in the corresponding transition table location.
        param: intermediate, list with the information in the corresponding intermediate table location.
        '''
    conn = sqlite3.connect('igemDatabase.db.txt')
=======
    if intermediates_row is not None and len(INTERMEDIATES_COLS) == len(intermediates_row):    
        i = sql_insert('Intermediates', INTERMEDIATES_COLS, intermediates_row)
        cur.execute(i)
    cur.close()
    
def update_database(devices_row = None, transitions_row = None, intermediates_row = None):
    '''
    param: cursor, need a connection to the sql database (using sqlite3) in order to insert.
    param: device, list with information in corresponding device table location.
    param: transition, list with information in the corresponding transition table location.
    param: intermediate, list with the information in the corresponding intermediate table location.
    '''
    conn = sqlite3.connect('igemDBdevice.db.txt')
>>>>>>> cad6433ea4b471adf416c7db14e7fa99beb76206
    cur = conn.cursor()
    if devices_row is not None and len(DEVICES_COLS) == len(devices_row):
        d = sql_update('Devices', DEVICES_COLS, devices_row)
        cur.execute(d)
    if transitions_row is not None and len(TRANSITIONS_COLS) == len(transitions_row):
        t = sql_update('Transitions', TRANSITIONS_COLS, transitions_row)
        cur.execute(t)
<<<<<<< HEAD
    if intermediates_row is not None and len(INTERMEDIATES_COLS) == len(intermediates_row):
        i = sql_update('Intermediates', INTERMEDIATES_COLS, intermediates_row)
        cur.execute(i)
    cur.close()
    conn.commit()



def search_database(devices_row = None, transitions_row = None, intermediates_row = None):
    '''
        '''
    conn = sqlite3.connect('igemDatabase.db.txt')
=======
    if intermediates_row is not None and len(INTERMEDIATES_COLS) == len(intermediates_row):    
        i = sql_update('Intermediates', INTERMEDIATES_COLS, intermediates_row)
        cur.execute(i)
    cur.close()
    
            
def search_database(devices_row = None, transitions_row = None, intermediates_row = None):
    '''
    '''
    conn = sqlite3.connect('igemDBdevice.db.txt')
>>>>>>> cad6433ea4b471adf416c7db14e7fa99beb76206
    cur = conn.cursor()
    d = ''
    t = ''
    i = ''
    if devices_row is not None:
        d = sql_search('Devices', DEVICES_COLS,...)
        d = cur.execute(d)
        d = cur.fetchall()
    if transitions_row is not None:
        t = sql_search('Transitions', TRANSITIONS_COLS,...)
        t = cur.execute(t)
        t = cur.fetchall()
    if intermediates_row is not None:
        i = sql_search('Intermediates', INTERMEDIATES_COLS, ...)
        i = cur.execute(i)
        i = cur.fetchall()
    cur.close()
<<<<<<< HEAD

    return [d, t, i]
=======
        
    return [d, t, i]
       
>>>>>>> cad6433ea4b471adf416c7db14e7fa99beb76206
>>>>>>> 211b09cae59c4cf4aa8686ac4e119bed925987a5
