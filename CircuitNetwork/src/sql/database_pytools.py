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
    cur = conn.cursor()
    if devices_row is not None and len(DEVICES_COLS) == len(devices_row):
        d = sql_insert('Devices', DEVICES_COLS, devices_row)
        cur.execute(d)
    if transitions_row is not None and len(TRANSITIONS_COLS) == len(transitions_row):
        t = sql_insert('Transitions', TRANSITIONS_COLS, transitions_row)
        cur.execute(t)
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
    cur = conn.cursor()
    if devices_row is not None and len(DEVICES_COLS) == len(devices_row):
        d = sql_update('Devices', DEVICES_COLS, devices_row)
        cur.execute(d)
    if transitions_row is not None and len(TRANSITIONS_COLS) == len(transitions_row):
        t = sql_update('Transitions', TRANSITIONS_COLS, transitions_row)
        cur.execute(t)
    if intermediates_row is not None and len(INTERMEDIATES_COLS) == len(intermediates_row):    
        i = sql_update('Intermediates', INTERMEDIATES_COLS, intermediates_row)
        cur.execute(i)
    cur.close()
    
            
def search_database(devices_row = None, transitions_row = None, intermediates_row = None):
    '''
    '''
    conn = sqlite3.connect('igemDBdevice.db.txt')
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
        
    return [d, t, i]
       
