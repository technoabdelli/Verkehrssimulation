from typing import TypedDict

class CarSnapshot(TypedDict):
    """Zum Erstellen eines Snapshots eines Car-Objekts für die Ausgabe."""
    tick: int
    car_id: int
    x: float
    y: float
    next_node_x: float
    next_node_y: float
    start_node: str
    end_node: str
