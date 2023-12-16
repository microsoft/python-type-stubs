#!/bin/bash

python -m pip install --upgrade pyright
python -m pip install -r requirements.txt


pyright --pythonversion 3.11 -p pyrighttestconfig.json .
