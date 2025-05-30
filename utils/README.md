# Useful Utilities

This folder contains scripts that may be useful when creating stubs.

- `count_ids.py` will count the occurrence of identifiers across a set of files. With --uniq it will out the IDs that occurred
  once only, including their location and context. This can be useful to find classes and functions in the stubs that are
  defined but never referenced, in cases where all top-level imports of functions/classes are explicit (i.e. where the
  imports are not of the form "import module as m" but of the form "from module import class as c, function as f").
- `remove_private_re_exports.py` applies Ruff's
  [useless-import-alias (PLC0414)](https://docs.astral.sh/ruff/rules/useless-import-alias/#useless-import-alias-plc0414)
  \+ [unused-import (F401)](https://docs.astral.sh/ruff/rules/unused-import/) on stubs files.
  Normally `useless-import-alias` only applies to `.py`. So this is achieved by temporarily renaming all private module type stubs.
  
You can run a script with --help for more detailed argument help.
