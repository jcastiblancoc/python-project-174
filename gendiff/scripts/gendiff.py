# gendiff/scripts/gendiff.py
import argparse
from gendiff import generate_diff

def main():
    parser = argparse.ArgumentParser(
        description="Compares two JSON files and shows the difference."
    )
    parser.add_argument("first_file", help="Path to first JSON file")
    parser.add_argument("second_file", help="Path to second JSON file")
    args = parser.parse_args()

    diff = generate_diff(args.first_file, args.second_file)
    print(diff)

if __name__ == "__main__":
    main()
