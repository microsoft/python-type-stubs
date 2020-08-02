import logging
from .extensions import Extension
from typing import Any, BinaryIO, Dict, IO, List, Mapping, Optional, Sequence, Text, TextIO, Union

from typing_extensions import Literal

"""
Python Markdown

A Python implementation of John Gruber's Markdown.

Documentation: https://python-markdown.github.io/
GitHub: https://github.com/Python-Markdown/markdown/
PyPI: https://pypi.org/project/Markdown/

Started by Manfred Stienstra (http://www.dwerg.net/).
Maintained for a few years by Yuri Takhteyev (http://www.freewisdom.org).
Currently maintained by Waylan Limberg (https://github.com/waylan),
Dmitry Shachnev (https://github.com/mitya57) and Isaac Muse (https://github.com/facelessuser).

Copyright 2007-2018 The Python Markdown Project (v. 1.7 and later)
Copyright 2004, 2005, 2006 Yuri Takhteyev (v. 0.2-1.6b)
Copyright 2004 Manfred Stienstra (the original version)

License: BSD (see LICENSE.md for details).
"""
__all__ = ["Markdown", "markdown", "markdownFromFile"]
logger = logging.getLogger("MARKDOWN")

class Markdown:
    """Convert Markdown to HTML."""

    doc_tag = ...
    output_formats = ...
    def __init__(
        self,
        extensions: Optional[Sequence[Union[str, Extension]]] = ...,
        extension_configs: Optional[Mapping[str, Mapping[str, str]]] = ...,
        output_format: Optional[Literal["xhtml", "html"]] = ...,
        tab_length: Optional[int] = ...,
    ) -> None:
        """
        Creates a new Markdown instance.

        Keyword arguments:

        * extensions: A list of extensions.
            If an item is an instance of a subclass of `markdown.extension.Extension`, the  instance will be used
            as-is. If an item is of type string, first an entry point will be loaded. If that fails, the string is
            assumed to use Python dot notation (`path.to.module:ClassName`) to load a markdown.Extension subclass. If
            no class is specified, then a `makeExtension` function is called within the specified module.
        * extension_configs: Configuration settings for extensions.
        * output_format: Format of output. Supported formats are:
            * "xhtml": Outputs XHTML style tags. Default.
            * "html": Outputs HTML style tags.
        * tab_length: Length of tabs in the source. Default: 4

        """
        ...
    def build_parser(self) -> Markdown:
        """ Build the parser from the various parts. """
        ...
    def registerExtensions(
        self, extensions: Sequence[Union[Extension, str]], configs: Mapping[str, Mapping[str, str]]
    ) -> Markdown:
        """
        Register extensions with this instance of Markdown.

        Keyword arguments:

        * extensions: A list of extensions, which can either
           be strings or objects.
        * configs: A dictionary mapping extension names to config options.

        """
        ...
    def build_extension(self, ext_name: Text, configs: Mapping[str, str]) -> Extension:
        """
        Build extension from a string name, then return an instance.

        First attempt to load an entry point. The string name must be registered as an entry point in the
        `markdown.extensions` group which points to a subclass of the `markdown.extensions.Extension` class.
        If multiple distributions have registered the same name, the first one found is returned.

        If no entry point is found, assume dot notation (`path.to.module:ClassName`). Load the specified class and
        return an instance. If no class is specified, import the module and call a `makeExtension` function and return
        the Extension instance returned by that function.
        """
        ...
    def registerExtension(self, extension: Extension) -> Markdown:
        """ This gets called by the extension """
        ...
    def reset(self: Markdown) -> Markdown:
        """
        Resets all state variables so that we can start with a new text.
        """
        ...
    def set_output_format(self, format: Literal["xhtml", "html"]) -> Markdown:
        """ Set the output format for the class instance. """
        ...
    def is_block_level(self, tag: str) -> bool:
        """Check if the tag is a block level HTML tag."""
        ...
    def convert(self, source: Text) -> Text:
        """
        Convert markdown to serialized XHTML or HTML.

        Keyword arguments:

        * source: Source text as a Unicode string.

        Markdown processing takes place in five steps:

        1. A bunch of "preprocessors" munge the input text.
        2. BlockParser() parses the high-level structural elements of the
           pre-processed text into an ElementTree.
        3. A bunch of "treeprocessors" are run against the ElementTree. One
           such treeprocessor runs InlinePatterns against the ElementTree,
           detecting inline markup.
        4. Some post-processors are run against the text after the ElementTree
           has been serialized into text.
        5. The output is written to a string.

        """
        ...
    def convertFile(
        self,
        input: Optional[Union[str, TextIO, BinaryIO]] = ...,
        output: Optional[Union[str, TextIO, BinaryIO]] = ...,
        encoding: Optional[str] = ...,
    ) -> Markdown:
        """Converts a markdown file and returns the HTML as a unicode string.

        Decodes the file using the provided encoding (defaults to utf-8),
        passes the file content to markdown, and outputs the html to either
        the provided stream or the file with provided name, using the same
        encoding as the source file. The 'xmlcharrefreplace' error handler is
        used when encoding the output.

        **Note:** This is the only place that decoding and encoding of unicode
        takes place in Python-Markdown.  (All other code is unicode-in /
        unicode-out.)

        Keyword arguments:

        * input: File object or path. Reads from stdin if `None`.
        * output: File object or path. Writes to stdout if `None`.
        * encoding: Encoding of input and output files. Defaults to utf-8.

        """
        ...

def markdown(
    text: Text,
    extensions: Optional[Sequence[Union[str, Extension]]] = ...,
    extension_configs: Optional[Mapping[str, Mapping[str, str]]] = ...,
    output_format: Optional[Literal["xhtml", "html"]] = ...,
    tab_length: Optional[int] = ...,
) -> Text:
    """Convert a markdown string to HTML and return HTML as a unicode string.

    This is a shortcut function for `Markdown` class to cover the most
    basic use case.  It initializes an instance of Markdown, loads the
    necessary extensions and runs the parser on the given text.

    Keyword arguments:

    * text: Markdown formatted text as Unicode or ASCII string.
    * Any arguments accepted by the Markdown class.

    Returns: An HTML document as a string.

    """
    ...

def markdownFromFile(
    input: Optional[Union[str, TextIO, BinaryIO]] = ...,
    output: Optional[Union[str, TextIO, BinaryIO]] = ...,
    encoding: Optional[str] = ...,
    extensions: Optional[Sequence[Union[str, Extension]]] = ...,
    extension_configs: Optional[Mapping[str, Mapping[str, str]]] = ...,
    output_format: Optional[Literal["xhtml", "html"]] = ...,
    tab_length: Optional[int] = ...,
) -> None:
    """Read markdown code from a file and write it to a file or a stream.

    This is a shortcut function which initializes an instance of Markdown,
    and calls the convertFile method rather than convert.

    Keyword arguments:

    * input: a file name or readable object.
    * output: a file name or writable object.
    * encoding: Encoding of input and output.
    * Any arguments accepted by the Markdown class.

    """
    ...

