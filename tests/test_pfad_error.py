import pytest
from anwendung.us1 import DatenEinlesen
from anwendung.us4 import DateiValidierung


def create_temp_file(tmp_path, content: str):
    file = tmp_path / "test_input.txt"
    file.write_text(content)
    return str(file)


@pytest.mark.parametrize("input_data, expected_error", [

    (
        """
        [Einfallspunkte]
        EP1 0 0
        """,
        "Zeit"
    ),

    (
        """
        [Zeit]
        0

        [Kreuzungen]
        K1 0 0
        """,
        "invalid"
    ),

    (
        """
        [Zeit]
        0 100

        [Kreuzungen]
        K1 0
        """,
        "split"
    ),

    (
        """
        [Zeit]
        0 100

        [Kreuzungen]
        K1 x y
        """,
        "could"
    ),

    (
        "",
        "Zeit"
    ),
])
def test_pfad_error_cases(tmp_path, input_data, expected_error):
    file_path = create_temp_file(tmp_path, input_data)

    parser = DatenEinlesen(file_path)

    with pytest.raises(Exception) as exc_info:
        daten = parser.einlesen()
        DateiValidierung.validierung(daten)

    assert isinstance(exc_info.value, Exception)