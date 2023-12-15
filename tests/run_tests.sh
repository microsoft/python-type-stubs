#!/bin/bash

python -m pip install -r requirements.txt -U

cd ../
python -m mypy .
npx -y pyright@latest .
