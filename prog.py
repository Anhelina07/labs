import argparse

parser = argparse.ArgumentParser(description="Sum integers")
parser.add_argument("numbers", nargs="*", type=int)
args = parser.parse_args()

print(sum(args.numbers))