# Python: 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)]
# Library: win32comext, version: unspecified
# Module: win32comext.adsi.adsi, version: unspecified

''

import typing
import builtins as _mod_builtins
import win32.lib.pywintypes as _mod_pywintypes

_PyIID = _mod_pywintypes.IID

def ADsBuildEnumerator() -> typing.Any:
    ...

def ADsEnumerateNext() -> typing.Any:
    ...

def ADsGetLastError() -> typing.Any:
    ...

def ADsGetObject() -> typing.Any:
    ...

def ADsOpenObject() -> typing.Any:
    ...

CLSID_ADsDSOObject: _PyIID
CLSID_AccessControlEntry: _PyIID
CLSID_AccessControlList: _PyIID
CLSID_DsObjectPicker: _PyIID
CLSID_SecurityDescriptor: _PyIID
DBGUID_LDAPDialect: _PyIID
DBPROPSET_ADSISEARCH: _PyIID
DSOP_SCOPE_INIT_INFOs = _mod_builtins.PyDSOP_SCOPE_INIT_INFOs
IID_IADs: _PyIID
IID_IADsClass: _PyIID
IID_IADsCollection: _PyIID
IID_IADsComputer: _PyIID
IID_IADsComputerOperations: _PyIID
IID_IADsContainer: _PyIID
IID_IADsDeleteOps: _PyIID
IID_IADsDomain: _PyIID
IID_IADsFileService: _PyIID
IID_IADsFileServiceOperations: _PyIID
IID_IADsFileShare: _PyIID
IID_IADsGroup: _PyIID
IID_IADsLocality: _PyIID
IID_IADsMembers: _PyIID
IID_IADsNamespaces: _PyIID
IID_IADsO: _PyIID
IID_IADsOU: _PyIID
IID_IADsOpenDSObject: _PyIID
IID_IADsPrintJob: PyIID
IID_IADsPrintJobOperations: PyIID
IID_IADsPrintQueue: _PyIID
IID_IADsPrintQueueOperations: _PyIID
IID_IADsProperty: _PyIID
IID_IADsPropertyList: _PyIID
IID_IADsResource: _PyIID
IID_IADsSearch: _PyIID
IID_IADsService: _PyIID
IID_IADsServiceOperations: _PyIID
IID_IADsSession: _PyIID
IID_IADsSyntax: _PyIID
IID_IADsUser: _PyIID
IID_IDirectoryObject: _PyIID
IID_IDirectorySearch: _PyIID
IID_IDsObjectPicker: _PyIID
LIBID_ADs: _PyIID
def StringAsDS_SELECTION_LIST() -> typing.Any:
    ...

__doc__: str
__file__: str
__name__: str
__package__: str
error = _mod_pywintypes.com_error
def __getattr__(name) -> typing.Any:
    ...

