#!/bin/sh

python -m pip install --upgrade pandas
mkdir -p stubs
for d in cv2-stubs django gym-stubs jmespath matplotlib openpyxl pandas pythonwin-stubs scipy-stubs sklearn-stubs sqlalchemy sympy-stubs transformers-stubs win32-stubs win32comext-stubs
do
    cp -R ../../$d stubs
done
(cd ../docify; rm -rf .eggs; PBR_VERSION=1.0.0 pip install .)
(cd stubs/pandas; docify ../../docify-pandas.cfg)




