import random


class Node:
    """A class representing a node in the traffic simulation."""
    _x_coordinate: float
    _y_coordinate: float
    _known_neighbours: list['Node']
    turning_chance: float
    def __init__(self, x_coordinate: float, y_coordinate: float, turning_chance: float):
        self._x_coordinate = x_coordinate
        self._y_coordinate = y_coordinate
        self.turning_chance = turning_chance

    def add_neighbours(self, new_node: 'Node'):
       """Adds a new node to the known neighbour lists to simulate a graph"""
       if(new_node not in self._known_neighbours):
          self._known_neighbours.append(new_node)
    
    def get_next_node(self) -> 'Node':
      """Returns a weighted random node from known neighbours based on turning chances."""
      
      total_chance = sum(node.turning_chance for node in self._known_neighbours)
      if total_chance == 0:
        return random.choice(self._known_neighbours)
      
      normalized_chances = [node.turning_chance / total_chance for node in self._known_neighbours]
      return random.choices(self._known_neighbours, weights=normalized_chances, k=1)[0]
