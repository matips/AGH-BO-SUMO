from io import StringIO
import pickle
import random
from SumoPathFinding.sumoPathFinding.inputLoader import loadInput
from SumoPathFinding.sumoPathFinding.edgeTimeStats import EdgeTimeStats
from SumoPathFinding.sumoPathFinding.path import radom_statistic_metric
from SumoPathFinding.sumoPathFinding.pathFinder import dijkstra_find_path
from SumoPathFinding.sumoPathFinding.pathSimulator import PathSimulator
from SumoPathFinding.sumoPathFinding.population import Population

__author__ = 'Mateusz'

with open('../input/eichstaett.citymap', 'rUb', buffering=True) as f:
    city_map = pickle.load(f)
    start, end = random.sample(city_map.vertexes, 2)
    population = Population(city_map, start, end, comparator=radom_statistic_metric)
    dijkstra_result =  dijkstra_find_path(city_map, start, end)
    genetic_result = population.run_algorithm(200)
    path_simulator = PathSimulator('../input/eichstaett.sumocfg')
    dr =  path_simulator.measurePathTime(dijkstra_result, 0)
    print dr
    #print path_simulator.measurePathTime(genetic_result, 0)

