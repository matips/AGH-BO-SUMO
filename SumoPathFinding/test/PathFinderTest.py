from SumoPathFinding.sumoPathFinding.cityMap import CityMap, Vertex
from SumoPathFinding.sumoPathFinding.pathFinder import find_path

__author__ = 'Mateusz'

def init_city_map():
    cmap = CityMap(vertices=[Vertex(sumo_id=sid) for sid in range(11)])

    cmap.vertices[0].add_edge(cmap.vertices[1], 4)
    cmap.vertices[0].add_edge(cmap.vertices[4], 1)

    cmap.vertices[1].add_edge(cmap.vertices[0], 6)
    cmap.vertices[1].add_edge(cmap.vertices[3], 10)
    cmap.vertices[1].add_edge(cmap.vertices[4], 1)
    cmap.vertices[1].add_edge(cmap.vertices[2], 7)

    cmap.vertices[2].add_edge(cmap.vertices[1], 5)

    cmap.vertices[3].add_edge(cmap.vertices[1], 4)

    cmap.vertices[4].add_edge(cmap.vertices[3], 12)
    cmap.vertices[4].add_edge(cmap.vertices[1], 4)
    cmap.vertices[4].add_edge(cmap.vertices[5], 5)

    cmap.vertices[5].add_edge(cmap.vertices[4], 9)
    cmap.vertices[5].add_edge(cmap.vertices[2], 4)
    cmap.vertices[5].add_edge(cmap.vertices[6], 6)
    cmap.vertices[5].add_edge(cmap.vertices[7], 11)
    cmap.vertices[5].add_edge(cmap.vertices[8], 4)

    cmap.vertices[6].add_edge(cmap.vertices[2], 12)
    cmap.vertices[6].add_edge(cmap.vertices[5], 8)
    cmap.vertices[6].add_edge(cmap.vertices[7], 6)
    cmap.vertices[6].add_edge(cmap.vertices[7], 9)
    cmap.vertices[6].add_edge(cmap.vertices[9], 6)

    cmap.vertices[7].add_edge(cmap.vertices[10], 0)
    cmap.vertices[7].add_edge(cmap.vertices[9], 0)
    cmap.vertices[7].add_edge(cmap.vertices[6], 2)
    cmap.vertices[7].add_edge(cmap.vertices[6], 1)

    cmap.vertices[8].add_edge(cmap.vertices[5], 5)
    cmap.vertices[8].add_edge(cmap.vertices[7], 5)
    cmap.vertices[8].add_edge(cmap.vertices[10], 8)

    cmap.vertices[9].add_edge(cmap.vertices[6], 4)
    cmap.vertices[9].add_edge(cmap.vertices[7], 6)
    cmap.vertices[10].add_edge(cmap.vertices[7], 0)
    cmap.vertices[10].add_edge(cmap.vertices[8], 3)
    return cmap


city_map = init_city_map()

print (find_path(city_map, city_map.vertices[0], city_map.vertices[10]))
