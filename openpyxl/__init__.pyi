# Copyright (c) 2010-2020 openpyxl

from openpyxl.compat.numbers import NUMPY as NUMPY
from openpyxl.xml import DEFUSEDXML as DEFUSEDXML, LXML as LXML
from openpyxl.workbook import Workbook as Workbook
from openpyxl.reader.excel import load_workbook as open
from openpyxl.reader.excel import load_workbook as load_workbook
import openpyxl._constants as constants

# Expose constants especially the version number

__author__ = constants.__author__
__author_email__ = constants.__author_email__
__license__ = constants.__license__
__maintainer_email__ = constants.__maintainer_email__
__url__ = constants.__url__
__version__ = constants.__version__
