from SumoPathFinding.sumoPathFinding.cityMap import Vertex, Edge


class Path:
    def __init__(self, vertexes:[Vertex], cost = None):
        self.vertexes = vertexes
        self.cost = cost #if cost was estimated

    def __repr__(self):
        return "<{0}> -> {1}".format(self.vertexes, self.cost or self.estimate_cost(basic_metric))

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

    def estimate_cost(self, metric):
        return sum(map(
            lambda xy: min(map(metric,
                               list(filter(lambda edge: edge.vertex2 is xy[1], xy[0].edges)))),
            zip(self.vertexes, self.vertexes[1:])
        ))


    def estimate_edge(self, edge):
        return edge.medium_cost


def basic_metric(edge: Edge):
    return edge.medium_cost
