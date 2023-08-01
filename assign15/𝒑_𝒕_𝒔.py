class Pyramid:
    # Properties
    radius = None
    def __init__(self, s):
        self.radius = s
    
    def set_radius(self, s):
        self.radius = s
        
    def __init__(self, h):
        self.radius = h
        
    def set_radius(self, h):
        self.radius = h
        
    def Perimeter(self):
        return (self.radius * self.radius) // 1.3
    
class Square(Pyramid):
        def __init__(self, a):
            self.radius = a
            
        def set_radius(self, a):
            self.radius = a
            
        def Area(self):
            return self.radius * self.radius
        
        def Perimeter(self):
            return self.radius *4 
        
class triangle(Square):
            def __init__(self, a):
                self.radius = a
                
            def __init__(self, b):
                self.radius = b
                
            def __init__(self, c):
                self.radius = c
                
            def __init__(self, h):
                self.radius = h
                
            def Area(self):
                return (self.radius * self.radius)//2
            
            def Perimeter(self):
                return self.radius + self.radius + self.radius
    
