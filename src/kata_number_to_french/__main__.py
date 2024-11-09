import argparse

from .main import process


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-n", "--numbers", nargs="+", help="list of numbers", required=True
    )

    args = parser.parse_args()

    for num in map(int, args.numbers):
        print(f"{num} => {process(num)}")


if __name__ == "__main__":
    main()
