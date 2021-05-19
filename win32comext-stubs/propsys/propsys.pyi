# Python: 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)]
# Library: win32comext, version: unspecified
# Module: win32comext.propsys.propsys, version: unspecified

'A module, encapsulating the Property System interfaces.Available on Windows Vista and later, but can also be usedon XP if Desktop Search 3 is installed.'

import typing
import builtins as _mod_builtins
import win32.lib.pywintypes as _mod_pywintypes

_PyIID = _mod_pywintypes.IID

IID_IInitializeWithFile: _PyIID
IID_IInitializeWithStream: _PyIID
IID_INamedPropertyStore: _PyIID
IID_IObjectWithPropertyKey: _PyIID
IID_IPersistSerializedPropStorage: _PyIID
IID_IPropertyChange: _PyIID
IID_IPropertyChangeArray: _PyIID
IID_IPropertyDescription: _PyIID
IID_IPropertyDescriptionAliasInfo: _PyIID
IID_IPropertyDescriptionList: _PyIID
IID_IPropertyDescriptionSearchInfo: _PyIID
IID_IPropertyEnumType: _PyIID
IID_IPropertyEnumTypeList: _PyIID
IID_IPropertyStore: _PyIID
IID_IPropertyStoreCache: _PyIID
IID_IPropertyStoreCapabilities: _PyIID
IID_IPropertySystem: _PyIID
PROPVARIANTType = _mod_builtins.PyPROPVARIANT
def PSCreateMemoryPropertyStore() -> typing.Any:
    ...

def PSCreatePropertyChangeArray() -> typing.Any:
    ...

def PSCreatePropertyStoreFromPropertySetStorage() -> typing.Any:
    ...

def PSCreateSimplePropertyChange() -> typing.Any:
    ...

def PSGetItemPropertyHandler() -> typing.Any:
    ...

def PSGetNameFromPropertyKey() -> typing.Any:
    ...

def PSGetNamedPropertyFromPropertyStorage() -> typing.Any:
    ...

def PSGetPropertyDescription() -> typing.Any:
    ...

def PSGetPropertyFromPropertyStorage() -> typing.Any:
    ...

def PSGetPropertyKeyFromName() -> typing.Any:
    ...

def PSGetPropertySystem() -> typing.Any:
    ...

def PSLookupPropertyHandlerCLSID() -> typing.Any:
    ...

def PSRegisterPropertySchema() -> typing.Any:
    ...

def PSUnregisterPropertySchema() -> typing.Any:
    ...

def SHGetPropertyStoreForWindow() -> typing.Any:
    ...

def SHGetPropertyStoreFromParsingName() -> typing.Any:
    ...

def SHSetDefaultProperties() -> typing.Any:
    ...

def StgDeserializePropVariant() -> typing.Any:
    ...

def StgSerializePropVariant() -> typing.Any:
    ...

__doc__: str
__file__: str
__name__: str
__package__: str
error = _mod_pywintypes.com_error
def __getattr__(name) -> typing.Any:
    ...

