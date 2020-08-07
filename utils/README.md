# Useful Utilities

This folder contains a couple of scripts that may be useful when creating stubs.

- count_ids.py will count the occurrence of identifiers across a set of files. With --uniq it will out the IDs that occurred 
  once only, including their location and context. This can be useful to find classes and functions in the stubs that are
  defined but never referenced, in cases where all top-level imports of functions/classes are explicit (i.e. where the 
  imports are not of the form "import module as m" but of the form "from module import class as c, function as f").
- validate_stubs.py is a basic stub validator, that looks primarily for signature mismatches and missing methods. It gathers
  information about overloads but does not use that yet. It is limited in use because it imports .pyi files as Python, and
  so is much more likely to break in the presence of circular imports, etc. But it may be worth running on your stubs. The
  easiest way to do so is to change into this directory in your copy of the repo and just use `python validate_stubs.py <packagename>`.
  It will then look in the root folder of the repo for the stub packages.
  
You can run both scripts with --help for more detailed argument help.
