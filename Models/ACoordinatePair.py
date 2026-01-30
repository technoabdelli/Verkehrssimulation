from abc import ABC, abstractmethod

class ACoordinatePair(ABC):
    @property
    @abstractmethod
    def x_point(self) -> float:
        """Get the X coordinate of the coordinate pair."""
        pass

    @property
    @abstractmethod
    def y_point(self) -> float:
        """Get the Y coordinate of the coordinate pair."""
        pass
    
    @abstractmethod
    def calculcate_distance(self, other: 'ACoordinatePair') -> float:
        """Calculate the distance between this coordinate pair and another."""
        pass
    
    