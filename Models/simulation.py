"""Module containing the Simulation class for the traffic simulation."""
import random

from Models.Node import Node
from Models.Car import Car
from Models.car_snapshot import CarSnapshot
from Utils.FIleWriter import FileWriter


class Simulation:
    """A class representing the traffic simulation with all necessary logic to run the simulation"""
    name_simulation: str
    current_time: int
    end_time: int
    all_cars_any_time: list[list[Car]]
    last_car_id: int
    tick_speed: int
    nodes: dict[str, Node]
    snapshot_history: list[list[CarSnapshot]]
    cars_by_id: dict[int, Car]

    def __init__(self):
        self.nodes: dict[str, Node] = {}
        self.all_cars_any_time = []
        self.last_car_id = 0
        self.snapshot_history = []
        self.cars_by_id = {}

    def run(self):
        """Starts the simulation algorithm"""
        curr_tick = 0
        while curr_tick <= self.end_time:
            # Take snapshot of all *currently existing* cars
            snapshot: list[CarSnapshot] = []
            for car in self.cars_by_id.values():
                snapshot.append({
                    "tick": curr_tick,
                    "car_id": car.get_car_id(),
                    "x": car.current_x_position,
                    "y": car.current_y_position,
                    "next_node_x": car.end_node.x_coordinate,
                    "next_node_y": car.end_node.y_coordinate,
                })

            self.snapshot_history.append(snapshot)

            # Generate new cars
            for node in self.nodes.values():
                if curr_tick > 0 and node.is_start_node and (curr_tick % node.chance == 0):
                    car = self.generate_car(self.last_car_id, node)
                    self.cars_by_id[car.get_car_id()] = car
                    self.last_car_id += 1

            # Update all cars
            for car in self.cars_by_id.values():
                car.update_position()

            curr_tick += 1
        FileWriter.write_plan_file("plan.txt", self.nodes)

    def gen_car_speed(self) -> float:
        """Generates the speed of a car"""
        car_speed = random.gauss(mu=45, sigma=1)

        if car_speed < 5:
            car_speed = random.gauss(mu=45, sigma=1)
        return car_speed

    def generate_car(self, car_id: int, start_node: Node) -> 'Car':
        """Generates a new car based on the parameters of the current node"""
        new_car = Car(car_id, self.gen_car_speed(), start_node, start_node.known_neighbours[0][0])
        return new_car

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
