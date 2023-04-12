pip install --upgrade pyright
pip install -r requirements.txt
pyright --lib --pythonversion 3.11 -p ../pyrighttestconfig.json .
