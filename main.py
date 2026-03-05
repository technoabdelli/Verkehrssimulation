# import sys
from Utils.FileReader import FileReader
from Models.simulation import simulation

test_simu = simulation()

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
