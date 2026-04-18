import pytest
from Models.edge import Edge

@pytest.mark.parametrize("car", [
    None,
])
def test_add_car_invalid(car):
    edge = Edge(object(), object())

    edge.addCar(car)

    assert car in edge.allCarsSum

@pytest.mark.parametrize("car", [
    object(),
])
def test_remove_non_existing_car(car):
    edge = Edge(object(), object())

    edge.removeCar(car)

    assert edge.getSumAllCars() == 0
    assert len(edge.getKnownCars()) == 0

def test_add_car_duplicate():
    edge = Edge(object(), object())
    car = object()

    edge.addCar(car)
    edge.addCar(car)

    assert edge.getSumAllCars() == 2        
    assert len(edge.getKnownCars()) == 1 