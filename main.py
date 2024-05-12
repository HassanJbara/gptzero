import argparse
import json

from gptzero import GPT2PPL


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_file", type=str, default="input.txt")

    args = parser.parse_args()
    print("input args:\n", json.dumps(vars(args), indent=4, separators=(",", ":")))
    return args

def main(args):
    zero_gpt = GPT2PPL()

    with open(args.input_file, "r") as f:
        text = f.read().strip()
        print(zero_gpt.getScore(text))


if __name__ == '__main__':
    args = parse_args()
    main(args)