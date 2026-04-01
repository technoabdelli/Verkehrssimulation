from Models.Node import node
class SpawnNode:
    """Class that holds all the data for the different spawn points inside of the simulation."""
    node_name: str
    x_coordinate: float
    y_coordinate: float
    known_neighbours: list['node']
    spawn_chance_cars: float

    def __init__(self, node_name: str , x_coord: float, y_coord: float, spawn_chance: float):
        self.node_name = node_name
        self.x_coordinate = x_coord
        self.y_coordinate = y_coord
        self.spawn_chance_cars = spawn_chance

    def from_row(self, row: list[str]) -> 'SpawnNode':
        """Creates an object of the class from a row taken from an input file"""
        self.node_name = row[0]
        self.x_coordinate = row[1]
        self.y_coordinate = row[2]
        self.spawn_chance_cars = row[4]
