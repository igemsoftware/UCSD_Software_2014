'''
//Title: SBML Node Constructor. 

//Description: 
    Each class generates a corresponding SBML description of the input information.

*************************************************
@author: Fernando Contreras
@email: f2contre@gmail.com
@project: SBiDer
@institution: University of California, San Diego
*************************************************
'''
import os
class Nodes():
    '''
    Place, passive component of Petri Net model, and transition, active component 
    of Petri Net model, file constructor.When instantiated, a qualitative species 
    list and a transitions list are created. Data is then stored according to 
    SBML standards. 
    
    '''
    def __init__(self):
        '''
        Instantiate qualitative species and transitions list objects 
        '''
        self.qualitative_species = []
        self.transitions = []
    def writeQualSpecies(self, filename):
        '''
        @Parameters: filename
            type: string 
            description: desired file name for a particular qualitative species
            SBML text file(i.e. operon or chemical species)
        @Method:
            Write SBML text file for a qualitative species stored in the qualitative 
            species list object. File is then stored in the current working directory.  
        '''
        cwd = os.getcwd()                 
        absolute_path = os.path.join(cwd,str(filename)+".txt")
        with open(absolute_path, 'w') as species_file:
            species_file.writelines(self.qualitative_species)
    def writeTransition(self,filename):
        '''
        @Parameters: filename
            type: string 
            description: desired file name for a particular transition SBML text 
            file(i.e. input transition or output transition)
        @Method:
            Write SBML text file for a transition stored in the transition list 
            object. File is then stored in the current working directory.  
        '''
        cwd = os.getcwd()
        absolute_path = os.path.join(cwd,str(filename)+".txt")
        with open(absolute_path, 'w') as trans_file:
            trans_file.writelines(self.transitions)


class QualitativeSpecies():
    ''' Qualitative species, such as operons and chemical species, constructor'''
    def __init__(self,id,compartment, name = 'NONE', maxLevel = '1', constant = 'false',miriam_id = 'NONE'):
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
    def appendToQualSpecies(self, node_name):
        if self.compartment == 'plasmid':
            self.id = "ope_"+self.id
            node_name.qualitative_species.append('<qual:listOfQualitativeSpecies>\n')
            node_name.qualitative_species.append('\t<qual:qualitativeSpecies    qual:compartment="%s" qual:constant="%s"\n'%(self.compartment, self.constant))
            node_name.qualitative_species.append('\t\t\t\tqual:id="%s" qual:maxLevel="%s"/>\n'%(self.id,self.maxLevel))
            node_name.qualitative_species.append('\t\t\t\tqual:name="%s" qual:miriam id="%s"/>\n'%(self.name,self.miriam_id))
            node_name.qualitative_species.append('</qual:listOfQualitativeSpecies>')
        elif self.compartment == 'chemical_species':
            self.id = "spe_"+self.id
            node_name.qualitative_species.append('<qual:listOfQualitativeSpecies>\n')
            node_name.qualitative_species.append('\t<qual:qualitativeSpecies    qual:compartment="%s" qual:constant="%s"\n'%(self.compartment, self.constant))
            node_name.qualitative_species.append('\t\t\t\tqual:id="%s" qual:maxLevel="%s"\n'%(self.id,self.maxLevel))
            node_name.qualitative_species.append('\t\t\t\tqual:name="%s"/>\n'%self.name)
            node_name.qualitative_species.append('</qual:listOfQualitativeSpecies>')
        

