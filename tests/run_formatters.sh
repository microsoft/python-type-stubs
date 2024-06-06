#!/bin/bash
test_folder=$(dirname "${BASH_SOURCE[0]}")
root=$(dirname $test_folder)

python -m pip install --upgrade isort black

cd $root
python -m isort .
python -m black .
