# filename: SQLInterface
# author: Joaquin Reyna
# date: 07/02/14
# description: SQLwrappers and testing

import sqlite3

# static variables for tables in the sql database
devices_cols = ['Name', 'Components', 'Authors', 'Article', 'Journal', 'Image_Path']
transitions_cols = ['Input', 'Output', 'Function']
intermediates_cols = ['Name', 'Type', 'Annotation']

class sql_table:    
    '''
    SQL table object used to test SQL wrappers.
    ''' 
    # Static variables    
    TABLE_NAME = 'running'
    COLUMNS = ['Date', 'Miles', 'Trail']
    
    
    def __init__(self):
        '''
        This is the constructor for a table for SQL testing
        ''' 
        # Stores database on local machine
        self.db = sqlite3.connect(':memory:')
        # Formats SQL output string
        self.db.text_factory = str
        cur = self.db.cursor()
        self.init_db(cur)
        self.fill_table(cur,[('2014-06-03',3,'Coopers'), 
                            ('2014-06-05',5,'Bite Back'),
                            ('2014-06-07',3,'Anza Borrego'),
                            ('2014-06-11',14,'Broken Hill')]
                        )
        # Commits the SQL commands to the current machine
        self.db.commit()
        
    def init_db(self, cur):
        '''
        The init_db(...) method initiatilizes the SQL table.
        '''
        cur.execute('CREATE TABLE running({0} DATE, {1} INTEGER(15), {2} VARCHAR(15));'.format(self.COLUMNS[0],self.COLUMNS[1],self.COLUMNS[2]))
            
    def fill_table(self, cur, itr):
        ''' 
        Populates the table which cur points to using a list of tuples.
        '''
        cur.executemany('''
            INSERT INTO running 
            (Date,Miles,Trail)
            VALUES (?,?,?)''',itr)
            
    def print_table(self):
        '''
        Prints the SQL table a row at a time.
        '''
        
        for row in self.db.execute("SELECT * FROM " + self.TABLE_NAME):
            print row
        print '\n' + '*' * 10, 'Done', '*' * 10 + '\n'
        

def sql_insert_wrapper(table_name,cols,new_row):
    '''
    Constructs a string to insert a row into a sql table
    '''
    command = 'INSERT INTO ' + table_name
    variables = '(' + ','.join(cols) + ')'
    for i in range( len(new_row) ): 
        if isinstance(new_row[i], str):
            unformatted = new_row[i]
            new_row[i] = "'" + unformatted + "'"  
                
        else:
            unformatted = str(new_row[i])
            new_row[i] = unformatted      
                                            
    values = 'Values (' + ','.join(new_row) + ')'
    return command + '\n\t' + variables + '\n\t' + values + ';'
    
def sql_update_wrapper(table_name, cols = [], values = [], w_cols = [], w_ops = [],w_values = [],w_conts = []):
    '''
    Constructs a string to update a value in a sql table
    param: table_name, the name of the SQL table
    param: cols, a list of the column names for updating
    param: values, a list of the updating values
    param: w_cols, a list specifying the columns to change
    param: w_ops, a list of possible operators
    param: w_values, a list of values which set conditional statements
    param: w_conts, a list of AND's and OR's
    '''
    update_str = 'UPDATE ' + table_name
    set_list = []
    for var, value in zip(cols, values):
        set_list.append(str(var) + ' = ' + str(value))
    set_str = 'SET ' + ', '.join(set_list)
    if len(w_cols) > 0:
        where_str = 'WHERE '
        #will definitely have to fix this because you will have a problem trying to access all of the 
        #variables because w_ops will definitely be shorter than all of the rest of the lists and so you
        #cannot use zip()
        for var, value, op, i in zip(w_cols,w_values,w_ops, range(len(w_cols) + 1)):
            if i < len(w_cols) - 1:
                hold = where_str + ' '.join([var,op,str(value)]) + ' ' + w_conts[i]
            else:
                hold = where_str + ' '.join([var,op,str(value)]) + ' ' 
            where_str = hold 
        return update_str + '\n\t' + set_str + '\n\t' + where_str + ';'
    return update_str + '\n\t' + set_str + ';'    
        
