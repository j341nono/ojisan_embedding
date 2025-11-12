#!/bin/bash

export PYTHONPATH="./"

DATA_URL="https://github.com/yahoojapan/JGLUE.git"
DATA_PATH="data/JGLUE/datasets/jcommonsenseqa-v1.3/train-v1.3.json"

set -x

mkdir -p data/processed
cd data
git clone "$DATA_URL"
cd ..

uv run src/data_process/data_processer.py --data_path "$DATA_PATH"

