
import pytest


# Passes the main worker's random seeds to workers
class XDistHooks:
    def pytest_configure_node(self, node) -> None: ...


def pytest_configure(config) -> None: ...
def pytest_report_header(config) -> list[str]|None: ...
