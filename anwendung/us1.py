class Zeitraum:
    def __init__(self, startpunkt: int, endpunkt: int):
        self.startpunkt = startpunkt
        self.endpunkt = endpunkt


class Einfallspunkt:
    def __init__(self, name: str, x: float, y: float):
        self.name = name
        self.x = x
        self.y = y


class Kreuzung:
    def __init__(self, name: str, x: float, y: float):
        self.name = name
        self.x = x
        self.y = y

class DatenEinlesen:
    def __init__(self, datei: str):
        self.datei = datei
        self.zeitraum = None
        self.einfallspunkte = []
        self.kreuzungen = []

    def einlesen(self):
        try:
            with open(self.datei, "r") as f:
                zeilen = [z.strip() for z in f.readlines()]
        except FileNotFoundError:
            raise Exception(f"Datei {self.datei} nicht gefunden")

        abschnitt = None

        for zeile in zeilen:
            if not zeile or zeile.startswith("#"):
                continue

            if zeile.startswith("[") and zeile.endswith("]"):
                abschnitt = zeile[1:-1]
                continue

            if abschnitt == "Zeit":
                startpunkt, endpunkt = zeile.split()
                self.zeitraum = Zeitraum(int(startpunkt), int(endpunkt))

            elif abschnitt == "Einfallspunkte":
                name, x, y = zeile.split()
                self.einfallspunkte.append(
                    Einfallspunkt(name, float(x), float(y))
                )

            elif abschnitt == "Kreuzungen":
                name, x, y = zeile.split()
                self.kreuzungen.append(
                    Kreuzung(name, float(x), float(y))
                )
            else:
                raise Exception(f"Unbekannter Fehler im Datei: {abschnitt}")
                    
        return self