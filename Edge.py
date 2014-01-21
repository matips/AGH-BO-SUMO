__author__ = 'Mateusz'
from Vertex import Vertex


class Edge:
    def __init__(self, vertex1: Vertex, vertex2: Vertex, medium_cost, maximu_cost, minimum_cost):
        self.vertex1 = vertex1
        self.vertex2 = vertex2
        self.medium_cost = medium_cost
        self.maximu_cost = maximu_cost
        self.minimum_cost = minimum_cost
