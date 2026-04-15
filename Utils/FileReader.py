"""Module containing the FileReader class for reading and parsing the input file."""

from pathlib import Path

from Models.simulation import Simulation

class FileReader:
    """A helper class that handles the input file reading and parsing."""
    @staticmethod
    def read_input_file(file_path: str, simu: 'Simulation') -> None:
        """Method that handles the file reading logic"""
        file_path = Path(file_path)
        simu.name_simulation = file_path.parent.name
        
        params: dict[str, list[list[str]]] = {}
        current_key: str | None = None

        with open(file_path, 'r', encoding='utf-8') as file:
            for raw in file:
                line = raw.strip()

                if not line:
                    continue

                if line.startswith('#'):
                    continue

                if line.endswith(':'):
                    current_key = line[:-1]
                    params[current_key] = []
                else:
                    if current_key is not None:
                        params[current_key].append(line.split())


        if 'Zeitraum' in params and params['Zeitraum']:
            row = params['Zeitraum'][0]
            simu.end_time = int(row[0])
            simu.tick_speed = int(row[1])

        # Pass 1 & 2: create all nodes first
        for row in params.get('Einfallspunkte', []):
            simu.add_einfallspunkt(row)

        for row in params.get('Kreuzungen', []):
            simu.add_node(row)

        # Pass 3 & 4: wire everything now that all nodes exist
        for row in params.get('Einfallspunkte', []):
            simu.link_einfallspunkt_neighbour(row)

        for row in params.get('Kreuzungen', []):
            simu.link_node_neighbours(row)
