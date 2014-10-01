class device_node:
    '''
    '''

    def __init__(self, name, state = False):
        '''
        '''
        self.name = name
        self.state = state
        
    def __str__(self):
        '''
        '''
        return 'Name:', self.name
    
class t_input_node:
    '''
    '''
    
    def __init__(self, _type, math, devices = [], intermediates = []):
        '''
        @ param _type
        @ param math, either a string or a list of boolean logic to follow. 
        @ param devices
        @ param intermediates
        '''
        self._type = _type
        self.math = math
        self.devices = devices
        self.intermediates = intermediates
    
    def _math(self):
        '''
        @ funct Returns true if the boolean math is fufilled for a given t_input_node.
        Repressors produce tokens when not present.
        Activators produce tokens when present. 
        Specific boolean math considered using the custom_math() funct
        '''
        tokens = 0
        for interm in self.intermediates:
            if interm._type == 'activator' and interm.state == True:
                tokens += 1
            elif interm._type == 'repressor' and interm.state == False:
                tokens += 1
        if isinstance(self.math, list):
            return self.custom_math()
        elif self.math == 'and' and tokens == len(self.intermediates):
            return True
        elif self.math == 'or' and tokens != 0:
            return True
        elif self.math == 'nor' and tokens == 0:
            return True
        elif self.math == 'xor' and tokens != len(self.intermediates) and tokens != 0:
            return True
        elif self.math == 'nand' and tokens != len(self.intermediates):
            return True
        elif self.math == 'xnor' and tokens == 0 or tokens == len(self.intermediates):
            return True
        else:
            return False
        
    def custom_math(self):
        '''
        '''
        # The underlying idea is that the intermediates math list can only contain the following:
        # not, or, or not, and, and not
        for interm, state, i in self.intermediates, self.math, enumerate(self.math):
            if i == 0 and state == 'not':
                command = 'not ' + str(interm.name) + '.state '
            elif i == 0 and state != 'not':
                command = 'if ' + str(interm.name) + '.state'
            elif i > 0 and i < len(self.math) - 2: 
                command = command + ' ' + interm.math + ' ' + interm.state  
            elif  state == 'not'
                command = command + ' ' + interm.math + 'not ' + interm.state            
            else:
                command = command + ' ' + interm.math + ' ' + interm.state
            return exec command
        
    def __str__(self):
        '''
        '''
        return 'Type:', self._type, 'Math:', self.math
    
        
class intermediates_node:
    '''
    '''
    
    def __init__(self,name, state):
        '''
        '''
        self.name = name
        self.state = name
        
    def __str__(self):
        '''
        '''
        return 
    
        