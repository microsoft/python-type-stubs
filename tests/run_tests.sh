#!/bin/bash

python -m pip install -r requirements.txt -U

cd ../
# TODO: Remove --check-only and fix all
python -m isort . --check-only
# TODO: Remove --check and fix all
python -m black . --check
python -m mypy .
npx -y pyright@latest .
