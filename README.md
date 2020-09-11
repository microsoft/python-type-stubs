# Python Type Stubs

# Python Type Stubs

## Introduction

As the Python team, we are helping to ensure that packages have high-quality type annotations.
In cases where this must be done through type stubs, we are contributing stubs to
[typeshed](https://github.com/python/typeshed). This repository contains our “work in progress”.
Once the stubs for a package meet the requirements of typeshed, we will contribute them to
typeshed and delete them from this repository.

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

# Contributing

This project welcomes contributions and suggestions.  Most contributions require you to agree to a
Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us
the rights to use your contribution. For details, visit https://cla.opensource.microsoft.com.

When you submit a pull request, a CLA bot will automatically determine whether you need to provide
a CLA and decorate the PR appropriately (e.g., status check, comment). Simply follow the instructions
provided by the bot. You will only need to do this once across all repos using our CLA.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or
contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.
