pip install --upgrade pyright
pip install -r requirements.txt

cd ../
pyright --pythonversion 3.11 -p pyrighttestconfig.json .
