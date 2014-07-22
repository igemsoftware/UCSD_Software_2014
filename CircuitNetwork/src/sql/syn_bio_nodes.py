class device_node:
    '''
    '''

    def __init__(self, name, state = False):
        self.name = name
        self.state = state
        
    def __str__(self):
        return 'Name:', name
    
class t_input_node:
    '''
    '''
    
    def __init__(self, type, math, devices = [], intermediates = []):
        self.type = type
        self.math = math
        self.devices = devices
        self.intermediates = intermediates
        
    # The math is really limited right now. It is assume that all of the intermediates are activators. 
    # After I am creating the activating intermediates I will start to include boolean math for those cases. 
    def _math(self):
        try:
            if self.math == 'and':
                self._and()
            elif self.math == 'nor':
                self._nor()
            elif self.math == 'or':
                self._or()
            elif self.math == 'nand':
                self._nand()
            elif self.math == 'xor':
                self._xor()
            elif self.xnor() == 'xnor'
                self._xnor()
        except:
            self._custom()
        
    def _and(self):
        for interm in self.intermediates:
            if interm.state is not True:
                return False
        return True

    def _nor(self):
        for interm in self.intermediates:
            
        
    
    def _or(self):
        for interm in self.intermediates:
            if interm.state is True:
                return True
        return False
    
    def _nand(self):
        for interm in self.intermediates:
            if interm.state is True:
                return False
        return True
    
    def _xor(self):
        count_act = 0
        count_deact = 0
        for interm in self.intermediates:
            if interm.state == True:
                count_act += 1
        if count_act < len(self.intermediates):
            return False
        else:
            return True
        
    def _xnor(self):
        count_act = 0
        for interm in self.intermediates:
            if interm.state == True:
                count_act += 1
        if count_act == len(self.intermediates) or count_act == 0:
            return True
        else:
            return False
    
    def _encapsulating_math(self):
        for interm in self.intermediates:
            if interm.type == 'activator' and interm.state == 'True':
                count_act += 1
            elif interm.type == 'repressor' and interm.state == 'False'
                count_act += 1
        if self.math == 'and' and count_act == len(self.intermediates)
        
        
    def __str__(self):
        return 'Type:', self.type, 'Math:', self.math
    
        
class intermediates_node:
    '''
    '''
    
    def __init__(self,name, state):
        self.name = name
        self.state = name
        
    def __str__(self):
        return 
    
        