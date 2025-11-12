import argparse
import json
import random

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--data_path", type=str, required=True)
    parser.add_argument("--seed", type=int, default=33)
    return parser.parse_args()


def load_jsonl(path: str) -> list:
    with open(path, encoding="utf-8") as f:
        jsonl_data = [json.loads(l) for l in f.readlines()]
    return jsonl_data


def data_shuffle(data_list: list, seed: int) -> list:
    shuffled_data_list = data_list.copy()
    rng = random.Random(seed)
    rng.shuffle(shuffled_data_list)
    return shuffled_data_list


def parse_data(raw_data: list):
    for data_line in raw_data:
        data_line.get("question")



def main():
    args = parse_args()

    raw_data = load_jsonl(path=args.data_path)
    shuffled_raw_data = data_shuffle(data_list=raw_data, seed=args.seed)
    



if __name__ == "__main__":
    main()
