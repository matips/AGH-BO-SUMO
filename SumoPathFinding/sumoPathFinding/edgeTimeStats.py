__author__ = 'Piotrek'

class EdgeTimeStats:
    def __init__(self, estimatedTime):
        self.minTime = float('inf')
        self.maxTime = estimatedTime
        self.timeSum = 0.0
        self.sampleCount = 0

    def update(self, time):
        self.timeSum += time
        self.sampleCount += 1
        if time < self.minTime:
            self.minTime = time
        if time > self.maxTime:
            self.maxTime = time

    def meanTime(self):
        return self.minTime if self.sampleCount == 0 else self.timeSum / self.sampleCount

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return str(self.minTime) + ", " + str(self.maxTime) + ", " + str(self.meanTime())
