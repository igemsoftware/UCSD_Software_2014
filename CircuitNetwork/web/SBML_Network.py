'''
//Title: SBML Network Constructor. 

//Description: 
    Each class generates a corresponding SBML description of the input information 
    and appends the information to a list which is then written to file

*************************************************
@author: Fernando Contreras
@email: f2contre@gmail.com
@project: SBiDer
@institution: University of California, San Diego
*************************************************
'''
import os
class Model():
    '''
        Creates a model object. When instantiated the class appends all the URLs 
        necessary to understand our network model
    '''
    def __init__(self, id = 'SBider_Network' ):
        self.id  = id
        self.sbml= []
        self.sbml.append('<?xml version="1.0" encoding="UTF8"?>\n')
        self.sbml.append('<sbml xmlns="http://www.sbml.org/sbml/level3/version1/core" level="3" version="1"\n')   
        self.sbml.append('\txmlns:qual="http://www.sbml.org/sbml/level3/version1/qual/version1" qual:required="true">\n\n') 
        self.sbml.append('\tmiriam id:qual="http://www.ebi.ac.uk/miriam/main/mdb?section=intro" qual:required="false">\n\n')
        self.sbml.append('\t<model id="%s">\n\n'%self.id)
        self.sbml.append('\t\t<listOfCompartments>\n')
        self.sbml.append('\t\t\t<comparment id="plasmid" name="plasmid" constant="true"/>\n')
        self.sbml.append('\t\t\t<comparment id="chemical_species" name="chemical_species" constant="true"/>\n')   
        self.sbml.append('\t\t</listOfCompartments>\n')
        self.sbml.append('\t\t<qual:listOfQualitativeSpecies>\n')
    def writeSBML(self, filename):
        '''
        @Parameters: 
            filename: desired file name for network file 
            type: string 
        
        @Method:
            Write SBML formatted network model text file. File is then stored in 
            the current working directory.  
        '''
        cwd = os.getcwd()
        absolute_path = os.path.join(cwd,str(filename)+".txt")
        with open(absolute_path, 'w') as sbml_file:
            sbml_file.writelines(self.sbml)

class QualitativeSpecies():
    ''' Qualitative species, such as operons and chemical species, constructor '''
    def __init__(self,id,compartment, name = 'NONE', maxLevel = '1', constant = 'false', miriam_id = 'NONE'):
        '''
        @Parameters:
            id: node id 
            compartment: node compartment, for example, operons belong in the plasmid compartment
            name: node name, default=NONE because operons don't have a name 
            maxLevel: node threshold, default = 1 because a logic model was implemented 
            constant: denotes node passivity, if constant = True then the node does not interact with 
            network. Thus, the node does not transfer information.
            miriam_id: Minimal Information Required in the Annotation of Models id. This allows for 
            a standarized citation of literature references 
        
        @Method:
            Translate all the inputed information to SBML and append to list 
        '''
        self.id = id 
        self.name = name 
        self.compartment = compartment
        self.maxLevel = maxLevel
        self.constant = constant
        self.miriam_id = miriam_id 
    def appendToQualSpecies(self, model_name):
        if self.compartment == 'plasmid':
            self.id = "ope_"+self.id
            model_name.sbml.append('\t\t\t<qual:qualitativeSpecies    qual:compartment="%s" qual:constant="%s"\n'%(self.compartment, self.constant))
            model_name.sbml.append('\t\t\t\t\t\tqual:id="%s" qual:maxLevel="%s"/>\n'%(self.id,self.maxLevel))
            model_name.sbml.append('\t\t\t\t\t\tqual:name="%s" qual:miriam id="%s"/>\n'%(self.name,self.miriam_id))
        elif self.compartment == 'chemical_species':
            self.id = "spe_"+self.id
            model_name.sbml.append('\t\t\t<qual:qualitativeSpecies    qual:compartment="%s" qual:constant="%s"\n'%(self.compartment, self.constant))
            model_name.sbml.append('\t\t\t\t\t\tqual:id="%s" qual:maxLevel="%s"\n'%(self.id,self.maxLevel))
            model_name.sbml.append('\t\t\t\t\t\tqual:name="%s"/>\n'%self.name)
           

