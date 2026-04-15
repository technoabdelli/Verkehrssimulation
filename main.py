# from anwendung.us1 import DatenEinlesen
# from anwendung.us4 import DateiValidierung


# def main():
#     try:
#         dateiname = input("Bitte geben Sie die Name Ihre Datei ")
#         daten = DatenEinlesen(dateiname)
#         daten.einlesen()

#         DateiValidierung.validierung(daten)
#         print("\nDatei korrekt eingelesen!\n")
#         print("Zeitraum:", daten.zeitraum.startpunkt, "-", daten.zeitraum.endpunkt)

#         for ep in daten.einfallspunkte:
#             print("EP:", ep.name, ep.x, ep.y)

#         for k in daten.kreuzungen:
#             print("K:", k.name, k.x, k.y)

#         print("\nSimulation erfolgreich initialisiert \n")

#     except Exception as e:
#         print("Fehler beim Einlesen:", e)



# if __name__ == "__main__":
#     main()
# import sys
from pathlib import Path
from Utils.FileReader import FileReader
from Models.simulation import Simulation

Simulation = Simulation()

def main():
    """Main function to run the traffic simulation for all input files in the specified folder."""
    base_folder  = Path("Eingabedatei")

    for file_path in base_folder.rglob("*.txt"):
        relative_path = file_path.relative_to(base_folder)
        print(f"Wird bearbeitet: {relative_path}")

        FileReader.read_input_file(file_path, Simulation)
        Simulation.run()
        Simulation.reset()  # Reset the simulation for the next file
        print(f"Wurde fertig bearbeitet: {file_path.name}\n")

    print('Die fertigen Dateien finden Sie im Ordner "Lösungen"')

if __name__ == "__main__":
    main()
