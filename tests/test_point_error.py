import pytest
from Models.point import Point


@pytest.mark.parametrize("invalid_point", [
    None,
    "not_a_point",
    123,
    [],
    {},
])

def test_calculate_distance_invalid_input(invalid_point):
    p1 = Point(0, 0)

    with pytest.raises(Exception):
        p1.calculateDistance(invalid_point)

@pytest.mark.parametrize("x, y", [
    (0, 0),
    (5, 5),
    (-10, 20),
])

def test_same_point_distance_zero(x, y):
    p = Point(x, y)

    assert p.calculateDistance(p) == 0

@pytest.mark.parametrize("p1, p2, expected", [
    (Point(-1, -1), Point(-4, -5), 5.0),
    (Point(-2, 3), Point(2, -3), pytest.approx(7.21, 0.01)),
])
def test_negative_coordinates(p1, p2, expected):
    assert p1.calculateDistance(p2) == expected