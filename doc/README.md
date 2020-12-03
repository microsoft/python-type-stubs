This directory contains docstrings that we inline into type stubs before bundling the stubs in Pylance. This is only for cases where Pylance cannot otherwise locate the docstrings based on its own heuristics (perhaps because the docstrings are programmatically generated). The stubsplit.py utility in the utils folder is used for merging or splitting such docstrings into or out of stub files.

