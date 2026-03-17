from abc import ABC, abstractmethod

class ACoordinatePair(ABC):
    """An abstract class representing a coordinate pair (x, y) in the traffic simulation."""    
    @property
    @abstractmethod
    def x_point(self) -> float:
        """Get the X coordinate of the coordinate pair."""  

    @property
    @abstractmethod
    def y_point(self) -> float:
        """Get the Y coordinate of the coordinate pair."""

    @abstractmethod
    def calculcate_distance(self, other: 'ACoordinatePair') -> float:
        """Calculate the distance between this coordinate pair and another.""" 
