from anwendung.us1 import DatenEinlesen
from anwendung.us4 import DateiValidierung
from Models.edge import Edge
from Utils.FileReader import FileReader
from Models.simulation import Simulation

def main():
    try:
        dateiname = input("Bitte geben Sie die Name Ihre Datei ")
        daten = DatenEinlesen(dateiname)
        daten.einlesen()
        
        DateiValidierung.validierung(daten)
        print("\nDatei korrekt eingelesen!\n")
        print("Zeitraum:", daten.zeitraum.startpunkt, "-", daten.zeitraum.endpunkt)

        for ep in daten.einfallspunkte:
            print("EP:", ep.name, ep.x, ep.y)

        for k in daten.kreuzungen:
            print("K:", k.name, k.x, k.y)

        print("\nSimulation erfolgreich initialisiert \n")

    except Exception as e:
        print("Fehler beim Einlesen:", e)
    


if __name__ == "__main__":
    main()
# import sys


test_simu = Simulation()

def main(args):
    """Main entry point for the program, handling cmd-line arguments and starting the simulation."""
    if len(args) != 2:
        print("Usage: python main.py <name>")
        return

    name = args[1]
    print(f"Hello, {name}!")

if __name__ == "__main__":
    # main(sys.argv)
    FileReader.read_input_file("C:\\Users\\Lisa.Kortkamp\\Documents\\Schul_Dokumente\\LF13\\Montagsprodukt\\Verkehrssimulation\\IHK_01\\Eingabe.txt", test_simu)
