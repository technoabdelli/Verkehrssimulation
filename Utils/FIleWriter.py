"""Module containing the FileWriter class for writing the output of the simulation to a file."""

from pathlib import Path
from Models.Node import Node

class FileWriter:
    """A starter class that writes the output of the simulation to a file."""
    @staticmethod
    def write_plan_file(filename: str, all_streets: dict[str, Node]) -> None:
        """Writes the plan file with all streets and their coordinates"""
        base_path = Path("Lösungen") / filename
        filepath = base_path.with_name(base_path.name + "_Plan.txt")
        with open(filepath, 'w', encoding='utf-8') as f:
            for node in all_streets.values():
                for end_node, _ in node.known_neighbours:  # Iterate list directly
                    f.write(f"{node.x_coordinate} {node.y_coordinate} "
                          f"{end_node.x_coordinate} {end_node.y_coordinate}\n")

    @staticmethod
    def write_cars_file(filename: str, snapshot_history: dict[int, list[dict]]) -> None:
        """Writes the cars file with the position of all cars at each tick"""
        base_path = Path("Lösungen") / filename
        filepath = base_path.with_name(base_path.name + "_Fahrzeuge.txt")
        with open(filepath, 'w', encoding='utf-8') as f:
            for tick, snapshot in snapshot_history.items():
                f.write(f"*** t = {tick}\n")
                for car in snapshot:
                    f.write(f"{car['x']} {car['y']} "
                          f"{car['next_node_x']} {car['next_node_y']} {car['car_id']}\n")
    @staticmethod
    def write_statistics_file(filename: str, snapshot_history: dict[int, list[dict]]) -> None:
        """Writes the statistics file with total and peak counts per street segment."""
        base_path = Path("Lösungen") / filename
        filepath = base_path.with_name(base_path.name + "_Statistik.txt")
        total_counts: dict[tuple[str, str], int] = {}
        peak_counts: dict[tuple[str, str], int] = {}

        for tick_snapshot in snapshot_history.values():
            tick_segment_counts: dict[tuple[str, str], int] = {}

            for car in tick_snapshot:
                segment = (car['start_node'], car['end_node'])
                total_counts[segment] = total_counts.get(segment, 0) + 1
                tick_segment_counts[segment] = tick_segment_counts.get(segment, 0) + 1

            for segment, count in tick_segment_counts.items():
                peak_counts[segment] = max(peak_counts.get(segment, 0), count)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write("Gesamtanzahl Fahrzeuge pro 100 m:\n")
            for (start_node, end_node), count in sorted(total_counts.items()):
                f.write(f"{start_node} -> {end_node}: {count}\n")

            f.write("\nmaximale Anzahl Fahrzeuge pro 100 m:\n")
            for (start_node, end_node), peak in sorted(peak_counts.items()):
                f.write(f"{start_node} -> {end_node}: {peak}\n")

    @staticmethod
    def write_output_files(simulation_name: str, snapshot_history: dict[int, list[dict]],
                          all_streets: dict[str, Node]) -> None:
        """Method that handles the file writing logic"""
        FileWriter.write_plan_file(simulation_name, all_streets)
        FileWriter.write_cars_file(simulation_name, snapshot_history)
        FileWriter.write_statistics_file(simulation_name, snapshot_history)
