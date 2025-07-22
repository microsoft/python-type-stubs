# Python Type Stubs

## Introduction

As the Python team, we are helping to ensure that packages have high-quality type annotations.
In cases where this must be done through type stubs, we are contributing stubs to
[typeshed](https://github.com/python/typeshed). This repository contains our “work in progress”.
Once the stubs for a package meet the requirements of typeshed, we will contribute them to
typeshed and delete them from this repository. We also support partial stubs in our tooling
in which case the stubs may never graduate from here, but we want to share them publicly so
that others can contribute to or make use of what coverage we have.

## Our Use of Type Stubs

Microsoft's Python Language Server [Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance)
uses type information to implement useful features like autocompletion and type checking.
For best results, type annotations must be provided for functions, methods and variables.

There are two ways type annotations can be provided — through [inline type annotations](https://www.python.org/dev/peps/pep-0484/#type-definition-syntax)
and through [`.pyi` type stub files](https://www.python.org/dev/peps/pep-0484/#stub-files),
which may be bundled with the package or installed separately from some other source such as typeshed or PyPI.
_We believe that the best approach for package authors is to have explicit inline type annotations
that accurately and completely describe their public interface contract. This allows tools to validate
the types for the package authors themselves and reduces the maintenance burden of keeping two separate
API definitions in sync. In cases where inline type annotations are not possible (e.g. for compiled
libraries), packages should include stub files that describe those portions of the interface._

We recognize that there may be cases where type stubs are more appropriate, such as:

- Package authors who do not want to include type annotations, and
- Large, complex packages where adding type annotations can take time, and stubs may be an appropriate intermediate step.

## Installing our stubs

Whilst these stubs come bundled with Pylance, we recognize it can be beneficial to install them
so that type-checkers such as [Pyright](https://github.com/microsoft/pyright) and [mypy](https://github.com/python/mypy) pick up on them.  
The stubs are not currently published on PyPI, but you can install them all at once with:

```shell
pip install git+https://github.com/microsoft/python-type-stubs.git 
```

## Upstreamed libraries

Stubs for the following libraries now exist in typeshed or the libraries themselves and are no longer maintained here:

- aiofiles
- cachetools
- deprecated
- django (see <https://github.com/sbdchd/django-types>)
- filelock
- freezegun
- jmespath
- markdown
- netaddr
- networkx
- openpyxl
- opencv-python (see <https://github.com/opencv/opencv>; please upgrade opencv-python to 4.8.0+ and file any issues there)
- packaging
- pandas (see <https://github.com/pandas-dev/pandas-stubs>; please open pandas stub issues there)
- pendulum
- PIL
- pygame
- pywin32 (pythonwin, win32 and win32com packages)
- retry
- scipy (see <https://github.com/jorenham/scipy-stubs>)
- slugify
- SQLAlchemy (see <https://pypi.org/project/types-SQLAlchemy/> for SQLAlchemy 1.4; 2.0.0 and above include type annotations)
- tenacity

The following libraries are `py.typed`. We still have stubs for them here, but we are no longer actively maintaining them. We continue to bundle them with Pylance so users on older, non-`py.typed` versions will still get type info. If you find problems in our stubs for these libraries, rather than filing an issue here, you should upgrade to the version shown below to get the official stubs:

- matplotlib (3.8.0)

# Trademarks

This project may contain trademarks or logos for projects, products, or services. Authorized use of Microsoft trademarks or logos is subject to and must follow Microsoft's Trademark & Brand Guidelines. Use of Microsoft trademarks or logos in modified versions of this project must not cause confusion or imply Microsoft sponsorship. Any use of third-party trademarks or logos are subject to those third-party's policies.
