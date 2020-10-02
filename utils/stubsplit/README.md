stubsplit is a utility that can remove docstrings from Python type stub files, or
merge docstrings back in. We use this because we sometimes want to put docstrings for
functions into the stubs, because it is hard to extract them from source. This is 
primarily used for some pandas APIs for now.

Usage:
  stubsplit (split|merge) [--verbose] <stubpath> <docpath>
  stubsplit -h | --help
  stubsplit --version


TODO:
- handle folded lines
- handle nested classes
- implement merge
- test against pandas stubs for hermeticity

