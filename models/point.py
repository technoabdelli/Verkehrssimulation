import math


class Point:
    def __init__(self, x_point: float, y_point: float):
        self.x_point = x_point
        self.y_point = y_point

    def calculate_distance(self, point: "Point") -> float:
        """Calculates distance between two points"""
        dx = self.x_point - point.x_point
        dy = self.y_point - point.y_point
        return math.sqrt(dx ** 2 + dy ** 2)
