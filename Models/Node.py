import random


class Node:
    """A class representing a node in the traffic simulation."""
    node_name: str
    x_coordinate: float
    y_coordinate: float
    known_neighbours: list[tuple['Node', float]]
    chance: float
    is_start_node: bool

    def __init__(self, x_coordinate: float, y_coordinate: float, chance: float, is_start: bool):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.chance = chance
        self.is_start_node = is_start
        self.known_neighbours: list[tuple['Node', float]] = []

    def from_row(self, row: list[str]) -> 'Node':
        """Implements the data from a passed list of data"""
        self.node_name = row[0]
        self.x_coordinate = float(row[1])
        self.y_coordinate = float(row[2])

    def add_neighbours(self, new_node: 'Node', weight: float = 0.0):
        """Adds neighbouring nodes to form a graph"""
        if new_node not in [n for n, _ in self.known_neighbours]:
            self.known_neighbours.append((new_node, weight))

    def get_next_node(self) -> 'Node':
        """Returns the next node"""
        nodes, weights = zip(*self.known_neighbours)
        total = sum(weights)
        if total == 0:
            return random.choice(nodes)
        return random.choices(nodes, weights=[w/total for w in weights], k=1)[0]
