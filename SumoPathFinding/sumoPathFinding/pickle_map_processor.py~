import pickle
import random
from SumoPathFinding.sumoPathFinding.path import  min_max_triangular_metric
from SumoPathFinding.sumoPathFinding.pathFinder import dijkstra_find_path
from SumoPathFinding.sumoPathFinding.pathSimulator import PathSimulator
from SumoPathFinding.sumoPathFinding.population import Population
from SumoPathFinding.test.GenericDjicstraCompare import Timer

__author__ = 'Mateusz'

with open('../input/eichstaett.citymap', 'rUb', buffering=True) as f:
    city_map = pickle.load(f)

start, end = random.sample(city_map.vertexes, 2)
timer = Timer()
population = Population(city_map, start, end, comparator=min_max_triangular_metric)
timer.stop("Genetic initialization")
dijkstra_result =  dijkstra_find_path(city_map, start, end)
timer.stop("Dijkstra")
genetic_result = population.run_algorithm(200)
timer.stop("Genetic")
path_simulator = PathSimulator('../input/eichstaett.sumocfg')
print "Dijkstra: \n\tpath: {0}\n\tresult: {1} s\n\tpath countin time: {2} s".format(dijkstra_result, path_simulator.measurePathTime(dijkstra_result, 0), timer.get_avg("Dijkstra"))
print "Genetic: \n\tpath: {0}\n\tresult: {1} s\n\tinitialization: {2} s\n\tpath counting time: {3} s".format(genetic_result, path_simulator.measurePathTime(genetic_result, 0), timer.get_avg("Genetic initialization"), timer.get_avg("Genetic"))

