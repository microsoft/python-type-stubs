"""
Docify.

Usage:
  docify [--verbose] <configfile> [--inject] [<outpath>]
  docify -h | --help
  docify --version

Options:
  --inject      Inject docs into stubs (else write them out to .pyi.d files)
  --verbose     Print out details of what docify is doing.
  -h --help     Show this screen.
  --version     Show version.

If outpath is not specified the current working directory 
will be assumed. It should be the path where the stubs are
(if injecting) or where the docs should be saved.

The config file is a CSV file that has lines of the form:

    package,stub_file_path,classname,methodname

If classname is empty, methodname is a top-level function name.
The stub_file_path paths should be relative to outpath.

The stub file specified by stub_file_path will be patched with 
the docstring of classname.methodname, which will be extracted
by introspection from the specified package.

For example:

    pandas,core/series.pyi,Series,groupby

"""
import csv
import importlib
import inspect
import os
import sys
from docopt import docopt
from .docify import docify, writedoc


__version__ = "0.1"


def main():
    arguments = docopt(__doc__, version='docify 0.1')
    configfile = arguments['<configfile>']
    outpath = arguments['<outpath>']
    if outpath is None:
        outpath = '.'
    verbose = arguments['--verbose']
    inject = arguments['--inject']
    with open(configfile) as f:
        patches = csv.reader(f)

        for patch in patches:
            if not patch:
                break
            pkg, stub, class_, method = patch
            try:
                if pkg in sys.modules:
                    package = sys.modules[pkg]
                else:
                    package = importlib.import_module(pkg)

                obj = package

                for path in stub.split('/'):
                    obj = obj.__dict__[path]
            
                if class_:
                    obj = obj.__dict__[class_]
                obj = obj.__dict__[method]
                doc = inspect.getdoc(obj)

            except Exception as e:
                if class_ is None:
                    print(f'Could not get docstring for {pkg}.{method}: {e}')
                else:
                    print(f'Could not get docstring for {pkg}.{class_}.{method}: {e}')
                sys.exit(-1)
    
            if not doc:
                if class_ is None:
                    print(f'{pkg}.{method} has no docstring')
                else:
                    print(f'{pkg}.{class_}.{method} has no docstring')
                sys.exit(-1)
        
            #try:
            if True:
                path = os.path.join(outpath, stub)
                if inject:
                    docify(path, class_, method, doc, verbose)
                else:
                    writedoc(path, class_, method, doc, verbose)
            #except Exception as e:
            #    print(e)
            #    sys.exit(-1)


