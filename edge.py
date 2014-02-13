__author__ = 'Mateusz'

class Edge:
    def __init__(self, sumo_id, vertex1, vertex2, medium_cost=None, maximum_cost=None, minimum_cost=None):
        self.sumo_id = sumo_id
        self.vertex1 = vertex1
        self.vertex2 = vertex2
        self.medium_cost = medium_cost
        self.maximum_cost = maximum_cost
        self.minimum_cost = minimum_cost
