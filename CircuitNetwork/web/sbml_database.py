'''
//Title: SBML Database Access

//Description: 
    Access SBiDer database and retrieve all necessary SBML information 

*************************************************
@author: Fernando Contreras
@email: f2contre@gmail.com
@project: SBiDer
@institution: University of California, San Diego
*************************************************
'''
import os
import sbider_database as sd
#open database
cwd = os.getcwd()
database_path = os.path.join(cwd,'sbider.db')
con,cursor = sd.db_open(database_path)

def get_sbml_miriam_ids():
    '''
    Access plasmid table and plasmid-operon relationship table to retrieve 
    the miriam ids of each operon
    
    @Output: dictionary = {operon id: miriam id}
        operon id: string type 
        miriam id: string type 
    '''
    devices = sd.db_select(cursor,'plasmid',['pla_id', 'PMID'])
    devices = devices.fetchall()
    plasmid_operon = sd.db_select(cursor,'plasmidoperon',['ope_id','pla_id'])
    plasmid_operon = plasmid_operon.fetchall()
    plasmid_miriam  = dict(devices)
    operon_miriam  =  {}
    for operon in plasmid_operon:
        operon_id = operon[0]
        plasmid_id = operon[1]
        if plasmid_id in plasmid_miriam:
            operon_miriam[operon_id] = plasmid_miriam[plasmid_id]
    return operon_miriam        

def get_sbml_operons():
    '''
    Access operon table to retrieve all relevant operon information
    
    @Output: dictionary = {operon id: operon name}
        key = operon id: string type
        value = operon name: string type 
    '''
    devices = sd.db_select(cursor,'operon',['ope_id','name'])
    devices = devices.fetchall()
    return dict(devices)

def get_sbml_species():
    '''
    Access chemical species table and retrieve all relevant species information 
    
    @Output: dictionary = {species id: species name}
        key = species id 
        value = species name  
    '''
    species  = sd.db_select(cursor,'species',['spe_id', 'name'])
    species = species.fetchall()
    return dict(species)
def get_sbml_input_species_edges():
    '''
    Access the input transition-chemical species relationship table and acquire 
    input species-transition edges
    
    @Output: dictionary = {it_id: [(spe_id, repressor_boolean)]}
        key = input transition id 
        value = list of associated input chemical species
            tuple = (chemical species, associated repressor boolean). If 
            chemical species is a repressor then repressor_boolean is 'True'
    '''
    IN = sd.db_select(cursor,'inputtransitionspecies', ['it_id','spe_id','repression'])
    IN = IN.fetchall()
    input_trans_species = {}
    for trans in IN:
        input_trans_id = trans[0]
        species_id = trans[1]
        repressor_bool  = trans[2]
        if input_trans_id not in input_trans_species:
            input_trans_species[input_trans_id] = []
            input_trans_species[input_trans_id].append((species_id,repressor_bool))
        else:
            input_trans_species[input_trans_id].append((species_id,repressor_bool))
    return input_trans_species
def get_sbml_output_species_edges():
    '''
    Access the output transition-chemical species relationship table and acquire 
    output species-transition edges
    
    @Output: dictionary = {ot_id: [spe_id]}
        key = output transition id 
        value = list of associated output chemical species
    '''
    OUT = sd.db_select(cursor,'outputtransitionspecies', ['ot_id','spe_id'])
    OUT = OUT.fetchall()
    output_trans_species = {}
    for trans in OUT:
        output_trans_id = trans[0]
        species_id = trans[1]
        if output_trans_id not in output_trans_species:
            output_trans_species[output_trans_id] = []
            output_trans_species[output_trans_id].append(species_id)
        else:
            output_trans_species[output_trans_id].append(species_id)
    return output_trans_species

def get_sbml_input_operon_edges():
    ''' 
    Access the input transition-operon relationship table and acquire 
    input transition-operon edges
    
    @Output: dictionary = {it_id: ope_id}
        key = input transition id 
        value = operon id 
    '''
    operon_in_trans = sd.db_select(cursor, 'OperonInputTransition',['it_id','ope_id'])
    operon_in_trans = operon_in_trans.fetchall()
    return dict(operon_in_trans)

def get_sbml_output_operon_edges():
    ''' 
    Access the output transition-operon relationship table and acquire 
    output transition-operon edges
    
    @Output: dictionary = {ot_id: ope_id}
        key = output transition id 
        value = operon id 
    '''
    operon_out_trans = sd.db_select(cursor, 'OperonOutputTransition',['ot_id','ope_id'])
    operon_out_trans = operon_out_trans.fetchall()
    return dict(operon_out_trans)

def get_sbml_input_logic():
    ''' 
    Access the input transition logic table and acquire 
    input transition Boolean logic
    
    @Output: dictionary = {it_id: logic}
        key = input transition id 
        value = associated Boolean logic  
    '''
    in_logic = sd.db_select(cursor, 'InputTransition',['it_id','logic'])
    in_logic = in_logic.fetchall()
    return dict(in_logic)
