#!/bin/bash

python -m pip install isort black -U

cd ../
# TODO: Remove --check-only and fix all
python -m isort . --check-only
# TODO: Remove --check and fix all
python -m black . --check
