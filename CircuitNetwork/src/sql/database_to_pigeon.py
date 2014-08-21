import sqlite3

def plasmid_to_operon_list(plasmid_name):
    '''
    Returns a list of dictionaries containing information about the each operon
    '''
    plasmid_list = []
    plasmid_info = cur.execute('SELECT Operon_id, Directionality FROM POR WHERE Plasmid_id EQUALS' + plasmid_name)
    for item in plasmid_info:
        operon = operon_to_dict(*item)
        plasmid_list.append(operon)
    return plasmid
    
    #example plasmid
    #print plasmid --> [{operon1},{operon2},{operon3},..., operon{n}]
    
def operon_to_dict(operon_id, operon_direction = 'R'):
    '''
    Returns a single dictionary with information about an operon's directionality and components
    '''
    components_list = cur.execute('SELECT Components FROM OCR WHERE Operon_id EQUALS' + operon_id)    
    for component, i in components_list, len(components_list):
        #specifies if the given component is a promoter. Will have to change later to be careful about 
        #non-promoter components starting with a p.  
        if component[i][0] == 'p':
            component[i][0] = 'p', component[i][0]
        else:
            component[i][0] = 'c', component[i][0]
        component = ''.join(component)
    operon = {'directionality': operon_direction, 'components': components_list}
    return operon
    
    #example operon
    #print operon['components'] --> ['p plas','c luxR']
    #print operon['directionality'] --> 'R' or 'L'
    
def select_operon():
    conn = sqlite3.connect()
    cur = conn.cursor()
    conn.close()
