__author__ = 'Piotrek'

class Vertex:
    def __init__(self, sumo_id = None, edges=None):
        self.edges = edges or []
        self.sumo_id = sumo_id

    def neighbours(self):
        return list( map(lambda e: e.vertex2, self.edges))

    def add_edge(self, vertex2, medium_cost=None, maximum_cost = None, minimum_cost = None, sumo_id = None):
        """
        add edge from self vertex to vertex2. Returns self for support chain.
        """
        self.edges.append(Edge(vertex1=self, vertex2=vertex2, medium_cost=medium_cost, minimum_cost=minimum_cost, maximum_cost=maximum_cost, sumo_id=sumo_id))

    def __repr__(self):
        return str(self.sumo_id)


class Edge:
    class VertexIsNotInEdge(Exception):
        pass

    def __init__(self, sumo_id, vertex1, vertex2, medium_cost=None, maximum_cost=None, minimum_cost=None):
        self.sumo_id = sumo_id
        self.vertex1 = vertex1
        self.vertex2 = vertex2
        self.medium_cost = medium_cost
        self.maximum_cost = maximum_cost
        self.minimum_cost = minimum_cost

class CityMap:
    def __init__(self, vertexes = None):
        self.vertexes = vertexes or []
        
    def __iter__(self):
        return self.vertexes.__iter__()