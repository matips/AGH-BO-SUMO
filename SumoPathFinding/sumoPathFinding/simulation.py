__author__ = 'Piotrek'

import os
import sys
import subprocess
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
        try:
            edgeId = traci.vehicle.getRoadID(vehicle)
        except traci.TraCIException:
            edgeId = None
        previousEdgeId = vehicleEdges[vehicle].onEdge
        if previousEdgeId != edgeId:
            try:
                edgeTimes[previousEdgeId].update(step - vehicleEdges[vehicle].sinceStep)
            except KeyError:
                pass
            vehicleEdges[vehicle] = VehicleEdgeInfo(edgeId, step)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("Too few arguments.\nUsage: " + sys.argv[0] + " SUMO_NETWORK_FILE [STEP_LENGTH]")

    cityMap, vehicles = loadInput(sys.argv[1])
    print("Network file loaded.")

    PORT = 8888
    SEED = 123456
    DEFAULT_STEP_LENGTH = 1.0

    sumoServer = subprocess.Popen(
        [os.path.join(os.environ['SUMO_HOME'], 'bin', 'sumo'), '--remote-port', PORT.__str__(), '--step-length',
         sys.argv[2] if len(sys.argv) > 2 else DEFAULT_STEP_LENGTH, '--seed', SEED.__str__(), '-c', sys.argv[1]], cwd=os.getcwd())
    traci.init(PORT)
    print("Connected.")

    edgeTimes = {}
    for edge in cityMap.edgeIter():
        edgeTimes[edge.sumo_id] = EdgeTimeStats(traci.edge.getTraveltime(edge.sumo_id))

    VehicleEdgeInfo = namedtuple('VehicleEdgeInfo', ['onEdge', 'sinceStep'])
    vehicleEdges = {}
    for vehicle in vehicles:
        vehicleEdges[vehicle] = VehicleEdgeInfo(None, None)

    step = 0
    stepLength = float(sys.argv[2])
    while traci.simulation.getMinExpectedNumber() > 0:
        traci.simulationStep()
        updateVehiclePositions(vehicles, edgeTimes, vehicleEdges, step)
        step += stepLength

    traci.close()
    sumoServer.wait()

    print "edge ID, min time, max time, mean time:"
    for edge in cityMap.edgeIter():
        print(edge.sumo_id + ", " + str(edgeTimes[edge.sumo_id]))
