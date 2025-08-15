# gendiff/scripts/gendiff.py
import argparse
from gendiff import generate_diff

def main():
    parser = argparse.ArgumentParser(
        description="Compares two files and shows the difference."
    )
    parser.add_argument("first_file", help="Path to first JSON file")
    parser.add_argument("second_file", help="Path to second JSON file")
    parser.add_argument(
        "-f", "--format",
        dest="format_name",
        choices=["stylish", "plain", "json"],
        default="stylish",
        help="Output format (stylish, plain, or json)"
    )
    args = parser.parse_args()

    diff = generate_diff(args.first_file, args.second_file, args.format_name)
    print(diff)

if __name__ == "__main__":
    main()
