__author__ = 'Piotrek'

import os, sys
if 'SUMO_HOME' in os.environ:
    tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
    sys.path.append(tools)
else:
    sys.exit("please declare environment variable 'SUMO_HOME'")

if len(sys.argv) < 2:
    sys.exit("Too few arguments.\nUsage: " + sys.argv[0] + " SUMO_NETWORK_FILE")

from SumoPathFinding.sumoPathFinding.inputLoader import loadInput
cityMap, vehicles = loadInput(sys.argv[1])
print("Network file loaded.")

class EdgeTimeStats:
    def __init__(self, estimatedTime):
        self.minTime, self.maxTime = estimatedTime
        self.timeSum = 0
        self.sampleCount = 0

    def update(self, time):
        self.timeSum += time
        self.sampleCount += 1
        if time < self.minTime:
            self.minTime = time
        if time < self.maxTime:
            self.maxTime = time

    def meanTime(self):
        return self.minTime if self.sampleCount == 0 else self.timeSum / self.sampleCount

vehicleEdges = {}
for vehicle in vehicles:
    vehicleEdges[vehicle] = [None, None]

import traci

PORT = 8888
print("Connecting...")
traci.init(PORT)
print("Simulation started.")
step = 0
edgeTimes = {}
for edge in cityMap.edgeIter():
    edgeTimes[edge.sumo_id] = EdgeTimeStats(traci.edge.getTravelTime(edge.sumo_id))
while traci.simulation.getMinExpectedNumber() > 0:
    traci.simulationStep()
    for vehicle in vehicles:
        edge = traci.vehicle.getRoadID(vehicle)
        previousEdge = vehicleEdges[vehicle][0]
        if previousEdge != edge:
            if previousEdge != None:
                time = step - vehicleEdges[vehicle][1]
                edgeTimes[previousEdge][0] ########################
            vehicleEdges[vehicle][0] = edge
            vehicleEdges[vehicle][1] = step
    #for edge in cityMap.edgeIter():
    #    times[edge.sumo_id].append(traci.edge.getLastStepMeanSpeed(edge.sumo_id))
    #    edge.medium_cost += traci.edge.getTraveltime(edge.sumo_id)
    step += 1

traci.close()

for edge in cityMap.edgeIter():
    edge.medium_cost /= step
    print edge.sumo_id, ',', edgeTimes[edge.sumo_id]

