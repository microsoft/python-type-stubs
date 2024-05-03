#!/bin/bash
test_folder=$(dirname "${BASH_SOURCE[0]}")
root=$(dirname $test_folder)

python -m pip install --upgrade -r $test_folder/requirements.txt

cd $root
python -m mypy .
pyright .
