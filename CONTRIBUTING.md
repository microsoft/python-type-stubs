# Contributing

This project welcomes contributions and suggestions. Most contributions require you to
agree to a Contributor License Agreement (CLA) declaring that you have the right to,
and actually do, grant us the rights to use your contribution. For details, visit
https://cla.microsoft.com.

When you submit a pull request, a CLA-bot will automatically determine whether you need
to provide a CLA and decorate the PR appropriately (e.g., label, comment). Simply follow the
instructions provided by the bot. You will only need to do this once across all repositories using our CLA.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/)
or contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

## Checking stub changes

Use an isolated Python environment and install the test and hygiene dependencies:

```shell
python -m pip install --group tests --group hygiene
python -m ruff check
python -m ruff format --check
python -m mypy . --python-version 3.13
python -m pyright --pythonversion 3.13
python -m pytest -q tests
python tests/run_stubtest.py
```

Select the same environment in Pyright, using `--pythonpath` if necessary. Include the
local stubs when running mypy on regression tests; checking only a test directory can
resolve installed library code instead of the stubs being changed.

CI checks Python 3.10 and 3.13 on Linux, Windows, and macOS. Run against both Python
versions when updating runtime APIs: the latest compatible library release can differ
between them. For a focused runtime check, pass package directories to the runner,
for example `python tests/run_stubtest.py vispy sklearn`.

Fix incorrect declarations before adding allowlist entries. Keep exceptions narrow
and documented, and remove entries that no longer suppress an error. Modules shipped
only in some wheels or on some platforms need optional entries rather than disabling
unused-allowlist checks globally.
