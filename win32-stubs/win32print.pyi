# Python: 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)]
# Library: win32print, version: unspecified
# Module: win32print, version: unspecified

'A module encapsulating the Windows printing API.'

import typing
import builtins as _mod_builtins

def AbortDoc() -> typing.Any:
    ...

def AbortPrinter() -> typing.Any:
    ...

def AddForm() -> typing.Any:
    ...

def AddJob() -> typing.Any:
    ...

def AddPrinter() -> typing.Any:
    ...

def AddPrinterConnection() -> typing.Any:
    ...

def ClosePrinter() -> typing.Any:
    ...

DEF_PRIORITY: int
DI_APPBANDING: int
DI_ROPS_READ_DESTINATION: int
DPD_DELETE_ALL_FILES: int
DPD_DELETE_SPECIFIC_VERSION: int
DPD_DELETE_UNUSED_FILES: int
DSPRINT_PENDING: int
DSPRINT_PUBLISH: int
DSPRINT_REPUBLISH: int
DSPRINT_UNPUBLISH: int
DSPRINT_UPDATE: int
def DeleteForm() -> typing.Any:
    ...

def DeletePrinter() -> typing.Any:
    ...

def DeletePrinterConnection() -> typing.Any:
    ...

def DeletePrinterDriver() -> typing.Any:
    ...

def DeletePrinterDriverEx() -> typing.Any:
    ...

def DeviceCapabilities() -> typing.Any:
    ...

def DocumentProperties() -> typing.Any:
    ...

def EndDoc() -> typing.Any:
    ...

def EndDocPrinter() -> typing.Any:
    ...

def EndPage() -> typing.Any:
    ...

def EndPagePrinter() -> typing.Any:
    ...

def EnumForms() -> typing.Any:
    ...

def EnumJobs() -> typing.Any:
    ...

def EnumMonitors() -> typing.Any:
    ...

def EnumPorts() -> typing.Any:
    ...

def EnumPrintProcessorDatatypes() -> typing.Any:
    ...

def EnumPrintProcessors() -> typing.Any:
    ...

def EnumPrinterDrivers() -> typing.Any:
    ...

def EnumPrinters() -> typing.Any:
    ...

FORM_BUILTIN: int
FORM_PRINTER: int
FORM_USER: int
def FlushPrinter() -> typing.Any:
    ...

def GetDefaultPrinter() -> typing.Any:
    ...

def GetDefaultPrinterW() -> typing.Any:
    ...

def GetDeviceCaps() -> typing.Any:
    ...

def GetForm() -> typing.Any:
    ...

def GetJob() -> typing.Any:
    ...

def GetPrintProcessorDirectory() -> typing.Any:
    ...

def GetPrinter() -> typing.Any:
    ...

def GetPrinterDriverDirectory() -> typing.Any:
    ...

JOB_ACCESS_ADMINISTER: int
JOB_ACCESS_READ: int
JOB_ALL_ACCESS: int
JOB_CONTROL_CANCEL: int
JOB_CONTROL_DELETE: int
JOB_CONTROL_LAST_PAGE_EJECTED: int
JOB_CONTROL_PAUSE: int
JOB_CONTROL_RESTART: int
JOB_CONTROL_RESUME: int
JOB_CONTROL_SENT_TO_PRINTER: int
JOB_EXECUTE: int
JOB_INFO_1: int
JOB_POSITION_UNSPECIFIED: int
JOB_READ: int
JOB_STATUS_BLOCKED_DEVQ: int
JOB_STATUS_COMPLETE: int
JOB_STATUS_DELETED: int
JOB_STATUS_DELETING: int
JOB_STATUS_ERROR: int
JOB_STATUS_OFFLINE: int
JOB_STATUS_PAPEROUT: int
JOB_STATUS_PAUSED: int
JOB_STATUS_PRINTED: int
JOB_STATUS_PRINTING: int
JOB_STATUS_RESTART: int
JOB_STATUS_SPOOLING: int
JOB_STATUS_USER_INTERVENTION: int
JOB_WRITE: int
MAX_PRIORITY: int
MIN_PRIORITY: int
def OpenPrinter() -> typing.Any:
    ...

