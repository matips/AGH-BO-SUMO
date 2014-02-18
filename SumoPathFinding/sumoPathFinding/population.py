import random
from SumoPathFinding.sumoPathFinding.cityMap import CityMap, Vertex
from SumoPathFinding.sumoPathFinding.path import Path, basic_metric


class Population:
    def __init__(self, city_map:CityMap, start:Vertex, end:Vertex, population_size=10, path_exchange_probability = 0.5, mutation_probability = 0.1, comparator = basic_metric):
        self.city_map = city_map
        self.start = start
        self.end = end
        if population_size < 2:
            raise Exception("Population size have to be >= 2 ")

        self.population_size = population_size
        self.population = [self.random_path(self.start, self.end) for _ in range(population_size)]

        self.path_exchange_probability = path_exchange_probability
        self.mutation_probability = mutation_probability
        self.metric = comparator

    def run_algorithm(self, steps):
        for _ in range(steps):
            self.add_paths([self.mutate(),] if random.random() < self.mutation_probability else list(self.crossing()))

        return self.population[0]

    def add_paths(self, paths):
        self.population = sorted(self.population + paths, key=lambda path: path.estimate_cost   (self.metric))[:self.population_size]

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


    def mutate(self):
        path, = random.sample(self.population, 1)
        div1, div2 = sorted(random.sample(range(len(path)), 2))
        return Path(path[:div1] + self.random_path(path[div1], path[div2]).vertexes + path[div2:])

    def crossing(self):
        path1, path2 = random.sample(self.population, 2)
        child1 = path1.vertexes.copy()
        child2 = path2.vertexes.copy()
        i = 1
        while i < len(child1) - 1:
            if child1[i] in child2:
                index = child2.index(child1[i])
                child1, child2 = (child1[:i] + child2[index:], child2[:index] + child1[i:])
            i += 1

        return Path(child1), Path(child2)

    def add_element(self, new_element):
        self.elements = (self.elements + new_element).sort()[:self.population_size]



