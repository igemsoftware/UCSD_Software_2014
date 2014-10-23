'''
//Title: SBML Node Generator 

//Description: 
    Translate individual node information to SBML and store node file 
    in current working directory  

*************************************************
@author: Fernando Contreras
@email: f2contre@gmail.com
@project: SBiDer
@institution: University of California, San Diego
*************************************************
'''
import SBML_Nodes as sn
'''
IMPORTANT: ALL INPUTS ARE STRING TYPES!
'''
#construct operon/chemical species component of network SBML file 
def sbml_operon(operon_id,operon_name,miriam_id,filename):
    compartment = 'plasmid'
    operon_node=sn.Nodes()
    ope_spe = sn.QualitativeSpecies(operon_id,compartment,name=operon_name, miriam_id=miriam_id)  
    ope_spe.appendToQualSpecies(operon_node)
    operon_node.writeQualSpecies(str(filename))

def sbml_species(species_id, species_name,filename):
    compartment = 'chemical_species'
    species_node=sn.Nodes()
    chem_spe = sn.QualitativeSpecies(species_id,compartment,name=species_name)  
    chem_spe.appendToQualSpecies(species_node)
    species_node.writeQualSpecies(str(filename))

#construct input/output transition component of network SBML file
def sbml_input_trans(trans_id,input_species_id_and_boolean_tuple,operon_id,trans_logic,filename):
    in_trans = sn.Nodes()
    in_trans_spe = sn.Transitions()
    in_trans_spe.input_transition(in_trans,trans_id,input_species_id_and_boolean_tuple,operon_id,trans_logic)
    in_trans.writeTransition(str(filename))

def sbml_output_trans(trans_id,output_species_id,operon_id,filename):
    out_trans = sn.Nodes()
    out_trans_spe = sn.Transitions()
    out_trans_spe.output_transition(out_trans,trans_id,output_species_id,operon_id)       
    out_trans.writeTransition(str(filename))
