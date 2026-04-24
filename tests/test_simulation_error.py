import pytest
from Models.simulation import Simulation
from Models.Node import Node

@pytest.mark.parametrize("neighbours", [
    [],  
])
def test_generate_car_no_neighbours(neighbours):
    sim = Simulation()
    node = Node(0, 0, 1, True)
    node.known_neighbours = neighbours

    with pytest.raises(IndexError):
        sim.generate_car(1, node)

@pytest.mark.parametrize("active_states, expected_count", [
    ([True, True, True], 3),
    ([True, False, True], 2),
    ([False, False], 0),
])
def test_remove_inactive_cars(active_states, expected_count):
    sim = Simulation()

    class DummyCar:
        def __init__(self, cid, active):
            self._id = cid
            self.is_active = active

        def get_car_id(self):
            return self._id

    for i, state in enumerate(active_states):
        sim.cars_by_id[i] = DummyCar(i, state)

    sim.remove_inactive_cars()

    assert len(sim.cars_by_id) == expected_count

@pytest.mark.parametrize("row", [
    [],                    
    ["A"],                   
    ["A", "x", "y"],        
])
def test_add_node_invalid(row):
    sim = Simulation()

    with pytest.raises(Exception):
        sim.add_node(row)