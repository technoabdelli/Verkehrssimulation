import pytest
from Models.Node import Node

@pytest.mark.parametrize("row", [
    [],                         
    ["A"],                      
    ["A", "x", "y"],            
])
def test_from_row_invalid(row):
    node = Node(0, 0, 0.5, False)

    with pytest.raises(Exception):
        node.from_row(row)

@pytest.mark.parametrize("new_node", [
    None,
])
def test_add_neighbour_invalid(new_node):
    node = Node(0, 0, 0.5, False)

    node.add_neighbours(new_node)

    assert (new_node, 0.0) in node.known_neighbours
    
def test_add_neighbour_duplicate():
    node1 = Node(0, 0, 0.5, False)
    node2 = Node(1, 1, 0.5, False)

    node1.add_neighbours(node2)
    node1.add_neighbours(node2)

    assert len(node1.known_neighbours) == 1