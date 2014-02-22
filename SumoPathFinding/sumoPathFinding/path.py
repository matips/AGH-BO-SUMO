import random
from SumoPathFinding.sumoPathFinding.cityMap import Vertex, Edge


class Path:
    def __init__(self, vertexes, cost=None):
        """
        :param vertexes: list of Vertexes
        :type vertexes list

        :cost
        :type cost int or float
        """
        self.vertexes = vertexes
        self.cost = cost #if cost was estimated
        if vertexes is not None:
            self.remove_cycles()

    def __len__(self):
        return self.length()

    def __getitem__(self, item):
        return self.vertexes[item]

    def __repr__(self):
        return "<{0}> -> {1}".format(self.vertexes, self.estimate_cost(average_metric))

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
        return sum(map(
            lambda xy: min(map(metric, list(filter(lambda edge: edge.vertex2 is xy[1], xy[0].edges)))),
            zip(self.vertexes, self.vertexes[1:])
        ))

    # "convert" vertex path to edge path (a list of edge IDs)
    def get_edge_ids(self):
        return [filter(lambda edge: edge.vertex2 == self.vertexes[i+1], self.vertexes[i].edges)[0].sumo_id for i in range(len(self.vertexes)-1)]


def average_metric(edge):
    return edge.medium_cost

def radom_statistic_metric(edge):
    """
    :param edge: edge to count cost
    :type edge Edge
    """
    return random.sample(edge.cost_samples, 1)[0] if len(edge.cost_samples) > 0 else edge.medium_cost

def min_max_triangular_metric(edge):
    if edge.minimum_cost == edge.maximum_cost:
        return edge.maximum_cost
    return random.triangular(edge.minimum_cost, edge.maximum_cost, (edge.minimum_cost+edge.maximum_cost) / 2.0)
