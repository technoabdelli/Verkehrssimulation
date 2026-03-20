from Models.ACoordinatePair import ACoordinatePair
from Models.Node import Node


class Car():
    """A class representing a car in the traffic simulation."""
    _speed: float
    _car_id: int
    _start_node: Node
    _end_node: Node
    _current_point: ACoordinatePair

    def __init__(self, car_id: int, speed: float, start_node: Node,
                 end_node: Node):
        self._car_id = car_id
        self._speed = speed
        self._start_node = start_node
        self._end_node = end_node
        self._current_point.x_point = start_node.x_point
        self._current_point.y_point = start_node.y_point

    def get_speed(self) -> float:
        """Returns the speed of the car in km/h."""
        return self._speed

    def set_new_speed(self, new_speed: float) -> None:
        """Sets a new speed for the car in km/h. - Only used in the extended version"""
        self._speed = new_speed

    def get_car_id(self) -> int:
        """Returns the unique identifier of the car."""
        return self._car_id

    def get_current_point(self) -> ACoordinatePair:
        """Returns the current coordinate of the car."""
        return self._current_point

    def set_current_point(self, new_point: ACoordinatePair) -> None:
        """Sets a new current coordinate for the car."""
        self._current_point = new_point

    def update_position(self) -> None:
        """Updates the current position of the car based on its speed and direction."""
        speed_in_ms = self._speed / 3.6  # Convert speed from km/h to m/s
        is_path_vertical = self._start_node.x_point == self._end_node.x_point
        is_path_horizontal = self._start_node.y_point == self._end_node.y_point

        if is_path_vertical:
            self._current_point.y_point += speed_in_ms if self._end_node.y_point > self._start_node.y_point else self.turn_corner()

        elif is_path_horizontal:
            self._current_point.x_point += speed_in_ms if self._end_node.x_point > self._start_node.x_point else self.turn_corner()

        else:
            self._current_point.x_point += speed_in_ms if self._end_node.x_point > self._start_node.x_point else self.turn_corner()
            self._current_point.y_point += speed_in_ms if self._end_node.y_point > self._start_node.y_point else self.turn_corner()
         
    def turn_corner(self) -> None:
        """Handles the logic for turning a corner.ys"""
        new_start_node = self._end_node.get_next_node()
        self._start_node = self._end_node
        self._end_node = new_start_node
