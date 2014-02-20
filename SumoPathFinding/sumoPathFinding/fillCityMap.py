__author__ = 'Piotrek'

import os
import sys
import subprocess
import pickle
from SumoPathFinding.sumoPathFinding.inputLoader import loadInput
from SumoPathFinding.sumoPathFinding.edgeTimeStats import EdgeTimeStats
from collections import namedtuple

# Assertions for "traci" module import:

if sys.version_info.major != 2:
    sys.exit("SUMO TraCI requires Python version 2.x")

if 'SUMO_HOME' in os.environ:
    sys.path.append(os.path.join(os.environ['SUMO_HOME'], 'tools'))
else:
    sys.exit("Please declare environment variable 'SUMO_HOME'")

import traci

def updateVehiclePositions(vehicles, edgeTimes, vehicleEdges, step):
    for vehicle in vehicles:
        previousEdgeId = vehicleEdges[vehicle].onEdge   # which edge was the vehicle on in previous simulation step
        try:
            edgeId = traci.vehicle.getRoadID(vehicle)   # which edge is the vehicle currently on
        except traci.TraCIException:    # (if vehicle has already left the simulation)
            edgeId = None
            vehicles.remove(vehicle)

        if previousEdgeId != edgeId:    # if vehicle has moved to an other edge
            try:
                edgeTimes[previousEdgeId].update(step - vehicleEdges[vehicle].sinceStep)    # measure time spent by the vehicle on the previous edge and update edge stats
            except KeyError:    # (if vehicle was teleporting, on an internal edge or has just entered the simulation)
                pass
            vehicleEdges[vehicle] = VehicleEdgeInfo(edgeId, step)   # update edge information


if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.exit("Too few arguments.\nUsage: " + sys.argv[0] + " SUMOCFG_FILE OUTPUT_CITY_MAP_FILE [STEP_LENGTH]")

    # load city map and vehicle IDs
    cityMap, vehicles = loadInput(sys.argv[1])
    print("Network file loaded.")

    PORT = 8888
    DEFAULT_STEP_LENGTH = 1.0
    STDOUT_FILE = None
    STDERR_FILE = open(os.devnull, "w") # open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../log/sumo_stderr.log'), 'w')

    # start SUMO server
    sumoServer = subprocess.Popen(
        [os.path.join(os.environ['SUMO_HOME'], 'bin', 'sumo'), '--remote-port', str(PORT), '--step-length',
         sys.argv[3] if len(sys.argv) > 3 else str(DEFAULT_STEP_LENGTH), '-c', sys.argv[1]],
        cwd=os.getcwd(), stdout=STDOUT_FILE, stderr=STDERR_FILE)

    # connect to server
    traci.init(PORT)
    print("Connected.")

    # dictionary: edge ID -> travel times (min, max, mean) for the edge
    edgeTimes = {}
    for edge in cityMap.edgeIter():
        edgeTimes[edge.sumo_id] = EdgeTimeStats(traci.edge.getTraveltime(edge.sumo_id))

    VehicleEdgeInfo = namedtuple('VehicleEdgeInfo', ['onEdge', 'sinceStep']) # create a new type (which edge and since which simulation step has the vehicle been on?)
    # dictionary: vehicle ID -> edge ID and simulation step since which the vehicle has been on the edge
    vehicleEdges = {}
    for vehicle in vehicles:
        vehicleEdges[vehicle] = VehicleEdgeInfo(None, None)

    step = 0
    stepLength = float(sys.argv[3]) if len(sys.argv) > 3 else DEFAULT_STEP_LENGTH
    while traci.simulation.getMinExpectedNumber() > 0:  # while there are vehicles in the simulation
        traci.simulationStep()
        updateVehiclePositions(vehicles, edgeTimes, vehicleEdges, step)
        step += stepLength

    traci.close()
    sumoServer.wait()

    # update city map
    for edge in cityMap.edgeIter():
        edge.minimum_cost = edgeTimes[edge.sumo_id].getMinTime()
        edge.maximum_cost = edgeTimes[edge.sumo_id].getMaxTime()
        edge.medium_cost = edgeTimes[edge.sumo_id].getMeanTime()

    # save city map to a file
    print("Saving the city map...")
    sys.setrecursionlimit(10000)    # the map is recursive; Python 2.x's pickle uses DFS
    pickle.dump(cityMap, open(sys.argv[2], 'wb'))
    print("Done.")

    # # output - for test purposes
    # print "edge ID, min time, max time, mean time:"
    # for edge in cityMap.edgeIter():
    #   print(edge.sumo_id + ", " + str(edgeTimes[edge.sumo_id]))
