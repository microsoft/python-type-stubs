pip install --upgrade pyright
pip install -r requirements.txt
robocopy /E ..\partial ..\typings *
pyright --lib --pythonversion 3.11 -p ../pyrighttestconfig.json .



