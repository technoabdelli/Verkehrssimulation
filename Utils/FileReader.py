
from Models.simulation import simulation

class FileReader:
    """A utility class for reading and parsing input files for the traffic simulation."""
    @staticmethod
    def read_input_file(file_path: str, simu: simulation) -> None:
        """Reads the input file and populates the given simulation object.

        The format expected is a parameter header on its own line ending with a
        colon (for example ``Zeitraum:`` or ``Node:``) followed by a line of
        space-separated values. This method collects all such settings in a
        dictionary attached to ``simu`` as ``simu.parameters`` so the simulation
        logic can access them later.
        """

        params: dict[str, list[str]] = {}

        with open(file_path, 'r', encoding='utf-8') as file:
            for raw in file:
                line = raw.strip()
                if not line or line.startswith('#'):
                    # name comment is stored separately
                    if line.startswith('#'):
                        name = line.lstrip('#').strip()
                        simu.name_simulation = name
                    continue

                if line.endswith(':'):
                    key = line[:-1]
                    # consume next non-empty, non-comment line for values
                    for values_raw in file:
                        value_line = values_raw.strip()
                        if value_line and not value_line.startswith('#'):
                            break
                    else:
                        # no more lines
                        break
                    params[key] = value_line.split()
                else:
                    # if you expect standalone lines not prefixed by a parameter, handle
                    # them here or log a warning
                    pass

        setattr(simu, 'parameters', params)

        # example of assigning common parameters directly
        if 'Zeitraum' in params and len(params['Zeitraum']) >= 2:
            try:
                simu.current_time = int(params['Zeitraum'][0])
                simu.end_time = int(params['Zeitraum'][1])
            except ValueError:
                # leave them as strings or handle error
                simu.current_time, simu.end_time = params['Zeitraum'][:2]