PORT_STATUS_DOOR_OPEN: int
PORT_STATUS_NO_TONER: int
PORT_STATUS_OFFLINE: int
PORT_STATUS_OUTPUT_BIN_FULL: int
PORT_STATUS_OUT_OF_MEMORY: int
PORT_STATUS_PAPER_JAM: int
PORT_STATUS_PAPER_OUT: int
PORT_STATUS_PAPER_PROBLEM: int
PORT_STATUS_POWER_SAVE: int
PORT_STATUS_TONER_LOW: int
PORT_STATUS_TYPE_ERROR: int
PORT_STATUS_TYPE_INFO: int
PORT_STATUS_TYPE_WARNING: int
PORT_STATUS_USER_INTERVENTION: int
PORT_STATUS_WARMING_UP: int
PORT_TYPE_NET_ATTACHED: int
PORT_TYPE_READ: int
PORT_TYPE_REDIRECTED: int
PORT_TYPE_WRITE: int
PRINTER_ACCESS_ADMINISTER: int
PRINTER_ACCESS_USE: int
PRINTER_ALL_ACCESS: int
PRINTER_ATTRIBUTE_DEFAULT: int
PRINTER_ATTRIBUTE_DIRECT: int
PRINTER_ATTRIBUTE_DO_COMPLETE_FIRST: int
PRINTER_ATTRIBUTE_ENABLE_BIDI: int
PRINTER_ATTRIBUTE_ENABLE_DEVQ: int
PRINTER_ATTRIBUTE_FAX: int
PRINTER_ATTRIBUTE_HIDDEN: int
PRINTER_ATTRIBUTE_KEEPPRINTEDJOBS: int
PRINTER_ATTRIBUTE_LOCAL: int
PRINTER_ATTRIBUTE_NETWORK: int
PRINTER_ATTRIBUTE_PUBLISHED: int
PRINTER_ATTRIBUTE_QUEUED: int
PRINTER_ATTRIBUTE_RAW_ONLY: int
PRINTER_ATTRIBUTE_SHARED: int
PRINTER_ATTRIBUTE_TS: int
PRINTER_ATTRIBUTE_WORK_OFFLINE: int
PRINTER_CONTROL_PAUSE: int
PRINTER_CONTROL_PURGE: int
PRINTER_CONTROL_RESUME: int
PRINTER_CONTROL_SET_STATUS: int
PRINTER_ENUM_CONNECTIONS: int
PRINTER_ENUM_CONTAINER: int
PRINTER_ENUM_DEFAULT: int
PRINTER_ENUM_EXPAND: int
PRINTER_ENUM_ICON1: int
PRINTER_ENUM_ICON2: int
PRINTER_ENUM_ICON3: int
PRINTER_ENUM_ICON4: int
PRINTER_ENUM_ICON5: int
PRINTER_ENUM_ICON6: int
PRINTER_ENUM_ICON7: int
PRINTER_ENUM_ICON8: int
PRINTER_ENUM_LOCAL: int
PRINTER_ENUM_NAME: int
PRINTER_ENUM_NETWORK: int
PRINTER_ENUM_REMOTE: int
PRINTER_ENUM_SHARED: int
PRINTER_EXECUTE: int
PRINTER_INFO_1: int
PRINTER_READ: int
PRINTER_STATUS_BUSY: int
PRINTER_STATUS_DOOR_OPEN: int
PRINTER_STATUS_ERROR: int
PRINTER_STATUS_INITIALIZING: int
PRINTER_STATUS_IO_ACTIVE: int
PRINTER_STATUS_MANUAL_FEED: int
PRINTER_STATUS_NOT_AVAILABLE: int
PRINTER_STATUS_NO_TONER: int
PRINTER_STATUS_OFFLINE: int
PRINTER_STATUS_OUTPUT_BIN_FULL: int
PRINTER_STATUS_OUT_OF_MEMORY: int
PRINTER_STATUS_PAGE_PUNT: int
PRINTER_STATUS_PAPER_JAM: int
PRINTER_STATUS_PAPER_OUT: int
PRINTER_STATUS_PAPER_PROBLEM: int
PRINTER_STATUS_PAUSED: int
PRINTER_STATUS_PENDING_DELETION: int
PRINTER_STATUS_POWER_SAVE: int
PRINTER_STATUS_PRINTING: int
PRINTER_STATUS_PROCESSING: int
PRINTER_STATUS_SERVER_UNKNOWN: int
PRINTER_STATUS_TONER_LOW: int
PRINTER_STATUS_USER_INTERVENTION: int
PRINTER_STATUS_WAITING: int
PRINTER_STATUS_WARMING_UP: int
PRINTER_WRITE: int
SERVER_ACCESS_ADMINISTER: int
SERVER_ACCESS_ENUMERATE: int
SERVER_ALL_ACCESS: int
SERVER_EXECUTE: int
SERVER_READ: int
SERVER_WRITE: int
def ScheduleJob() -> typing.Any:
    ...

def SetDefaultPrinter() -> typing.Any:
    ...

def SetDefaultPrinterW() -> typing.Any:
    ...

def SetForm() -> typing.Any:
    ...

def SetJob() -> typing.Any:
    ...

def SetPrinter() -> typing.Any:
    ...

def StartDoc() -> typing.Any:
    ...

def StartDocPrinter() -> typing.Any:
    ...

def StartPage() -> typing.Any:
    ...

def StartPagePrinter() -> typing.Any:
    ...

def WritePrinter() -> typing.Any:
    ...

__doc__: str
__file__: str
__name__: str
__package__: str
def __getattr__(name) -> typing.Any:
    ...

