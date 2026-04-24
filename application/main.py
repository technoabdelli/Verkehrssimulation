from anwendung.us1 import DatenEinlesen
from anwendung.us4 import DateiValidierung
from Utils.FileReader import FileReader
from Models.simulation import Simulation


def initialisiere_daten(dateiname: str): #US1 und US4
    daten = DatenEinlesen(dateiname)
    daten.einlesen()

    DateiValidierung.validierung(daten)

    return daten


def zeige_eingabedaten(daten):   #Debug_ausgabe
    print("\nDatei korrekt eingelesen!\n")
    print("Zeitraum:", daten.zeitraum.startpunkt, "-", daten.zeitraum.endpunkt)

    for ep in daten.einfallspunkte:
        print("EP:", ep.name, ep.x, ep.y)

    for k in daten.kreuzungen:
        print("K:", k.name, k.x, k.y)


def starte_simulation(dateiname: str):  #Simulation starten
    daten = initialisiere_daten(dateiname)

    zeige_eingabedaten(daten)

    simulation = Simulation()

    FileReader.read_input_file(dateiname, simulation)

    print("\nSimulation wird gestartet...\n")
    simulation.run()

    print("\nSimulation erfolgreich beendet.\n")


def main():
    try:
        dateiname = input("Bitte geben Sie den Namen Ihrer Datei ein: ")
        starte_simulation(dateiname)

    except Exception as e:
        print("Fehler:", e)


if __name__ == "__main__":
    main()