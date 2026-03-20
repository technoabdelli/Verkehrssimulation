from anwendung.us1 import DatenEinlesen
from anwendung.us4 import DateiValidierung
from modulen.edge import Edge


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