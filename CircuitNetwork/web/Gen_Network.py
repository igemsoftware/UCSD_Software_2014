'''
//Title: SBML Network Generator 

//Description: 
    Translate entire network model to SBML and store network file 
    in current working directory  

*************************************************
@author: Fernando Contreras
@email: f2contre@gmail.com
@project: SBiDer
@institution: University of California, San Diego
*************************************************
'''
import sbml_database as sd
import SBML_Network as sn

#establish model object as a global variable 
global model
def create_whole_network_sbml():
	model = sn.Model()

	#construct operon/chemical species component of network SBML file 
	operon_dict = sd.get_sbml_operons()
	miriam_dict = sd.get_sbml_miriam_ids()
	for operon in operon_dict:
	    ope_spe = sn.QualitativeSpecies(operon,'plasmid',name=operon_dict[operon],miriam_id=miriam_dict[operon])  
	    ope_spe.appendToQualSpecies(model)

	species_dict = sd.get_sbml_species()
	for species in species_dict:
	    chem_spe = sn.QualitativeSpecies(species,'chemical_species',name=species_dict[species])  
	    chem_spe.appendToQualSpecies(model)

	#required intermediate SBML statements for network model 
	intermediate_step = sn.IntermediateStep(model)


	#construct input/output transition component of network SBML file 
	input_trans_dict  = sd.get_sbml_input_species_edges()
	input_operon = sd.get_sbml_input_operon_edges()
	trans_logic = sd.get_sbml_input_logic()
	for input in input_trans_dict:
	    in_trans_spe = sn.Transitions()
	    in_trans_spe.input_transition(model,input,input_trans_dict[input],input_operon[input],trans_logic[input])

	output_trans_dict = sd.get_sbml_output_species_edges()
	output_operon = sd.get_sbml_output_operon_edges()
	for output in output_trans_dict:
	    out_trans_spe = sn.Transitions()
	    out_trans_spe.output_transition(model,output,output_trans_dict[output],output_operon[output])   

	#required closing SBML statements for network model 
	close_model = sn.CloseModel(model)
	model.writeSBML("SBider_Network")
