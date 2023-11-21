#!/bin/bash

python -m pip install --upgrade pyright
python -m pip install -r requirements.txt

cd ../
python -m isort .
python -m black .
pyright --pythonversion 3.11 -p pyrighttestconfig.json .
