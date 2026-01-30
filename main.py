import sys

def main(args):
    if len(args) != 2:
        print("Usage: python main.py <name>")
        return

    name = args[1]
    print(f"Hello, {name}!")
    
if __name__ == "__main__":
    main(sys.argv)
