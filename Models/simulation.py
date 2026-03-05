from Models.Node import Node
from Models.Car import Car


class simulation:
    """A class representing the traffic simulation, containing all necessary components and logic to run the simulation."""
    graph: list[Node]
    name_simulation: str
    current_time: int
    end_time: int
    allCarsAnyTime: list[list[Car]]
    lastCarId: int
    tick_speed: int
    

    def __init__(self):
        # Initialize the simulation with necessary attributes such as roads, vehicles, traffic lights, etc.
        pass
    
    def run(self):
        # Main method to run the simulation, updating the state of all components at each time step.
        pass
      
    def addNode(self, node: Node):
        """Adds a new node to the simulation graph."""
        if node not in self.graph:
            self.graph.append(node)

        
    