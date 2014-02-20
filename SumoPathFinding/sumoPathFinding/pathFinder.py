from functools import reduce
from SumoPathFinding.sumoPathFinding.cityMap import CityMap, Vertex
from SumoPathFinding.sumoPathFinding.path import Path


def dijkstra_find_path(city_map, start, end):
    """
    Find path using dijkstra algorithm. Arguments:
     :param city_map
     :type city_map: CityMap

     :param start: first node
     :type start Vertex

     :param end: target node
     :type end: Vertex

     :returns: Path
     :rtype: Path
    """
    costs, prevs = shortest_path(city_map, start)
    vertexes = [end, ]
    while vertexes[0] in prevs:
        vertexes.insert(0, prevs[vertexes[0]])
    return Path(vertexes=vertexes, cost=costs[end])


def shortest_path(graph, sourceNode):
    """
    Return the shortest path distance between sourceNode and all other nodes
    using Dijkstra's algorithm.

    :param graph CityMap.
    :type graph CityMap

    :param sourceNode: Node from which to start the search.
    :type sourceNode: Vertex

    :rtype:  tuple
    :return: A tuple containing two dictionaries, each keyed by
        targetNodes.  The first dictionary provides the shortest distance
        from the sourceNode to the targetNode.  The second dictionary
        provides the previous node in the shortest path traversal.
        Inaccessible targetNodes do not appear in either dictionary.
    """
    # Initialization
    dist     = { sourceNode: 0 }
    previous = {}
    q = list(graph.vertexes)

    # Algorithm loop
    while q:
        # examine_min process performed using O(nodes) pass here.
        # May be improved using another examine_min data structure.
        u = reduce(lambda current, node: node if node in dist and dist[node] < dist.get(current, float('inf')) else current, q)
        q.remove(u)

        # Process reachable, remaining nodes from u
        for edge in u.edges:
            if edge.vertex2 in q:
                alt = dist[u] + edge.medium_cost
                if (edge.vertex2 not in dist) or (alt < dist[edge.vertex2]):
                    dist[edge.vertex2] = alt
                    previous[edge.vertex2] = u

    return (dist, previous)