import pytest
from Models.Car import Car

class DummyNode:
    def __init__(self, x, y, is_start_node=False, next_node=None):
        self.x_coordinate = x
        self.y_coordinate = y
        self.is_start_node = is_start_node
        self._next_node = next_node

    def get_next_node(self):
        return self._next_node

@pytest.mark.parametrize("car_id, speed, start_node, end_node", [
    (1, -10, DummyNode(0, 0), DummyNode(1, 1)),   # negative Geschwindigkeit
    (1, 50, None, DummyNode(1, 1)),              # start_node leer
    (1, 50, DummyNode(0, 0), None),              # end_node leer
])
def test_invalid_initialization(car_id, speed, start_node, end_node):
    with pytest.raises(Exception):
        Car(car_id, speed, start_node, end_node)

@pytest.mark.parametrize("x, y", [
    (0, 0),
    (5, 5),
])

def test_same_start_end_node(x, y):
    node = DummyNode(x, y)
    car = Car(1, 50, node, node)

    car.update_position()

    assert car.current_x_position == x
    assert car.current_y_position == y

def test_zero_speed_no_movement():
    start = DummyNode(0, 0)
    end = DummyNode(10, 0)

    car = Car(1, 0, start, end)
    old_x = car.current_x_position

    car.update_position()

    assert car.current_x_position == old_x