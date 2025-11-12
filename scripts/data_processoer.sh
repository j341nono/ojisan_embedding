#!/bin/bash

export PYTHONPATH="./"

DATA_URL="https://github.com/EhimeNLP/WRIME-v4.git"
DATA_PATH="data/WRIME-v4/data.json"

set -x

mkdir -p data/processed
cd data
git clone "$DATA_URL"
cd ..

# uv run src/data_process/data_processer.py --data_path "$DATA_PATH"

