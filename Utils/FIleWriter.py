"""Module containing the FileWriter class for writing the output of the simulation to a file."""

from Models.Node import Node

class FileWriter:
    """A starter class that writes the output of the simulation to a file."""
    @staticmethod
    def write_plan_file(filename: str, all_streets: dict[str, Node]) -> None:
        """Writes the plan file with all streets and their coordinates"""
        with open(filename, 'w', encoding='utf-8') as f:
            for node in all_streets.values():
                for end_node, _ in node.known_neighbours:  # Iterate list directly
                    f.write(f"{node.x_coordinate} {node.y_coordinate} "
                          f"{end_node.x_coordinate} {end_node.y_coordinate}\n")


    @staticmethod
    def write_output_file(file_path: str, snapshot_his: list[list[dict]],
                          all_streets: dict[str, Node]) -> None:
        """Method that handles the file writing logic"""
        with open(file_path, 'w', encoding='utf-8') as file:
            FileWriter.write_plan_file(file, all_streets)
