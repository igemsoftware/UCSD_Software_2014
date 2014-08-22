from sql_pytools import *
import sqlite3


# Suggestion: it may be better to pass in a cursor object. That way you don't have to be
# connecting and reconnecting all of the time. 
# Suggestion #2: Might also think about making a class that quickly can capture the bool
# logic that is happening. This would make transitions objects. 
# Suggestion #3: In order to capture bool logic for or you may need a list that 
# separates transitions by the or placement. 
# Suggestion #4: May need make methods that also return only the name of each genetic part
sqlconn = sqlite3.connect("")
sql = sqlconn.cursor()

#############WORKING!!#############
#Declaring list global variables for integration with accession functions
plasmid_table = []
operon_table = []
part_table = []
interactor_table = []
opr_table = []
optr_table = []
oitr_table = []
ootr_table = []
input_trans_table = []
output_trans_table = []

#############WORKING!!#############

def database_to_json():
    '''
    Obtain nodes and edge information and parse into json
    '''

def database_to_pigeon():
    '''
    Obtain operon information and parse into pigeonCAD string commands
    '''
def get_all_interactors_ID():
    '''
    Return all interactor ID's
    '''
def get_all_parts():
    '''
    Return all parts_ID's
    '''
def get_all_operon_plasmid_rlts()
    '''
    Return a list of tuples with Operon_ID and Plasmid_ID
    '''
def get_all_operon_part_rlts()
    '''
    Return a list of tuples with Operon_ID and Part_ID
    '''
def get_all_operon_in_trans_rlts()
    '''
    Return a list of tuples with Operon_ID and Input_Transition_ID
    '''
def get_all_operon_out_trans_rlts()
    '''
    Return a list of tuples with Operon_ID and Output Transition ID
    '''
def get_all_operon_plasmid_rlts()
    '''
    Return a list of tuples with Operon_ID and Plasmid_ID
    '''
def get_all_operon_plasmid_rlts()
    '''
    Return a list of tuples with Operon_ID and Plasmid_ID
    '''
def get_all_input_transitions()
    '''
    Return a list of lists with ...
    '''
    
    
    
    
    
    
    
    
    
    
#############DONE!#############    
    
def get_all_input_trans_ID():
    '''
    Return all of the input transitions ID's
    '''
    return unlist_values(sql.execute("SELECT ID from input_trans"))
    
def get_all_operon_ID():
    '''
    Return all of the operon ID's
    '''
    return unlist_values(sql.execute("SELECT ID from operon"))
    
def get_all_plasmid_ID():
    '''
    Return all the plasmid ID's
    '''
    return unlist(sql.execute("SELECT ID from plasmid"))
    
def single_trans_to_bool(trans_ID):
    '''
    Determine the boolean logic of a single transition using the ID
    @param trans_ID, the transition for which logic is desired
    '''
    trans_list = sql.execute('''SELECT Interactor_ID, NOT/
        FROM input_trans WHERE Input_Transition_ID = ''' + trans_ID)
    return bool_trans(trans_list)

def single_operon_to_bool(operon_ID)
    '''
    Determine the boolean logic of a single operon using the ID
    @param operon_ID, the operon for which logic is desired
    '''
    operon_list = sql.execute('''SELECT Input_Transition_ID from oitr 
        where Operon_ID = ''' + operon_ID)
    operon_list = unlist_values(operon_list)
    operon_list = [single_trans_to_bool(x) for x in operon_list]
    if len(operon_list) = 1:
        return operon_list
    else:
        return ' OR '.join(operon_list)
        
def unlist_values(to_list)
    '''
    Stringify values in a list that are within a list
    @param to_list, a list with lists of single values
    '''
    return [''.join(x) for x in to_list]
    

def database_to_trans_logic():
    '''
    Determine the boolean logic for all transitions in the database
    '''
    #Collecting all of the transition-interactor information inside of a dictionary 
        #Key: trans_ID
        #Value: List of [[interactor1, not_boolean1], [interactor2, not_boolean2], ...]
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
            if i = 0:
                if interactor[0][1] == False:
                    bool_string += str(interactor[0][0])
                else:
                    bool_string += "NOT " + str(interactor[0][0])
            else: 
                if i = 0:
                    if interactor[0][1] == False:
                        bool_string += " AND " + str(interactor[0][0])
                    else:
                        bool_string += " AND NOT " + str(interactor[0][0])
        return bool_string
        
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
    

    

        
            