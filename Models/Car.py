from Models.ACoordinatePair import ACoordinatePair
from Models.Node import Node

class Car():
    """A class representing a car in the traffic simulation."""
    _speed: float
    _car_id: int
    start_node: Node
    is_active: bool
    end_node: Node
    current_x_position: float
    current_y_position: float
    _current_point: ACoordinatePair

    def __init__(self, car_id: int, speed: float, start_node: Node,
                 end_node: Node):
        if speed < 0:
            raise ValueError("Geschwindigkeit darf nicht negativ sein")
        
        if start_node is None or end_node is None:
            raise ValueError("Start und Ende dürfen nicht leer sein")

        self._car_id = car_id
        self._speed = speed
        self.start_node = start_node
        self.is_active = True
        self.end_node = end_node
        self.current_x_position = start_node.x_coordinate
        self.current_y_position = start_node.y_coordinate

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
        speed_in_ms = self._speed / 3.6  # km/h -> m/s
        speed_for_algorithm = speed_in_ms / 100

        is_path_vertical = self.start_node.x_coordinate == self.end_node.x_coordinate
        is_path_horizontal = self.start_node.y_coordinate == self.end_node.y_coordinate

        if is_path_vertical:
            dy = self.end_node.y_coordinate - self.start_node.y_coordinate
            direction_y = 1 if dy > 0 else -1  # up or down
            self.current_y_position += direction_y * speed_for_algorithm

            # when we reach or pass the target, turn
            if (direction_y > 0 and self.current_y_position >= self.end_node.y_coordinate) or \
            (direction_y < 0 and self.current_y_position <= self.end_node.y_coordinate):
                self.turn_corner()

        elif is_path_horizontal:
            dx = self.end_node.x_coordinate - self.start_node.x_coordinate
            direction_x = 1 if dx > 0 else -1  # right or left
            self.current_x_position += direction_x * speed_for_algorithm

            if (direction_x > 0 and self.current_x_position >= self.end_node.x_coordinate) or \
            (direction_x < 0 and self.current_x_position <= self.end_node.x_coordinate):
                self.turn_corner()

        else:
            # diagonal / general case: move in both x and y
            dx = self.end_node.x_coordinate - self.start_node.x_coordinate
            dy = self.end_node.y_coordinate - self.start_node.y_coordinate

            direction_x = 1 if dx > 0 else -1
            direction_y = 1 if dy > 0 else -1

            self.current_x_position += direction_x * speed_for_algorithm
            self.current_y_position += direction_y * speed_for_algorithm

            reached_x = (direction_x > 0 and self.current_x_position >= self.end_node.x_coordinate) or \
                        (direction_x < 0 and self.current_x_position <= self.end_node.x_coordinate)
            reached_y = (direction_y > 0 and self.current_y_position >= self.end_node.y_coordinate) or \
                        (direction_y < 0 and self.current_y_position <= self.end_node.y_coordinate)

            if reached_x and reached_y:
                self.turn_corner()

    def turn_corner(self) -> None:
        """Handles the logic for turning a corner."""        
        self.current_x_position = self.end_node.x_coordinate
        self.current_y_position = self.end_node.y_coordinate

        if self.end_node.is_start_node:
            self.is_active = False
            return
        new_start_node = self.end_node.get_next_node()
        self.start_node = self.end_node
        self.end_node = new_start_node
