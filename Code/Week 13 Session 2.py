class car(object):
    def __init__(self, model = "", gas = 0, gas_cap = 0, mpg = 0, pos = 0):
        self.model = model
        self.gas = gas
        self.gas_cap = gas_cap
        self.mpg = mpg
        self.pos = 0
        
    def __repr__(self):
        return "The {} is at position {} with {} gas left".format(self.model, self.pos, self.gas)
    
    def __str__(self):
        return "The {} is at position {} with {} gas left".format(self.model, self.pos, self.gas)
    
    def fill_up(self):
        self.gas = self.gas_cap
        
    def go_for_x_gal(self, gal = 0):
        if gal <= self.gas:
            self.gas -=gal
            self.pos = self.mpg * gal
        else:
            for g in range(0,gal):
                if self.gas <= 0:
                    break
                self.gas -= 1
                self.pos += self.mpg
            
    def go_until_empty(self):
        self.pos = self.mpg * self.gas
        self.gas = 0
             
        
        
        
        
    
