from SumoPathFinding.sumoPathFinding.cityMap import CityMap, Vertex

__author__ = 'Mateusz'

def init_city_map():
    cmap = CityMap(vertexes=[Vertex(sumo_id=sid) for sid in range(16)])

    cmap.vertexes[0].add_edge(cmap.vertexes[1], 4)
    cmap.vertexes[0].add_edge(cmap.vertexes[4], 1)
    cmap.vertexes[0].add_edge(cmap.vertexes[14], 4)

    cmap.vertexes[1].add_edge(cmap.vertexes[0], 6)
    cmap.vertexes[1].add_edge(cmap.vertexes[3], 10)
    cmap.vertexes[1].add_edge(cmap.vertexes[4], 1)
    cmap.vertexes[1].add_edge(cmap.vertexes[2], 7)
    cmap.vertexes[1].add_edge(cmap.vertexes[11], 1)

    cmap.vertexes[2].add_edge(cmap.vertexes[1], 5)
    cmap.vertexes[2].add_edge(cmap.vertexes[11], 1)

    cmap.vertexes[3].add_edge(cmap.vertexes[1], 4)

    cmap.vertexes[4].add_edge(cmap.vertexes[3], 12)
    cmap.vertexes[4].add_edge(cmap.vertexes[1], 4)
    cmap.vertexes[4].add_edge(cmap.vertexes[5], 5)

    cmap.vertexes[5].add_edge(cmap.vertexes[4], 9)
    cmap.vertexes[5].add_edge(cmap.vertexes[2], 4)
    cmap.vertexes[5].add_edge(cmap.vertexes[6], 6)
    cmap.vertexes[5].add_edge(cmap.vertexes[7], 11)
    cmap.vertexes[5].add_edge(cmap.vertexes[8], 4)

    cmap.vertexes[6].add_edge(cmap.vertexes[2], 12)
    cmap.vertexes[6].add_edge(cmap.vertexes[5], 8)
    cmap.vertexes[6].add_edge(cmap.vertexes[7], 6)
    cmap.vertexes[6].add_edge(cmap.vertexes[7], 9)
    cmap.vertexes[6].add_edge(cmap.vertexes[9], 6)
    cmap.vertexes[6].add_edge(cmap.vertexes[3], 1)

    cmap.vertexes[7].add_edge(cmap.vertexes[10], 0)
    cmap.vertexes[7].add_edge(cmap.vertexes[9], 0)
    cmap.vertexes[7].add_edge(cmap.vertexes[6], 2)
    cmap.vertexes[7].add_edge(cmap.vertexes[6], 1)

    cmap.vertexes[8].add_edge(cmap.vertexes[5], 5)
    cmap.vertexes[8].add_edge(cmap.vertexes[7], 5)
    cmap.vertexes[8].add_edge(cmap.vertexes[10], 8)

    cmap.vertexes[9].add_edge(cmap.vertexes[6], 4)
    cmap.vertexes[9].add_edge(cmap.vertexes[7], 6)
    cmap.vertexes[9].add_edge(cmap.vertexes[10], 1)
    cmap.vertexes[9].add_edge(cmap.vertexes[13], 3)

    cmap.vertexes[10].add_edge(cmap.vertexes[7], 0)
    cmap.vertexes[10].add_edge(cmap.vertexes[8], 3)

    cmap.vertexes[11].add_edge(cmap.vertexes[14], 7)
    cmap.vertexes[11].add_edge(cmap.vertexes[1], 4)
    cmap.vertexes[11].add_edge(cmap.vertexes[2], 3)
    cmap.vertexes[11].add_edge(cmap.vertexes[12], 5)

    cmap.vertexes[12].add_edge(cmap.vertexes[14], 2)
    cmap.vertexes[12].add_edge(cmap.vertexes[11], 1)
    cmap.vertexes[12].add_edge(cmap.vertexes[2], 8)
    cmap.vertexes[12].add_edge(cmap.vertexes[6], 3)
    cmap.vertexes[12].add_edge(cmap.vertexes[13], 5)
    cmap.vertexes[12].add_edge(cmap.vertexes[15], 2)

    cmap.vertexes[13].add_edge(cmap.vertexes[12], 19)
    cmap.vertexes[13].add_edge(cmap.vertexes[9], 3)

    cmap.vertexes[14].add_edge(cmap.vertexes[0], 2)
    cmap.vertexes[14].add_edge(cmap.vertexes[11], 2)
    cmap.vertexes[14].add_edge(cmap.vertexes[12], 3)

    cmap.vertexes[15].add_edge(cmap.vertexes[13], 2)
    return cmap
