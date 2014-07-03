# SQLInterface
# author: Joaquin Reyna
# date: 07/02/14
# description: SQLwrappers and testing

import sqlite3

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
        
        cur.execute('''CREATE TABLE running
                        ( Date DATE,
                          Miles INTEGER(15),
                          Trail VARCHAR(15)
                        );
                    '''
                    )
            
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

#Running the code using an SQLInterface object to comvert information from
#Python in to SQL commands. A running_table database is also                
base = sql_table()

base.db.execute(sql_insert_wrapper(base.TABLE_NAME,base.COLUMNS,['2014-06-30',14,'Chunk Rock']))
base.print_table()
#print sqlObj.sql_update_wrapper(base.table_name,['Miles'], [80] ,['Miles'], ['>'], [10])
base.db.execute(sql_update_wrapper(base.TABLE_NAME,['Miles'], [80] ,['Miles'], ['>'], [10]))
#base.print_table()
base.db.execute(sql_update_wrapper(base.TABLE_NAME, ['Miles'], [15]))
#base.print_table()