class Transitions():
    ''' 
    Input and output transition constructor; transitions denote the operon's input 
    and output reaction in our network. 
    '''
    def input_transition(self,node_name,trans_id,input_id_boolean_tuple,operon_id,trans_logic):
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
        node_name.transitions.append('<qual:listOfTransitions>\n')
        node_name.transitions.append('\t<qual:transtion qual:id="%s">\n'%("it_"+trans_id))
        if trans_logic.lower() == 'and':
            input_ids = []
            node_name.transitions.append('\t\t<qual:listOfInputs>\n')
            for species_input_bool in input_id_boolean_tuple:
                input_ids.append(species_input_bool[0])
                node_name.transitions.append('\t\t\t<qual:input qual:id="theta_%s"        qual:qualitativeSpecies="%s"\n'%("spe_"+species_input_bool[0],"spe_"+species_input_bool[0]))                
                node_name.transitions.append('\t\t\t\t    qual:thresholdLevel="1"   qual:transitionEffect="none"\n')
                if species_input_bool[1].lower() == 'true':
                    node_name.transitions.append('\t\t\t\t    qual:sign="negative"/>\n')
                elif species_input_bool[1].lower() == 'false':
                    node_name.transitions.append('\t\t\t\t    qual:sign="positive"/>\n')
            node_name.transitions.append('\t\t</qual:listOfInputs>\n')   
            node_name.transitions.append('\t\t<qual:listOfOutputs>\n')
            node_name.transitions.append('\t\t\t<qual:output    qual:qualitativeSpecies="%s"\n'%("ope_"+operon_id))
            node_name.transitions.append('\t\t\t\t     qual:transitionEffect="assignmentLevel"/>\n')
            node_name.transitions.append('\t\t</qual:listOfOutputs>\n')
            node_name.transitions.append('\t\t<qual:listOfFunctionTerms>\n')
            node_name.transitions.append('\t\t\t<qual:functionTerm qual:resultLevel="1">\n')
            node_name.transitions.append('\t\t\t\t<math xmlns="http://www.w3.org/1998/Math/MathML">\n')
            node_name.transitions.append('\t\t\t\t\t<!-- input_1 >= 1 and input_2 >= 1 -->\n')
            node_name.transitions.append('\t\t\t\t\t<apply>\n')
            node_name.transitions.append('\t\t\t\t\t\t<and/>\n')
            node_name.transitions.append('\t\t\t\t\t\t<apply>\n')
            node_name.transitions.append('\t\t\t\t\t\t\t<geq/>\n')
            node_name.transitions.append('\t\t\t\t\t\t\t<ci>%s</ci>\n'%("spe_"+input_ids[0]))
            node_name.transitions.append('\t\t\t\t\t\t\t<ci>theta_%s</ci>\n'%("spe_"+input_ids[0]))
            node_name.transitions.append('\t\t\t\t\t\t</apply>\n')
            node_name.transitions.append('\t\t\t\t\t\t<apply>\n')
            node_name.transitions.append('\t\t\t\t\t\t\t<geq/>\n')
            node_name.transitions.append('\t\t\t\t\t\t\t<ci>%s</ci>\n'%("spe_"+input_ids[1]))
            node_name.transitions.append('\t\t\t\t\t\t\t<ci>theta_%s</ci>\n'%("spe_"+input_ids[1]))
            node_name.transitions.append('\t\t\t\t\t\t</apply>\n')
            node_name.transitions.append('\t\t\t\t\t</apply>\n')
            node_name.transitions.append('\t\t\t\t</math>\n')
            node_name.transitions.append('\t\t\t</qual:funtionTerm>\n')
            node_name.transitions.append('\t\t\t<qual:defaultTerm qual:resultLevel="0"/>\n')
            node_name.transitions.append('\t\t</qual:listOfFunctionTerms>\n')
            node_name.transitions.append('\t</qual:transition>\n') 
        elif trans_logic.lower() == 'or':
            input_id_bool = input_id_boolean_tuple[0]
            input_id = "spe_"+input_id_bool[0]
            boolean = input_id_bool[1]
            node_name.transitions.append('\t\t<qual:listOfInputs>\n')
            node_name.transitions.append('\t\t\t<qual:input qual:id="theta_%s"        qual:qualitativeSpecies="%s"\n'%(input_id,input_id))                
            node_name.transitions.append('\t\t\t\t    qual:thresholdLevel="1"   qual:transitionEffect="none"\n')
            if boolean.lower() == 'true':
                node_name.transitions.append('\t\t\t\t    qual:sign="negative"/>\n')
            elif boolean.lower() == 'false':
                node_name.transitions.append('\t\t\t\t    qual:sign="positive"/>\n')
            node_name.transitions.append('\t\t</qual:listOfInputs>\n')   
            node_name.transitions.append('\t\t<qual:listOfOutputs>\n')
            node_name.transitions.append('\t\t\t<qual:output    qual:qualitativeSpecies="%s"\n'%("ope_"+operon_id))
            node_name.transitions.append('\t\t\t\t     qual:transitionEffect="assignmentLevel"/>\n')
            node_name.transitions.append('\t\t</qual:listOfOutputs>\n')
            node_name.transitions.append('\t\t<qual:listOfFunctionTerms>\n')
            node_name.transitions.append('\t\t\t<qual:functionTerm qual:resultLevel="1">\n')
            node_name.transitions.append('\t\t\t\t<math xmlns="http://www.w3.org/1998/Math/MathML">\n')
            node_name.transitions.append('\t\t\t\t\t<!-- input >= 1-->\n')
            node_name.transitions.append('\t\t\t\t\t<apply>\n')
            node_name.transitions.append('\t\t\t\t\t\t<geq/>\n')
            node_name.transitions.append('\t\t\t\t\t\t<ci>%s</ci>\n'%input_id)
            node_name.transitions.append('\t\t\t\t\t\t<ci>theta_%s</ci>\n'%input_id)
            node_name.transitions.append('\t\t\t\t\t</apply>\n')
            node_name.transitions.append('\t\t\t\t</math>\n')
            node_name.transitions.append('\t\t\t</qual:funtionTerm>\n')
            node_name.transitions.append('\t\t\t<qual:defaultTerm qual:resultLevel="0"/>\n')
            node_name.transitions.append('\t\t</qual:listOfFunctionTerms>\n')
            node_name.transitions.append('\t</qual:transition>\n') 
        node_name.transitions.append('</qual:listOfTransitions>')
    
    def output_transition(self,node_name,trans_id,output_id,operon_id):
        '''
        @Parameters:
            node_name: name of node object, instantiated using the Node class 
            trans_id: transition id 
            output_id: single variable input which denotes the id of an operon's output
            operon_id: operon id 
            
        @Method:
            Translate all the inputed information to SBML and append to list
        '''
        node_name.transitions.append('<qual:listOfTransitions>\n')
        node_name.transitions.append('\t<qual:transtion qual:id="%s">\n'%("ot_"+trans_id))
        node_name.transitions.append('\t\t<qual:listOfInputs>\n')
        node_name.transitions.append('\t\t\t<qual:input    qual:id="theta_%s"        qual:qualitativeSpecies="%s"\n'%("ope_"+operon_id,"ope_"+operon_id))                
        node_name.transitions.append('\t\t\t\t    qual:thresholdLevel="1"   qual:transitionEffect="none"\n')
        node_name.transitions.append('\t\t\t\t    qual:sign="positive"/>\n')
        node_name.transitions.append('\t\t</qual:listOfInputs>\n')
        if len(output_id) > 1:
            node_name.transitions.append('\t\t<qual:listOfOutputs>\n')
            for spe_output in output_id:
                node_name.transitions.append('\t\t\t<qual:output    qual:qualitativeSpecies="%s"\n'%("spe_"+spe_output))
                node_name.transitions.append('\t\t\t\t     qual:transitionEffect="assignmentLevel"/>\n')
            node_name.transitions.append('\t\t</qual:listOfOutputs>\n')    
        else:
            node_name.transitions.append('\t\t<qual:listOfOutputs>\n')
            node_name.transitions.append('\t\t\t<qual:output    qual:qualitativeSpecies="%s"\n'%("spe_"+output_id[0]))
            node_name.transitions.append('\t\t\t\t     qual:transitionEffect="assignmentLevel"/>\n')
            node_name.transitions.append('\t\t</qual:listOfOutputs>\n')
        node_name.transitions.append('\t\t<qual:listOfFunctionTerms>\n')
        node_name.transitions.append('\t\t\t<qual:functionTerm qual:resultLevel="1">\n')
        node_name.transitions.append('\t\t\t\t<math xmlns="http://www.w3.org/1998/Math/MathML">\n')
        node_name.transitions.append('\t\t\t\t\t<!-- input >= 1-->\n')
        node_name.transitions.append('\t\t\t\t\t<apply>\n')
        node_name.transitions.append('\t\t\t\t\t\t<geq/>\n')
        node_name.transitions.append('\t\t\t\t\t\t<ci>%s</ci>\n'%("ope_"+operon_id))
        node_name.transitions.append('\t\t\t\t\t\t<ci>theta_%s</ci>\n'%("ope_"+operon_id))
        node_name.transitions.append('\t\t\t\t\t</apply>\n')
        node_name.transitions.append('\t\t\t\t</math>\n')
        node_name.transitions.append('\t\t\t</qual:funtionTerm>\n')
        node_name.transitions.append('\t\t\t<qual:defaultTerm qual:resultLevel="0"/>\n')
        node_name.transitions.append('\t\t</qual:listOfFunctionTerms>\n')
        node_name.transitions.append('\t</qual:transition>\n') 
        node_name.transitions.append('</qual:listOfTransitions>')    