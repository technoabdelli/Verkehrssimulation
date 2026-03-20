import math


class Point:
    def __init__(self, x_point: float, y_point: float):
        self.xPoint = x_point
        self.yPoint = y_point

    def calculateDistance(self, point: "Point") -> float:
        dx = self.xPoint - point.xPoint
        dy = self.yPoint - point.yPoint
        return math.sqrt(dx ** 2 + dy ** 2)
    