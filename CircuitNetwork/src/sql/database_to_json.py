import sqlite3
import js

def increment_level
#obtains information for interactor nodes
def database_to_interactor_node(i_id, name):
    data = '\s' * 6 + '"data" : { + \n'
    data += '\s' * 8 + 'id : "%s",',i_id
#obtains information particular for transition nodes
def database_to_transition_node(o_id, name): 
#gives the position for each node
def node_position():
    
def database_to_json():
    conn = sqlite3.connection('')
    cur = conn.cursor()
    header = '''
    {
     "format_version" : "1.0",
     "generated_by" : "cytoscape-3.1.1",
     "target_cytoscapejs_version" : "~2.1",
     "data" : {
       "selected" : true,
       "__Annotations" : [ ],
       "shared_name" : "galFiltered.sif",
       "SUID" : 52,
       "name" : "galFiltered.sif"
    },
    "elements" : {
      "nodes" : [ {'''
    #making all of the transitions nodes
    cur.execute('SELECT O_ID, Name FROM Operon')
    transitions = cur.fetchall()
    
    cur.execute('SELECT I_ID, Name from Interactors')
    places = cur.fetchall()
    
    
    
    return #string
    