#!/bin/sh

python -m pip install --upgrade pandas
python -m pip install --upgrade pyright
python -m pip install --upgrade docopt

mkdir -p stubs

# Generate pandas stubs with pyright and copy them over

#pyright --createstub pandas
#cp -R ../../typings/pandas stubs

# Copy over the stubs from here, including partial stubs for pandas

for d in cv2-stubs django gym-stubs jmespath matplotlib openpyxl pythonwin-stubs scipy-stubs sklearn-stubs sqlalchemy sympy-stubs transformers-stubs win32-stubs win32comext-stubs
do
    cp -R ../../$d stubs
done
cp -R ../../partial/pandas stubs

# Install docify and patch the pandas stubs with docstrings

(cd ../docify; flit install)
(cd stubs/pandas; docify --verbose --inject ../../docify-pandas.cfg)
-mkdir -p docs
docify --verbose docify-pandas.cfg docs




