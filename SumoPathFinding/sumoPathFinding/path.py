from SumoPathFinding.sumoPathFinding.cityMap import Vertex, Edge


class Path:
    def __init__(self, vertexes:[Vertex], cost=None):
        self.vertexes = vertexes
        self.cost = cost #if cost was estimated
        if vertexes is not None:
            self.remove_cycles()

    def __len__(self):
        return self.length()

    def __getitem__(self, item):
        return self.vertexes[item]

    def __repr__(self):
        return "<{0}> -> {1}".format(self.vertexes, self.cost or self.estimate_cost(basic_metric))

    def length(self):
        return len(self.vertexes)

    def remove_cycles(self):
        prev = {}
        for i, vertex in enumerate(self.vertexes):
            if vertex in prev:
                self.vertexes = self.vertexes[: prev[vertex]] + self.vertexes[i:]
                self.remove_cycles()
                return
            prev[vertex] = i

    def estimate_cost(self, metric):
        self.cost = sum(map(
            lambda xy: min(map(metric, list(filter(lambda edge: edge.vertex2 is xy[1], xy[0].edges)))),
            zip(self.vertexes, self.vertexes[1:])
        ))
        return self.cost



def basic_metric(edge: Edge):
    return edge.medium_cost