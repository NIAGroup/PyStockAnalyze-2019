#!/bin/bash -e

ROOT_DIR=$(git rev-parse --show-toplevel)
VENV_NAME=pydjango-build-env

python -m venv $ROOT_DIR/build/$VENV_NAME
pip install -r $ROOT_DIR/tools/requirements.txt

# Create activate script pointer
