from Models import ACoordinatePair


class Car():
    _speed: float
    _car_id: int
    _start_point: ACoordinatePair
    _end_point: ACoordinatePair
    _current_point: ACoordinatePair
    
    def __init__(self, car_id: int, speed: float, start_point: ACoordinatePair, end_point: ACoordinatePair):
        self._car_id = car_id
        self._speed = speed
        self._start_point = start_point
        self._end_point = end_point
        self._current_point = start_point
        
    def get_speed(self) -> float:
        """Returns the speed of the car in km/h."""
        return self._speed
    
    def set_new_speed(self, new_speed: float) -> None:
        """Sets a new speed for the car in km/h. - Only used in the extended version"""
        self._speed = new_speed
        
    def get_car_id(self) -> int:
        """Returns the unique identifier of the car."""
        return self._car_id
    
    def get_start_point(self) -> ACoordinatePair:
        """Returns the starting coordinate of the car."""
        return self._start_point
      
    def get_end_point(self) -> ACoordinatePair:
        """Returns the ending coordinate of the car."""
        return self._end_point
      
    def get_current_point(self) -> ACoordinatePair:
        """Returns the current coordinate of the car."""
        return self._current_point
      
    def set_current_point(self, new_point: ACoordinatePair) -> None:
        self._current_point = new_point
        
    def set_start_point(self, new_start_point: ACoordinatePair) -> None:
        self._start_point = new_start_point
        
    def set_end_point(self, new_end_point: ACoordinatePair) -> None:
        self._end_point = new_end_point
        
    def update_position(self, new_point: ACoordinatePair) -> None:
        speed_in_ms = self._speed / 3.6  # Convert speed from km/h to m/s
        
        is_path_vertical = self._start_point.x_point == self._end_point.x_point
        is_path_horizontal = self._start_point.y_point == self._end_point.y_point
        
        if is_path_vertical:
            self._current_point.y_point += speed_in_ms if self._end_point.y_point > self._start_point.y_point else self.turn_corner()
        
        elif is_path_horizontal:
            self._current_point.x_point += speed_in_ms if self._end_point.x_point > self._start_point.x_point else self.turn_corner()
            
        else:
            self._current_point.x_point += speed_in_ms if self._end_point.x_point > self._start_point.x_point else self.turn_corner()
            self._current_point.y_point += speed_in_ms if self._end_point.y_point > self._start_point.y_point else self.turn_corner()
            
    def turn_corner(self) -> None:
        """Handles the logic for turning a corner. - Only used in the extended version"""
        pass
