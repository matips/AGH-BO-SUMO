__author__ = 'Piotrek'

import os
import sys
import subprocess

# Assertions for "traci" module import:

try:
    if sys.version_info.major != 2:
        sys.exit("SUMO TraCI requires Python version 2.x")
except AttributeError:
    if sys.version[0] != '2':
        sys.exit("SUMO TraCI requires Python version 2.x")


if 'SUMO_HOME' in os.environ:
    sys.path.append(os.path.join(os.environ['SUMO_HOME'], 'tools'))
else:
    sys.exit("Please declare environment variable 'SUMO_HOME'")

import traci


class PathSimulator:
    """
    Runs simulation and measures travel time for given paths.
    """
    PORT = 8888
    STDOUT_FILE = None
    ROUTE_ID = 'highway_to_hell'
    VEHICLE_ID = 'wehikul_czasu'
    RED_COLOR = (255, 0, 0, 0)
    DELTA = 0.01
    STDERR_FILE = open(os.devnull, "w")  # open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../log/sumo_stderr.log'), 'w')

    def __init__(self, sumocfgFileName, graphicMode=False, stepLength=1.0):
        """
        Create a new simulator.

        Args:
            sumocfgFileName: .sumocfg simulation file name
            stepLength: step length (simulation accuracy). Do not change :>
        """
        self.sumocfgFileName = sumocfgFileName
        self.stepLength = stepLength
        self.graphicMode = graphicMode

    def __startSUMOServer(self):
        command = 'sumo-gui' if self.graphicMode else 'sumo'
        return subprocess.Popen(
            [os.path.join(os.environ['SUMO_HOME'], 'bin', command), '--remote-port', str(self.PORT), '--step-length',
             str(self.stepLength), '-c', self.sumocfgFileName], cwd=os.getcwd(), stdout=self.STDOUT_FILE,
            stderr=self.STDERR_FILE)

    def measurePathTime(self, path, departureTime):
        """
        Run the simulation and measure how long does it take for the vehicle to travel the given path.

        Args:
            path: the Path to measure
            departure time: time (in seconds) from the beginning of the simulation when the vehicle should start
        Returns:
            time of the passage (in seconds)
        Raises:
            RuntimeError: if the vehicle has been teleported during the passage. Refer to SUMO docs
        """
        sumoServer = self.__startSUMOServer()

        traci.init(self.PORT)   # connect to server
        traci.route.add(self.ROUTE_ID, path.get_edge_ids())    # add path to simulation
        step = 0
        previousEdge = None
        while traci.simulation.getMinExpectedNumber() > 0:  # while there are vehicles in the simulation
            traci.simulationStep()
            if abs(departureTime-step) < self.DELTA:
                traci.vehicle.add(self.VEHICLE_ID, self.ROUTE_ID)
                traci.vehicle.setColor(self.VEHICLE_ID, self.RED_COLOR)
                previousEdge = traci.vehicle.getRoadID(self.VEHICLE_ID)
            if previousEdge != None:    # vehicle is in the simulation
                try:
                    currentEdge = traci.vehicle.getRoadID(self.VEHICLE_ID)
                except traci.TraCIException:    # vehicle left the simulation - get data and return
                    traci.close()
                    sumoServer.wait()
                    return step - departureTime
                if currentEdge != previousEdge:
                    if currentEdge == '':   # protection against unwanted vehicle teleport (refer to SUMO docs)
                        raise RuntimeError('The vehicle teleported! Cannot measure correct travel time. Try modifying the departure time slightly or assign other path')
                    else:
                        previousEdge = currentEdge
            step += self.stepLength

        raise RuntimeError('The vehicle did not leave the simulation. Perhaps the specified departure time was too late.')
