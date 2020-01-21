from numpy.random import normal

class ConnectingFlight:
  def __init__(
    self,
    destinationtime,
    flightmean,
    flightstandard
  ):
    self.destinationtime = destinationtime
    self.flightmean = flightmean
    self.flightstandard = flightstandard

  def getFlightTime(self):
    mean = self.flightmean
    std = self.flightstandard

    max = mean + 3 * std
    min = mean - 3 * std
    time =  normal(mean, std, 1)[0]
    if (time > max):
      time = max
    if(time < min):
      time = min
    return time


a1c = {
  'aToB': [ConnectingFlight(8, 4, .25)],
  'bToC': [
    ConnectingFlight(12.5, 4, .25),
    ConnectingFlight(13, 4, .25)
  ],
  'cToD': [
    ConnectingFlight(17, 3.5, .25),
    ConnectingFlight(17.5, 3.5, .25),
    ConnectingFlight(18, 3.5, .25)
  ]

}


a2c = {
  'aToE': [ConnectingFlight(8, 3.5, .5)],
  'eToF': [
    ConnectingFlight(12, 4, .5),
    ConnectingFlight(12.5, 4, .5)
  ],
  'fToD': [
    ConnectingFlight(16.5, 3.5, .5),
    ConnectingFlight(17, 3.5, .5),
    ConnectingFlight(17.5, 3.5, .5)
  ]

}

class FlightTester:
  def __init__(self, connections, lateTime, maxTime):
    self.maxTime = maxTime
    self.lateTime = lateTime
    self.connections = connections

  def toPercentage(self, probability):
    percentage = probability * 100
    return round(percentage, 2)

  def printArrivalTime(self, time):
    hours = int(time)
    minutes = (time*60) % 60
    print("Average Arival Time: %d:%02d" % (hours, minutes))

  def getArrivalTime(self):
    stranded = False
    time = 8
    for flights in self.connections.values():
      for flight in flights:
        if(time <= flight.destinationtime):
          time += flight.destinationtime - time
          time += flight.getFlightTime()
          break
        else:
          stranded = True
          break
    if (stranded == True):
      time = -1
    return time

  def testArrivalTimes(self):
    timesArrivedLate = 0
    timesStranded = 0
    arrivalTimes = 0
    trials = 10000
    for _ in range(trials):
      arrivalTime = self.getArrivalTime()
      if (arrivalTime == -1):
        arrivalTimes += self.maxTime
        timesStranded += 1
      elif(arrivalTime > self.lateTime):
        timesArrivedLate += 1
        arrivalTimes += arrivalTime
      elif(arrivalTime <= self.lateTime):
        arrivalTimes += arrivalTime
    averageArrivalTime = arrivalTimes / trials
    lateProbability = timesArrivedLate / trials
    strandedProbability = timesStranded / trials
    self.printArrivalTime(averageArrivalTime)
    print(f"Late:  {self.toPercentage(lateProbability)}%")
    print('\n')
    print(f"Stranded:  {self.toPercentage(strandedProbability)}%")
    print('\n')

airlineOne = FlightTester(a1c, 21, 22.25)
airlineTwo = FlightTester(a2c, 20.5, 22.5)

print("Airline One:")
airlineOne.testArrivalTimes()
print("Airline Two:")
airlineTwo.testArrivalTimes()