def sql_advanced_select(self, table, column, w_col = None, w_opt = None,
    w_var = None,w_bool = None, group = None, h_col = None, h_bool = None, h_value = None):
    '''
    advanced SQL select function
    @param table - name of the table
    @param column - the columns to be selected
    @param w_col - column names for where clause
    @param w_opt - operator for where clause
    @param w_var - variable for where clause 
    @param w_bool - boolean for where clause
    @param group - group name for GROUP BY caluse
    @param h_col
    
    '''
    # check whether argument is valid or not
    # all the w_ variables must be all None or same size w_bool is less by 1
    if (w_col is not None and w_opt is not None and w_var is not None \
        and w_bool is not None):
        if (len(w_col) != len(w_opt) and len(w_opt) != len(w_var)\
            and len(w_var) != (len(w_bool) - 1)):
            raise Exception("Invalid arguement")
    elif(w_col is not None or w_opt is not None or w_var is not None \
         or w_bool is not None):
            raise Exception("Invalid arguement")

    # must have a table name
    if ( table is None or len(table) == 0):
        raise Exception("a table name must be provided.")

    Q = "SELECT "
    
    for i in range(len(column)):
        Q = Q + column[i]
        if (i != len(column) - 1):
            Q += ", "
        else:
            Q += " "
    Q += "\n" + "FROM " + table + " "

    if w_col is not None :
        Q = Q + "\n"+"WHERE "
        for i in range(len(w_col)):
            Q = Q + w_col[i] + " " + w_opt[i] + " " + str(w_var[i]) + " "
            if i < len(w_bool):
                Q = Q + w_bool[i] + " "

    if group is not None:
        Q += "\n" + "GROUP BY " + group
        
    if h_col is not None and h_bool is not None and h_value is not None:
        Q += "\n" + "HAVING " + h_col + " " +  h_bool + " " + str(h_value)
    Q +=";"
    
    return Q

def insert_into_database(cur,devices_row = None, transitions_row = None, intermediates_row = None):
    '''
    param: cursor, need a connection to the sql database (using sqlite3) in order to insert.
    param: device, list with information in corresponding device table location.
    param: transition, list with information in the corresponding transition table location.
    param: intermediate, list with the information in the corresponding intermediate table location.
    '''
    if devices_row is not None and len(devices_cols) == len(devices_row):
        sql_insert_wrapper('Devices', devices_cols, devices_row)
    if transitions_row is not None and len(transitions_cols) == len(transitions_row):
        sql_insert_wrapper('Transitions', transitions_cols, transitions_row)
    if intermediates_row is not None and len(intermediates_cols) == len(intermediates_row):    
        sql_insert_wrapper('Intermediates', intermediates_cols, intermediates_row)
            
def search_database(cur, devices_row = None, transitions_row = None, intermediates_row = None):
    '''
    '''
    if devices_row is not None:
        d = sql_advanced_search('Devices',...)
        d = cur.execute(d)
    if transitions_row is not None:
        t = sql_advanced_search('Transitions',...)
        t = cur.execute(t)
    if intermediates_row is not None:
        i = sql_advanced_search('Intermediates',...)
        i = cur.execute(i)
        

    
    
    
#Running the code using an SQLInterface object to comvert information from
#Python in to SQL commands. A running_table database is also                
base = sql_table()
base.db.execute(sql_insert_wrapper(base.TABLE_NAME,base.COLUMNS,['2014-06-30',14,'Chunk Rock']))
base.print_table()
print sql_update_wrapper(base.TABLE_NAME,['Miles'], [80] ,['Miles'], ['>'], [10])
base.db.execute(sql_update_wrapper(base.TABLE_NAME,['Miles'], [80] ,['Miles'], ['>'], [10]))
base.print_table()
base.db.execute(sql_update_wrapper(base.TABLE_NAME, ['Miles'], [15]))
base.print_table()

insert_into_database(['5', '4','3','2','1'])