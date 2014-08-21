from sql_pytools import *
import sqlite3


# Suggestion: it may be better to pass in a cursor object. That way you don't have to be
# connecting and reconnecting all of the time. 
# Suggestion #2: Might also think about making a class that quickly can capture the bool
# logic that is happening. This would make transitions objects. 
# Suggestion #3: In order to capture bool logic for or you may need a list that 
# separates transitions by the or placement. 

def database_to_json():

def database_to_pigeon()

def database_to_trans_logic():
    '''
    Determine the boolean logic for all transitions in the database
    '''
    #collecting all of the transition information
    trans_list = sql.execute("SELECT Interactor_ID, Input_Transition_ID, NOT)
    trans_dict = {}
    for trans in trans_list:
        trans_ID = trans[1]
        if trans_ID in trans_dict:
            trans_dict[trans_ID].append([trans[0]] + [trans[2]])
        else:
            trans_dict[trans_ID] = [trans[0]] + [trans[2]]
    
    #creating a list of all of the transitions
    trans_bool_dict = {}
    for interactor, bool in trans_dict:
    '''        
    #Collecting all of the transition logic        
    logic_list = []
    for trans in trans_dict.values() 
        logic_list.append(bool_single_trans(trans))
    ''' 
            
def bool_trans(interactor): 
    '''
    Determine the boolean logic of a NOT/AND/IF input transition
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
                
            
            
        return  "AND" #interactor[0][0] maybe also return the i_ID's
        
def database_to_bool_operon()
    '''
    Determine the boolean logic of the whole operon
    '''
    operon_trans_list = sql.execute('grab all of the operons and transitions')
    for rlts in operon_trans_list:
        operon = rlts[0] 
        if operon in operon_trans_dict:
            operon_trans_dict[operon].append(operon[1])
        else:
            operon_trans_dict[operon] = [operon[0]]
    
    operon_logic_list = []
    for operon in operon_trans_dict.values():
        if len(operon_trans_dict[operon]) == 1:
            