__author__ = 'Piotrek'

class EdgeTimeStats:
    def __init__(self, estimatedTime):
        self.__minTime = float('inf')
        self.__maxTime = estimatedTime
        self.__timeSum = 0.0
        self.__sampleCount = 0
        self.__estimatedTime = estimatedTime

    def update(self, time):
        self.__timeSum += time
        self.__sampleCount += 1
        if time < self.__minTime:
            self.__minTime = time
        if time > self.__maxTime:
            self.__maxTime = time

    def getMinTime(self):
        return self.__estimatedTime if self.__sampleCount == 0 else self.__minTime

    def getMaxTime(self):
        return self.__estimatedTime if self.__sampleCount == 0 else self.__maxTime

    def getMeanTime(self):
        return self.__estimatedTime if self.__sampleCount == 0 else self.__timeSum / self.__sampleCount

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return str(self.getMinTime()) + ", " + str(self.getMaxTime()) + ", " + str(self.getMeanTime())
