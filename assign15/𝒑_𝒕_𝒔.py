class Pyramid:
    # Properties
    radius = None
    def __init__(self, s1):
        self.radius = s1
    def __init__(self, s2):
        self.radius = s2
        
    def Perimeter(self):
        return (self.radius * self.radius) // 1.3
    
class Square(Pyramid):
        def __init__(self, a):
            self.radius = a
            
        def Area(self):
            return self.radius ** 2
        
        def Perimeter(self):
            return self.radius *4 
        
class Triangle(Square):
            def __init__(self, a):
                self.radius = a
                
            def __init__(self, b):
                self.radius = b
                
            def __init__(self, c):
                self.radius = c
                
            def __init__(self, h):
                self.radius = h
                
            def Area(self):
                return (self.h * self.b)//2
            
            def Perimeter(self):
                return self.a + self.b + self.c
            
pyramid =  Pyramid(5)
print(pyramid.Perimeter())
sphere = Square(5)
triangle = Triangle(5) 
