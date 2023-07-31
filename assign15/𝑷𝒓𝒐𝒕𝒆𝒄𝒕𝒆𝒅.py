class Cup:
    def __init__(self):
        self.color = None #proteced variable
        self._content = None
        
    def fill(self,beverage):
        self._content = beverage
        
    def empty(self):
        self._content = None 
