class DateiValidierung:
    
    @staticmethod
    def validierung(daten):
        fehler = []

        if daten.zeitraum is None:
            fehler.append("Fehler: Zeitabschnitt fehlt.")

        if not daten.einfallspunkte:
            fehler.append("Fehler: Keine Einfallspunkte definiert.")
        else:
            for ep in daten.einfallspunkte:
                if not ep.name or ep.x is None or ep.y is None:
                    fehler.append(f"Fehler: Ungültiger Einfallspunkt {ep}")

        if not daten.kreuzungen:
            fehler.append("Fehler: Keine Kreuzungen definiert.")
        else:
            for k in daten.kreuzungen:
                if not k.name or k.x is None or k.y is None:
                    fehler.append(f"Fehler: Ungültige Kreuzung {k}")

        if fehler:
            for f in fehler:
                print(f)
            raise Exception("Validierungsfehler: Eingabedatei ungültig.")
