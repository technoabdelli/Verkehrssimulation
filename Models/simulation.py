from Models.Node import Node
from Models.Car import Car


class Simulation:
    """A class representing the traffic simulation, containing all necessary components and logic to run the simulation."""
    name_simulation: str
    current_time: int
    end_time: int
    allCarsAnyTime: list[list[Car]]
    lastCarId: int
    tick_speed: int

    def __init__(self):
        self.nodes: dict[str, Node] = {}

    def run(self):
        """Starts the algorithm to solve the simulation."""
        currTick = 0;
        while(currTick <= self.end_time):
           pass 

    def add_node(self, row: list[str]) -> None:
        """Pass 1: Creates a Kreuzung node and stores it.
        row format: [node_id, x, y, neighbour1, weight1, ...]"""
        n = Node(
            x_coordinate = float(row[1]),
            y_coordinate = float(row[2]),
            chance       = 0.0,
            is_start     = False
        )
        n.from_row(row)
        self.nodes[n.node_name] = n

    def add_einfallspunkt(self, row: list[str]) -> None:
        """Pass 1: Creates a start node and stores it, no wiring yet.
        row format: [node_id, x, y, target_node, spawn_interval]"""
        n = Node(
            x_coordinate = float(row[1]),
            y_coordinate = float(row[2]),
            chance       = float(row[4]),
            is_start     = True
        )
        n.from_row(row)
        self.nodes[n.node_name] = n

    def link_node_neighbours(self, row: list[str]) -> None:
        """Pass 2: Wires up neighbours for a Kreuzung node.
        row format: [node_id, x, y, neighbour1, weight1, neighbour2, weight2, ...]"""
        source = self.nodes[row[0]]
        for i in range(3, len(row), 2):
            neighbour = self.nodes[row[i]]
            weight = float(row[i + 1])
            source.add_neighbours(neighbour, weight)

    def link_einfallspunkt_neighbour(self, row: list[str]) -> None:
        """Pass 2: Wires a start node to its single target.
        row format: [node_id, x, y, target_node, spawn_interval]"""
        source = self.nodes[row[0]]
        target = self.nodes[row[3]]
        source.add_neighbours(target, weight=0.0)
