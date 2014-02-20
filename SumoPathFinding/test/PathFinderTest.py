from datetime import time
from SumoPathFinding.sumoPathFinding.pathFinder import dijkstra_find_path
from SumoPathFinding.sumoPathFinding.population import Population
from SumoPathFinding.test.init_city_map import init_city_map

__author__ = 'Mateusz'



city_map = init_city_map()

print ("Dijkstra path:")
print (dijkstra_find_path(city_map, city_map.vertexes[0], city_map.vertexes[10]))

print ("Population paths:")
population = Population(city_map = city_map, start = city_map.vertexes[0], end = city_map.vertexes[10], population_size=2)
for path in population.population:
    print (path)

print ("Crossing 0 with 1:")
print (population.crossing())
print ("Mutate")
print (population.mutate())
print ("Algorithm")
population = Population(city_map = city_map, start = city_map.vertexes[0], end = city_map.vertexes[10], population_size=4)
print (population.run_algorithm(10))
