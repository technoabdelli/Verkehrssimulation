import pytest
from anwendung.us1 import DatenEinlesen

def test_datei_nicht_gefunden():
    daten = DatenEinlesen("datei_gibt_es_nicht.txt")

    with pytest.raises(Exception) as e:
        daten.einlesen()

    assert "nicht gefunden" in str(e.value)

    