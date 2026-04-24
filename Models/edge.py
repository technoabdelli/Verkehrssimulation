class Edge:
    def __init__(self, start_point, end_point):
        self.startPoint = start_point      
        self.endPoint = end_point          
        self.allCarsSum = []                 
        self.knownCars = []
        self.allPointsOnPath = []              

    def getKnownCars(self):
        return self.knownCars

    def getSumAllCars(self) -> int:
        return len(self.allCarsSum)

    def addCar(self, new_car):
        self.allCarsSum.append(new_car)
        if new_car not in self.knownCars:
            self.knownCars.append(new_car)

    def removeCar(self, old_car):
        if old_car in self.allCarsSum:
            self.allCarsSum.remove(old_car)
        if old_car in self.knownCars:
            self.knownCars.remove(old_car)

    def generatePath(self):
        pass