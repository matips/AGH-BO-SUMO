__author__ = 'Piotrek'

class CityMap:
    
    def __init__(self, vertices):
        self.vertices = vertices
        
    def __iter__(self):
        return self.vertices.itervalues()