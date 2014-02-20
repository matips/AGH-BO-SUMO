from SumoPathFinding.sumoPathFinding.pathFinder import dijkstra_find_path
from SumoPathFinding.sumoPathFinding.population import Population
from time import time
from SumoPathFinding.test.init_city_map import init_city_map

__author__ = 'Mateusz'


class Timer:
    """
    Nie wiem, czy to cos ulatwia, ale pozwala na badanie szybkosci wykonywania roznych czesci skryptu. Miezy do wywolania stop dana czynnosc. Zaczyna od inicjalizacji, poprzedniego stop lub restartu
    """
    def __init__(self):
        self.activities = {}
        self.start_current = time()

    def stop(self, name):
        current = time() - self.start_current
        if name in self.activities:
            self.activities[name].append(current)
        else:
            self.activities[name] = [current, ]
        self.start_current = time()


    def reset(self):
        self.start_current = time()

    def print_result(self):
        for name, values in self.activities.items():
            print ("{0} \t\t -- avg: {1} \t\t sum: {2}".format(name.ljust(20), str(sum(values) / len(values)).ljust(15),
                                                               sum(values)) )

    def get_avg(self, name):
        values = self.activities[name]
        return str(sum(values) / len(values))


if __name__ == "__main__":
    city_map = init_city_map()

    for _ in range(1000):
        timer = Timer()
        dijkstra_find_path(city_map, city_map.vertexes[0], city_map.vertexes[10])
        timer.stop("Dijkstra")

    for _ in range(1000):
        timer.reset()
        population = Population(city_map = city_map, start = city_map.vertexes[0], end = city_map.vertexes[10], population_size=4)
        population.run_algorithm(3)
        timer.stop("Genetic algorithm")


    timer.print_result()