from sql_pytools import *
import sqlite3


# Suggestion: it may be better to pass in a cursor object. That way you don't have to be
# connecting and reconnecting all of the time. 

# static variables for tables in the sql database
# actually I cannot hard code these variables we may not return every single column every single time
DEVICES_COLS = ['Name', 'Components', 'Authors', 'Article', 'Journal', 'Image_Path']
TRANSITIONS_COLS = ['Input_Species', 'Output_Species', 'Math']
INTERMEDIATES_COLS = ['Name', 'Type', 'MARIAM', 'PromoterInteractionList', 'Annotation']
PROMOTER_COLS = ['Name', 'Regulators', 'Sequence', 'Annotation']
CDS_CIS = ['Name', 'Sequence', 'Annotation']

def get_table_header(table_name):
    if table_name == 'devices_row':
        return DEVICES_COLS
    elif table_name == 'transitions_row':
        return TRANSITIONS_COLS
    elif table_name == 'intermediates_row':
        return INTERMEDIATES_COLS
    #elif table_name == 'promoters_row':
        #return PROMOTERS_COLS
     #elif table_name == 'cds_row':
        #return CDS_COLS
    else:
        return []
    

def insert_into_database(devices_row = None, transitions_row = None, intermediates_row = None, promoters_row = None, cds_row = None):
    '''
    param: cursor, need a connection to the sql database (using sqlite3) in order to insert.
    param: device, list with information in corresponding device table location.
    param: transition, list with information in the corresponding transition table location.
    param: intermediate, list with the information in the corresponding intermediate table location.
    '''
    parameters = locals().items()
    conn = sqlite3.connect('igemDBdevice.db.txt')
    cur = conn.cursor()
    for table_row, table_values in parameters:
        print 'table', table_row
        print 'values',table_values
        if table_values != None:
            table_header = get_table_header(table_row)
            print 'header',table_header
            if len(table_header) == len(table_values):
                table_name = table_row.replace("_row","").title()
                print 'table_name',table_name
                sql_cmd = sql_insert(table_name, table_header, table_values)
                print 'sql_cmd',sql_cmd
                cur.execute(sql_cmd)
            elif len(table_header) != len(table_values):
                raise TypeError( 'Missing values:', table_row, 'has', len(table_values), '.\n',
                    'You need a total of', len(table_header), '.')
    cur.close()
    
def update_database(devices_row = None, transitions_row = None, intermediates_row = None, promoters_row = None, cds_row = None):
    '''
    param: cursor, need a connection to the sql database (using sqlite3) in order to insert.
    param: device, list with information in corresponding device table location.
    param: transition, list with information in the corresponding transition table location.
    param: intermediate, list with the information in the corresponding intermediate table location.
    '''
    conn = sqlite3.connect('igemDBdevice.db.txt')
    cur = conn.cursor()
    tables = locals()
    
    for table_row, table_values in tables:
        table_header = get_table_header(table_row)
        if table_row is not None and len(table_header) == len(table_values):
            table_name = table_row.replace("_row","").title()
            sql_cmd = sql_update(table_name, table_header, table_values)
            cur.execute(sql_cmd)
            
        elif len(table_header) is not len(table_values):
            raise TypeError( 'Missing values:', table_row, 'has', len(table_values), '.\n', 
                'You need a total of', len(table_header), '.')
    cur.close()
    
            
def select_database(table, column, w_col = None, w_opt = None,
    w_var = None,w_bool = None, group = None, h_col = None, h_bool = None, h_value = None):
    '''
    '''
    conn = sqlite3.connect('igemDBdevice.db.txt')
    cur = conn.cursor()
    sql_cmd = sql_search(table, column, w_col = None, w_opt = None,
        w_var = None,w_bool = None, group = None, h_col = None, h_bool = None, h_value = None)
    cur.execute(sql_cmd)
    selection = cur.fetchall()
    cur.close()
        
    return selection
        
