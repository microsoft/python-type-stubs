#!/bin/bash
test_folder=$(dirname "${BASH_SOURCE[0]}")
root=$(dirname $test_folder)

python -m pip install -r $test_folder/requirements.txt -U

cd $root
python -m mypy .
npx -y pyright@latest .
