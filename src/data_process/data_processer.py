import argparse
import json
import random
import sys


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--data_path", type=str, required=True)
    parser.add_argument("--save_path", type=str, default="data/processed")
    parser.add_argument("--seed", type=int, default=33)
    return parser.parse_args()


def load_jsonl(path: str) -> list:
    with open(path, "r", encoding="utf-8") as f:
        d = json.load(f)
    return d


def save_jsonl(save_file_path: str, save_data: list) -> None:
    with open(save_file_path, 'w', encoding="utf-8") as f:
        lines_to_write = [json.dumps(l, ensure_ascii=False) + '\n' for l in save_data]
        f.writelines(lines_to_write)


def data_shuffle(data_list: list, seed: int) -> list:
    shuffled_data_list = data_list.copy()
    rng = random.Random(seed)
    rng.shuffle(shuffled_data_list)
    return shuffled_data_list


def parse_data(raw_data: list):
    choiced_data = []
    for data_line in raw_data:
        question_text = data_line.get("sentence")
        if len(question_text) < 15 or len(question_text) > 50:
            continue
        choiced_data.append(data_line)
    return choiced_data


def main():
    args = parse_args()

    raw_data = load_jsonl(path=args.data_path)
    shuffled_raw_data = data_shuffle(data_list=raw_data, seed=args.seed)
    choiced_data = parse_data(raw_data=shuffled_raw_data)

    choiced_data = choiced_data[:3000]

    save_file_path = f"{args.save_path}/choiced_data.jsonl"
    save_jsonl(save_file_path=save_file_path, save_data=choiced_data)


if __name__ == "__main__":
    main()
