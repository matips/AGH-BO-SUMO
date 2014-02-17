import random
from SumoPathFinding.sumoPathFinding.cityMap import CityMap, Vertex
from SumoPathFinding.sumoPathFinding.path import Path


class Population:
    def __init__(self, city_map:CityMap, start:Vertex, end:Vertex, population_size=10):
        self.city_map = city_map
        self.start = start
        self.end = end
        self.population_size = population_size
        self.population = [self.random_path(self.start, self.end) for _ in range(population_size)]

        self.max_child = 0

    def random_path(self, start, end):
        remain = set(self.city_map.vertexes)
        path = [start, ]
        while path[-1] is not end:
            path__neighbours = path[-1].neighbours()
            available = remain.intersection(set(path__neighbours))
            if len(available) == 0:
                remain = set(self.city_map)
                path = [start, ]
            else:
                path.append(random.sample(available, 1)[0])
                remain.remove(path[-1])
        return Path(path)

    def crossing(self, element1, element2):
        sub_path_1 = element1[:self.divide_point(len(element1))]
        sub_path_2 = element2[len(element2) - self.divide_point(len(element2)):]
        child_path = Path(sub_path_1 + self.path_finder(sub_path_1[-1], sub_path_2[0]) + sub_path_2)
        child_path.remove_cycles()
        self.add_element(child_path)

    def divide_point(self, right):
        "determine divide point of mutate routes"
        r = random.uniform(1 / (right + 1), 1)
        return int(1 / r - 1)

    def mutate(self, right):
        pass

    def add_element(self, new_element):
        self.elements = (self.elements + new_element).sort()[:self.max_child]



