<<<<<<< HEAD
import sql_pytools
import sqlite3

# Suggestion: it may be better to pass in a cursor object. That way you don't have to be
# connecting and reconnecting all of the time.

# static variables for tables in the sql database
# actually I cannot hard code these variables we may not return every single column every single time
DEVICES_COLS = ['NAME', 'COMPONENT', 'AUTHOR', 'ARTICLE', 'JOURNAL', 'YEAR', 'IMAGE_PATH']
TRANSITIONS_COLS = ['INPUT_SPECIES','OUTPUT_SPECIES','TYPE','FUNCTION']
INTERMEDIATES_COLS = ['NAME','TYPE','ANNOTATION']

def insert_into_database(devices_row = None, transitions_row = None, intermediates_row = None):
    '''
        param: cursor, need a connection to the sql database (using sqlite3) in order to insert.
        param: device, list with information in corresponding device table location.
        param: transition, list with information in the corresponding transition table location.
        param: intermediate, list with the information in the corresponding intermediate table location.
        '''
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
