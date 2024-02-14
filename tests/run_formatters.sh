#!/bin/bash
test_folder=$(dirname "${BASH_SOURCE[0]}")
root=$(dirname $test_folder)

python -m pip install isort black -U

cd $root
# TODO: Remove --check-only and fix all
python -m isort . --check-only
# TODO: Remove --check and fix all
python -m black . --check
