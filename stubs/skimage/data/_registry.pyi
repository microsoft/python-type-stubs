import sys

if sys.version_info < (3, 11):
    legacy_datasets: list[str]
    legacy_registry: dict[str, str]

# Registry of datafiles that can be downloaded along with their SHA256 hashes
# To generate the SHA256 hash, use the command
# openssl sha256 filename
registry: dict = ...

registry_urls: dict = ...
