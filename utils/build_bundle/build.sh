#!/bin/sh

python -m pip install --upgrade pandas
python -m pip install --upgrade pyright
python -m pip install --upgrade docopt

mkdir -p stubs

# Copy over the stubs from here

for d in cv2-stubs django gym-stubs jmespath matplotlib openpyxl scipy-stubs sklearn-stubs sqlalchemy sympy-stubs transformers-stubs
do
    cp -R ../../$d stubs
done

