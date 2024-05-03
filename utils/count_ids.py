#!/bin/python

"""Count IDs.

Usage:
  count_ids [--path=<root>] [--suffix=<filesuffix>] [--pat=<pat>] [--uniq]
  count_ids -h | --help
  count_ids --version

Options:
  -h --help               Show this screen.
  --version               Show version.
  --path=<root>           Directory to scan (default is current working directory)
  --suffix=<filesuffix>   File name suffix to restrict to (default is all files)
  --pat=<pat>             A regular expression to use to extract IDs
  --uniq                  Only output IDs that occur once only (with their context)
"""

import glob
import os
import re

import docopt


def count(root, suffix, regex, uniq):
    if root is None:
        root = "."
    filepat = "*" if suffix is None else "*." + suffix[suffix.find(".") + 1 :]
    if regex is None:
        regex = "[A-Za-z_][A-Za-z0-9_]*"
    data = {}
    loc = {}
    ctx = {}
    try:
        prog = re.compile(regex)
    except Exception as e:
        print(f"Invalid regex {regex}: {e}")
        return
    pathpat = root + "/**/" + filepat
    for name in glob.iglob(pathpat, recursive=True):
        n = 0
        if os.path.isdir(name):
            continue
        try:
            with open(name) as f:
                for line in f:
                    n += 1
                    for id in prog.findall(line):
                        if id in data:
                            data[id] += 1
                            if id in loc:
                                del loc[id]  # save some memory
                                del ctx[id]
                        else:
                            data[id] = 1
                            loc[id] = f"{name}:{n}"
                            ctx[id] = line[:-1]
        except Exception as e:
            print(f"Couldn't process file {name}: {e}")

    if uniq:
        for id, lc in loc.items():
            print(f"{id}: {lc}: {ctx[id]}")
    else:
        for id, count in data.items():
            print(f"{id}: {count}")


if __name__ == "__main__":
    args = docopt.docopt(__doc__, version="Count IDs 0.1")
    count(root=args["--path"], suffix=args["--suffix"], regex=args["--pat"], uniq=args["--uniq"])
