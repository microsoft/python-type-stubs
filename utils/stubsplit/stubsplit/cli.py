"""
StubSplit.

Usage:
  stubsplit (split|merge) [--verbose] <stubpath> <docpath>
  stubsplit -h | --help
  stubsplit --version

Options:
  -h --help     Show this screen.
  --version     Show version.
"""
import os
from docopt import docopt
import stubsplit


def main():
    arguments = docopt(__doc__, version='Stubsplit 0.1')
    docpath = arguments['<docpath>']
    stubpath = arguments['<stubpath>']
    verbose = arguments['--verbose']
    if arguments['split']:
        # Walk the stub tree and call split for each .pyi file
        for root, _, files in os.walk(stubpath):
            for name in files:
                if not name.endswith('.pyi'):
                    continue
                relpath = root[len(stubpath)+1:]
                stubsplit.split(root, os.path.join(docpath, relpath), name, verbose)
    else:
        # Walk the doc tree and call combine for each .ds file
        for root, _, files in os.walk(docpath):
            for name in files:
                if not name.endswith('.ds'):
                    continue
                relpath = root[len(docpath)+1:]
                stubsplit.combine(os.path.join(stubpath, relpath), root, name[:-3], verbose)


if __name__ == '__main__':
    main()
