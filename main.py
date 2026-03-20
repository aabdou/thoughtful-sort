from argparse import ArgumentParser
from robot import sort

def main():
    parser = ArgumentParser()
    parser.add_argument("--width_cm", type=float, required=True)
    parser.add_argument("--height_cm", type=float, required=True)
    parser.add_argument("--length_cm", type=float, required=True)
    parser.add_argument("--mass_kg", type=float, required=True)

    args = parser.parse_args()
    res = sort(args.width_cm, args.height_cm, args.length_cm, args.mass_kg)
    print(f"The package will be added to the stack {res.value}")

if __name__ == "__main__":
    main()