pip install --upgrade pyright
pip install -r requirements.txt

cd ../
isort .
black .
pyright --pythonversion 3.11 -p pyrighttestconfig.json .
