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
file = open('eichstaett_output.txt','w')
file.write("Dijkstra             Genetic\n")
file.write("result time          result time\n")
	
for _ in range(7):
	start, end = random.sample(city_map.vertexes, 2)
	timer = Timer()
	for _ in range(7):
		population = Population(city_map, start, end, path_exchange_probability=0.1*random.randint(3,7),  mutation_probability=0.01*random.randint(1,20), comparator=min_max_triangular_metric)
		timer.stop("Genetic initialization")
		dijkstra_result =  dijkstra_find_path(city_map, start, end)
		timer.stop("Dijkstra")
		genetic_result = population.run_algorithm(200)
		timer.stop("Genetic")
		path_simulator = PathSimulator('../input/eichstaett.sumocfg')
		mpt1 = path_simulator.measurePathTime(dijkstra_result, 0)
		mpt2 = path_simulator.measurePathTime(genetic_result, 0)
		file.write("{0} {1} {2} {3}\n".format(mpt1, timer.get_avg("Dijkstra"), mpt2, timer.get_avg("Genetic")))
file.close()

with open('../input/rand20.citymap', 'rUb', buffering=True) as f:
    city_map = pickle.load(f)
file = open('rand20_output.txt','w')
file.write("Dijkstra             Genetic\n")
file.write("result time          result time\n")
	
for _ in range(7):
	start, end = random.sample(city_map.vertexes, 2)
	timer = Timer()
	for _ in range(7):
		population = Population(city_map, start, end, path_exchange_probability=0.1*random.randint(3,7),  mutation_probability=0.01*random.randint(1,20), comparator=min_max_triangular_metric)
		timer.stop("Genetic initialization")
		dijkstra_result =  dijkstra_find_path(city_map, start, end)
		timer.stop("Dijkstra")
		genetic_result = population.run_algorithm(200)
		timer.stop("Genetic")
		path_simulator = PathSimulator('../input/rand20.sumocfg')
		mpt1 = path_simulator.measurePathTime(dijkstra_result, 0)
		mpt2 = path_simulator.measurePathTime(genetic_result, 0)
		file.write("{0} {1} {2} {3}\n".format(mpt1, timer.get_avg("Dijkstra"), mpt2, timer.get_avg("Genetic")))
file.close()