class Transitions():
    ''' 
    Input and output transition constructor; transitions denote the operon's input 
    and output reaction in our network. 
    '''
    def input_transition(self,model_name,trans_id,input_id_boolean_tuple,operon_id,trans_logic):
        '''
        @Parameters:
            node_name: name of node object, instantiated using the Node class 
            trans_id: transition id 
            input_id_boolean_tuple: tuple of the form (input chemical species, repressor boolean)
                input chemical species: chemical species involved in reaction 
                repressor boolean: denotes whether a chemical species is a repressor (True or False)
                Can input a list if multiple operators are involved, such is the case for an AND gate 
            operon_id: operon id 
            trans_logic: transition logic denotes the Boolean logic of a reaction ('AND', 'OR', 'NOT')
            
        @Method:
            Translate all the inputed information to SBML and append to list
        '''
        model_name.sbml.append('\t\t\t<qual:transtion qual:id="%s">\n'%("it_"+trans_id))
        if trans_logic.lower() == 'and':
            input_ids = []
            model_name.sbml.append('\t\t\t\t<qual:listOfInputs>\n')
            for species_input_bool in input_id_boolean_tuple:
                input_ids.append(species_input_bool[0])
                model_name.sbml.append('\t\t\t\t\t<qual:input qual:id="theta_%s"        qual:qualitativeSpecies="%s"\n'%("spe_"+species_input_bool[0],"spe_"+species_input_bool[0]))                
                model_name.sbml.append('\t\t\t\t\t\t    qual:thresholdLevel="1"   qual:transitionEffect="none"\n')
                if species_input_bool[1].lower() == 'true':
                    model_name.sbml.append('\t\t\t\t\t\t    qual:sign="negative"/>\n')
                elif species_input_bool[1].lower == 'false':
                    model_name.sbml.append('\t\t\t\t\t\t    qual:sign="positive"/>\n')
            model_name.sbml.append('\t\t\t\t</qual:listOfInputs>\n')  
            model_name.sbml.append('\t\t\t\t<qual:listOfOutputs>\n')
            model_name.sbml.append('\t\t\t\t\t<qual:output qual:qualitativeSpecies="%s"\n'%("ope_"+operon_id))
            model_name.sbml.append('\t\t\t\t\t\t     qual:transitionEffect="assignmentLevel"/>\n')
            model_name.sbml.append('\t\t\t\t</qual:listOfOutputs>\n')
            model_name.sbml.append('\t\t\t\t<qual:listOfFunctionTerms>\n')
            model_name.sbml.append('\t\t\t\t\t<qual:functionTerm qual:resultLevel="1">\n')
            model_name.sbml.append('\t\t\t\t\t\t<math xmlns="http://www.w3.org/1998/Math/MathML">\n')
            model_name.sbml.append('\t\t\t\t\t\t\t<!-- input_1 >= 1 and input_2 >= 1 -->\n')
            model_name.sbml.append('\t\t\t\t\t\t\t<apply>\n')
            model_name.sbml.append('\t\t\t\t\t\t\t\t<and/>\n')
            model_name.sbml.append('\t\t\t\t\t\t\t\t<apply>\n')
            model_name.sbml.append('\t\t\t\t\t\t\t\t\t<geq/>\n')
            model_name.sbml.append('\t\t\t\t\t\t\t\t\t<ci>%s</ci>\n'%("spe_"+input_ids[0]))
            model_name.sbml.append('\t\t\t\t\t\t\t\t\t<ci>theta_%s</ci>\n'%("spe_"+input_ids[0]))
            model_name.sbml.append('\t\t\t\t\t\t\t\t</apply>\n')
            model_name.sbml.append('\t\t\t\t\t\t\t\t<apply>\n')
            model_name.sbml.append('\t\t\t\t\t\t\t\t\t<geq/>\n')
            model_name.sbml.append('\t\t\t\t\t\t\t\t\t<ci>%s</ci>\n'%("spe_"+input_ids[1]))
            model_name.sbml.append('\t\t\t\t\t\t\t\t\t<ci>theta_%s</ci>\n'%("spe_"+input_ids[1]))
            model_name.sbml.append('\t\t\t\t\t\t\t\t</apply>\n')
            model_name.sbml.append('\t\t\t\t\t\t\t</apply>\n')
            model_name.sbml.append('\t\t\t\t\t\t</math>\n')
            model_name.sbml.append('\t\t\t\t\t</qual:funtionTerm>\n')
            model_name.sbml.append('\t\t\t\t\t<qual:defaultTerm qual:resultLevel="0"/>\n')
            model_name.sbml.append('\t\t\t\t</qual:listOfFunctionTerms>\n')
            model_name.sbml.append('\t\t\t</qual:transition>\n') 
        elif trans_logic.lower() == 'or':
            input_id_bool = input_id_boolean_tuple[0]
            input_id = "spe_"+input_id_bool[0]  
            boolean = input_id_bool[1]         
            model_name.sbml.append('\t\t\t\t<qual:listOfInputs>\n')
            model_name.sbml.append('\t\t\t\t\t<qual:input qual:id="theta_%s"        qual:qualitativeSpecies="%s"\n'%(input_id,input_id))                
            model_name.sbml.append('\t\t\t\t\t\t    qual:thresholdLevel="1"   qual:transitionEffect="none"\n')
            if boolean.lower() == 'true':
                model_name.sbml.append('\t\t\t\t\t\t    qual:sign="negative"/>\n')
            elif boolean.lower() == 'false':
                model_name.sbml.append('\t\t\t\t\t\t    qual:sign="positive"/>\n')
            model_name.sbml.append('\t\t\t\t</qual:listOfInputs>\n')  
            model_name.sbml.append('\t\t\t\t<qual:listOfOutputs>\n')
            model_name.sbml.append('\t\t\t\t\t<qual:output    qual:qualitativeSpecies="%s"\n'%("ope_"+operon_id))
            model_name.sbml.append('\t\t\t\t\t\t     qual:transitionEffect="assignmentLevel"/>\n')
            model_name.sbml.append('\t\t\t\t</qual:listOfOutputs>\n')
            model_name.sbml.append('\t\t\t\t<qual:listOfFunctionTerms>\n')
            model_name.sbml.append('\t\t\t\t\t<qual:functionTerm qual:resultLevel="1">\n')
            model_name.sbml.append('\t\t\t\t\t\t<math xmlns="http://www.w3.org/1998/Math/MathML">\n')
            model_name.sbml.append('\t\t\t\t\t\t\t<!-- input >= 1-->\n')
            model_name.sbml.append('\t\t\t\t\t\t\t<apply>\n')
            model_name.sbml.append('\t\t\t\t\t\t\t\t<geq/>\n')
            model_name.sbml.append('\t\t\t\t\t\t\t\t<ci>%s</ci>\n'%input_id)
            model_name.sbml.append('\t\t\t\t\t\t\t\t<ci>theta_%s</ci>\n'%input_id)
            model_name.sbml.append('\t\t\t\t\t\t\t</apply>\n')
            model_name.sbml.append('\t\t\t\t\t\t</math>\n')
            model_name.sbml.append('\t\t\t\t\t</qual:funtionTerm>\n')
            model_name.sbml.append('\t\t\t\t\t<qual:defaultTerm qual:resultLevel="0"/>\n')
            model_name.sbml.append('\t\t\t\t</qual:listOfFunctionTerms>\n')
            model_name.sbml.append('\t\t\t</qual:transition>\n') 
        
    
    def output_transition(self,model_name,trans_id,output_id,operon_id):
        '''
        @Parameters:
            node_name: name of node object, instantiated using the Node class 
            trans_id: transition id 
            output_id: single variable input which denotes the id of an operon's output
            operon_id: operon id 
            
        @Method:
            Translate all the inputed information to SBML and append to list
        '''
        model_name.sbml.append('\t\t\t<qual:transtion qual:id="%s">\n'%("ot_"+trans_id))
        model_name.sbml.append('\t\t\t\t<qual:listOfInputs>\n')
        model_name.sbml.append('\t\t\t\t\t<qual:input qual:id="theta_%s"        qual:qualitativeSpecies="%s"\n'%("ope_"+operon_id,"ope_"+operon_id))                
        model_name.sbml.append('\t\t\t\t\t\t    qual:thresholdLevel="1"   qual:transitionEffect="none"\n')
        model_name.sbml.append('\t\t\t\t\t\t    qual:sign="positive"/>\n')
        model_name.sbml.append('\t\t\t\t</qual:listOfInputs>\n')
        if len(output_id) > 1:
            model_name.sbml.append('\t\t\t\t<qual:listOfOutputs>\n')
            for spe_output in output_id:
                model_name.sbml.append('\t\t\t\t\t<qual:output qual:qualitativeSpecies="%s"\n'%("spe_"+spe_output))
                model_name.sbml.append('\t\t\t\t\t\t     qual:transitionEffect="assignmentLevel"/>\n')
            model_name.sbml.append('\t\t\t\t</qual:listOfOutputs>\n')    
        else:
            model_name.sbml.append('\t\t\t\t<qual:listOfOutputs>\n')
            model_name.sbml.append('\t\t\t\t\t<qual:output    qual:qualitativeSpecies="%s"\n'%("spe_"+output_id[0]))
            model_name.sbml.append('\t\t\t\t\t\t     qual:transitionEffect="assignmentLevel"/>\n')
            model_name.sbml.append('\t\t\t\t</qual:listOfOutputs>\n')
        model_name.sbml.append('\t\t\t\t<qual:listOfFunctionTerms>\n')
        model_name.sbml.append('\t\t\t\t\t<qual:functionTerm qual:resultLevel="1">\n')
        model_name.sbml.append('\t\t\t\t\t\t<math xmlns="http://www.w3.org/1998/Math/MathML">\n')
        model_name.sbml.append('\t\t\t\t\t\t\t<!-- input >= 1-->\n')
        model_name.sbml.append('\t\t\t\t\t\t\t<apply>\n')
        model_name.sbml.append('\t\t\t\t\t\t\t\t<geq/>\n')
        model_name.sbml.append('\t\t\t\t\t\t\t\t<ci>%s</ci>\n'%("ope_"+operon_id))
        model_name.sbml.append('\t\t\t\t\t\t\t\t<ci>theta_%s</ci>\n'%("ope_"+operon_id))
        model_name.sbml.append('\t\t\t\t\t\t\t</apply>\n')
        model_name.sbml.append('\t\t\t\t\t\t</math>\n')
        model_name.sbml.append('\t\t\t\t\t</qual:funtionTerm>\n')
        model_name.sbml.append('\t\t\t\t\t<qual:defaultTerm qual:resultLevel="0"/>\n')
        model_name.sbml.append('\t\t\t\t</qual:listOfFunctionTerms>\n')
        model_name.sbml.append('\t\t\t</qual:transition>\n')
        
class IntermediateStep():
    ''' Require class, need to append necessary SBML statements for network model '''
    def __init__(self,model_name):
        '''
        @Parameter:
            model_name: model object, instantiated using Model class
        '''
        model_name.sbml.append('\t\t</qual:listOfQualitativeSpecies>\n')
        model_name.sbml.append('\t\t<qual:listOfTransitions>\n')
class CloseModel():
    ''' Require class, need to append closing SBML statements for network model '''
    def __init__(self,model_name):
        '''
        @Parameter:
            model_name: model object, instantiated using Model class
        '''
        model_name.sbml.append('\t\t</qual:listOfTransitions>\n')
        model_name.sbml.append('\t</model>\n')
        model_name.sbml.append('</sbml>\n') 