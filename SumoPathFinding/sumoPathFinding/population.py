import random
from SumoPathFinding.sumoPathFinding.cityMap import CityMap, Vertex
from SumoPathFinding.sumoPathFinding.path import Path, basic_metric


class Population:
    def __init__(self, city_map, start, end, population_size=10, path_exchange_probability=0.5,
                 mutation_probability=0.1, comparator=basic_metric):
        """
        Create population base on city_map, start and target vertexes and options like population size and probablity of muatioon
        :param city_map
        :type city_map CityMap

        :param start
        :type start Vertex

        :param end: target node
        :type end Vertex

        :param population_size maximum population size. In Population initialization population_size ranodm path will be generated. After mutation or crossing operation new paths will be compare and reduce to population_size best paths
        :type population_size int

        :param path_exchange_probability probability of exchange sub-paths during corssing operation it. Should be flat from 0 to 1
        :type path_exchange_probability int

        :param mutation_probability probality of muation. Float form 0 to 1. During execution of algorithm mutation will be chose with this probality, otherwise crossing
        :type mutation_probability float

        """
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
            self.add_paths([self.mutate(), ] if random.random() < self.mutation_probability else list(self.crossing()))

        return self.population[0]

    def add_paths(self, paths):
        self.population = sorted(self.population + paths, key=lambda path: path.estimate_cost(self.metric))[
                          :self.population_size]

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
        child1 = list(path1.vertexes)
        child2 = list(path2.vertexes)
        i = 1
        while i < len(child1) - 1:
            if child1[i] in child2:
                index = child2.index(child1[i])
                child1, child2 = (child1[:i] + child2[index:], child2[:index] + child1[i:])
            i += 1

        return Path(child1), Path(child2)




