# Python: 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)]
# Library: win32comext, version: unspecified
# Module: win32comext.axcontrol.axcontrol, version: unspecified

'A module, encapsulating the ActiveX Control interfaces.'

import typing
import builtins as _mod_builtins
import win32.lib.pywintypes as _mod_pywintypes

_PyIID = _mod_pywintypes.IID

EMBDHLP_CREATENOW: int
EMBDHLP_DELAYCREATE: int
EMBDHLP_INPROC_HANDLER: int
EMBDHLP_INPROC_SERVER: int
IID_IObjectWithSite: _PyIID
IID_IOleClientSite: _PyIID
IID_IOleCommandTarget: _PyIID
IID_IOleControl: _PyIID
IID_IOleControlSite: _PyIID
IID_IOleInPlaceActiveObject: _PyIID
IID_IOleInPlaceFrame: _PyIID
IID_IOleInPlaceObject: _PyIID
IID_IOleInPlaceSite: _PyIID
IID_IOleInPlaceSiteEx: _PyIID
IID_IOleInPlaceSiteWindowless: _PyIID
IID_IOleInPlaceUIWindow: _PyIID
IID_IOleLink: _PyIID
IID_IOleObject: _PyIID
IID_ISpecifyPropertyPages: _PyIID
IID_IViewObject: _PyIID
IID_IViewObject2: _PyIID
OLECLOSE_NOSAVE: int
OLECLOSE_PROMPTSAVE: int
OLECLOSE_SAVEIFDIRTY: int
OLECMDF_ENABLED: int
OLECMDF_LATCHED: int
OLECMDF_NINCHED: int
OLECMDF_SUPPORTED: int
OLECMDTEXTF_NAME: int
OLECMDTEXTF_NONE: int
OLECMDTEXTF_STATUS: int
OLECREATE_LEAVERUNNING: int
OLEIVERB_DISCARDUNDOSTATE: int
OLEIVERB_HIDE: int
OLEIVERB_INPLACEACTIVATE: int
OLEIVERB_OPEN: int
OLEIVERB_PRIMARY: int
OLEIVERB_SHOW: int
OLEIVERB_UIACTIVATE: int
def OleCreate() -> typing.Any:
    ...

def OleLoadPicture() -> typing.Any:
    ...

def OleLoadPicturePath() -> typing.Any:
    ...

def OleSetContainedObject() -> typing.Any:
    ...

def OleTranslateAccelerator() -> typing.Any:
    ...

__doc__: str
__file__: str
__name__: str
__package__: str
def __getattr__(name) -> typing.Any:
    ...

