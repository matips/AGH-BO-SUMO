import Edge
import Vertex


class Path:
    def __init__(self, vertexes:[Vertex]):
        self.vertexes = vertexes
        self.cost = None #if cost was estimated

    def length(self):
        return len(self.vertexes)

    def remove_cycles(self, start=0):
        prev = {}
        for i in range(start, len(self.vertexes)):
            if self.vertexes[i] in prev:
                self.vertexes = self.vertexes[0: prev[self.vertexes[i]]] + self.vertexes[i + 1:]
                self.remove_cycles(i)
                return

    def __cmp__(self, other):
        if self.cost is None:
            self.estimate_cost()
        if other.cost is None:
            other.estimate_cost()
        return self.cost - other.cost

    def estimate_cost(self):
        self.cost = sum(map(
            lambda xy: min(map(self.estimate_edge,
                               filter(lambda edge: edge.vertex1 == xy[0] and edge.vertex2 == xy[1], xy[0].edges))),
            zip(self.vertexes, self.vertexes[1:])
        ))

    def estimate_edge(self, edge:Edge):
        return edge.maximu_cost


