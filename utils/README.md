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

## SymPy partial-stub retirement

`compare_sympy_typing.py` compares the partial SymPy `.pyi` files with an installed
SymPy release without importing the modules:

```shell
python utils/compare_sympy_typing.py \
  --sympy-root "$(python -c 'import sympy; print(sympy.__path__[0])')" \
  --json-out artifacts/sympy-typing.json \
  --markdown-out artifacts/sympy-typing.md
```

A file is a candidate only if every material function, async function, property,
class member, and explicitly annotated module attribute has a same-named,
same-kind source declaration. Functions and properties must annotate every
non-`self`/`cls` parameter (including variadics) and their return. Classes are
structural declarations; their explicit members are checked independently.
Imports, `__getattr__`, missing source modules, and declaration-kind mismatches
are conservatively retained. This deliberately does not assert semantic type
equivalence from matching names alone. `--check` makes candidates fail CI;
ordinary reports exit successfully when stubs still need to be retained.

The monthly **SymPy stub retirement** workflow uploads both reports and runs
`python utils/run_sympy_analysis_smoke.py --max-seconds 60`. The 60-second
threshold is deliberately generous: it detects gross analyzer regressions, not
small timing changes. It never
automatically removes `core/evalf.pyi`, `core/power.pyi`, `simplify/powsimp.pyi`,
or `simplify/simplify.pyi`, which were performance workarounds. To assess those,
run the smoke command with and without the relevant stub and compare its reported
elapsed time manually; timing is intentionally not an automatic deletion gate.
Add another relative `.pyi` path to
`PROTECTED_FILES` when a stub has value structural comparison cannot detect.
