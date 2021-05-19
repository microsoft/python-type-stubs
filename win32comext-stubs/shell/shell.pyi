# Python: 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)]
# Library: win32comext, version: unspecified
# Module: win32comext.shell.shell, version: unspecified

'A module wrapping Windows Shell functions and interfaces'

import typing
import builtins as _mod_builtins
import win32.lib.pywintypes as _mod_pywintypes

_PyIID = _mod_pywintypes.IID

def AddressAsPIDL() -> typing.Any:
    ...

def AssocCreate() -> typing.Any:
    ...

def AssocCreateForClasses() -> typing.Any:
    ...

BHID_AssociationArray: _PyIID
BHID_DataObject: _PyIID
BHID_EnumItems: _PyIID
BHID_Filter: _PyIID
BHID_LinkTargetItem: _PyIID
BHID_PropertyStore: _PyIID
BHID_SFObject: _PyIID
BHID_SFUIObject: _PyIID
BHID_SFViewObject: _PyIID
BHID_Storage: _PyIID
BHID_StorageEnum: _PyIID
BHID_Stream: _PyIID
BHID_ThumbnailHandler: _PyIID
BHID_Transfer: _PyIID
CGID_DefView: _PyIID
CGID_Explorer: _PyIID
CGID_ExplorerBarDoc: _PyIID
CGID_ShellDocView: _PyIID
CGID_ShellServiceObject: _PyIID
def CIDAAsString() -> typing.Any:
    ...

CLSID_ActiveDesktop: _PyIID
CLSID_ApplicationDestinations: _PyIID
CLSID_ApplicationDocumentLists: _PyIID
CLSID_ControlPanel: _PyIID
CLSID_DestinationList: _PyIID
CLSID_DragDropHelper: _PyIID
CLSID_EnumerableObjectCollection: _PyIID
CLSID_FileOperation: _PyIID
CLSID_Internet: _PyIID
CLSID_InternetShortcut: _PyIID
CLSID_KnownFolderManager: _PyIID
CLSID_MyComputer: _PyIID
CLSID_MyDocuments: _PyIID
CLSID_NetworkDomain: _PyIID
CLSID_NetworkPlaces: _PyIID
CLSID_NetworkServer: _PyIID
CLSID_NetworkShare: _PyIID
CLSID_Printers: _PyIID
CLSID_RecycleBin: _PyIID
CLSID_ShellDesktop: _PyIID
CLSID_ShellFSFolder: _PyIID
CLSID_ShellItem: _PyIID
CLSID_ShellLibrary: _PyIID
CLSID_ShellLink: _PyIID
CLSID_TaskbarList: _PyIID
def DragQueryFile() -> typing.Any:
    ...

def DragQueryFileW() -> typing.Any:
    ...

def DragQueryPoint() -> typing.Any:
    ...

EP_AdvQueryPane: _PyIID
EP_Commands: _PyIID
EP_Commands_Organize: _PyIID
EP_Commands_View: _PyIID
EP_DetailsPane: _PyIID
EP_NavPane: _PyIID
EP_PreviewPane: _PyIID
EP_QueryPane: _PyIID
def FILEGROUPDESCRIPTORAsString() -> typing.Any:
    ...

FMTID_AudioSummaryInformation: _PyIID
FMTID_Briefcase: _PyIID
FMTID_Displaced: _PyIID
FMTID_ImageProperties: _PyIID
FMTID_ImageSummaryInformation: _PyIID
FMTID_InternetSite: _PyIID
FMTID_Intshcut: _PyIID
FMTID_MediaFileSummaryInformation: _PyIID
FMTID_Misc: _PyIID
FMTID_Query: _PyIID
FMTID_ShellDetails: _PyIID
FMTID_Storage: _PyIID
FMTID_SummaryInformation: _PyIID
FMTID_Volume: _PyIID
FMTID_WebView: _PyIID
FOLDERID_AddNewPrograms: _PyIID
FOLDERID_AdminTools: _PyIID
FOLDERID_AppUpdates: _PyIID
FOLDERID_CDBurning: _PyIID
FOLDERID_ChangeRemovePrograms: _PyIID
FOLDERID_CommonAdminTools: _PyIID
FOLDERID_CommonOEMLinks: _PyIID
FOLDERID_CommonPrograms: _PyIID
FOLDERID_CommonStartMenu: _PyIID
FOLDERID_CommonStartup: _PyIID
FOLDERID_CommonTemplates: _PyIID
FOLDERID_ComputerFolder: _PyIID
FOLDERID_ConflictFolder: _PyIID
FOLDERID_ConnectionsFolder: _PyIID
FOLDERID_Contacts: _PyIID
FOLDERID_ControlPanelFolder: _PyIID
FOLDERID_Cookies: _PyIID
FOLDERID_Desktop: _PyIID
FOLDERID_DeviceMetadataStore: _PyIID
FOLDERID_Documents: _PyIID
FOLDERID_DocumentsLibrary: _PyIID
FOLDERID_Downloads: _PyIID
FOLDERID_Favorites: _PyIID
FOLDERID_Fonts: _PyIID
FOLDERID_GameTasks: _PyIID
FOLDERID_Games: _PyIID
FOLDERID_History: _PyIID
FOLDERID_HomeGroup: _PyIID
FOLDERID_ImplicitAppShortcuts: _PyIID
FOLDERID_InternetCache: _PyIID
FOLDERID_InternetFolder: _PyIID
FOLDERID_Libraries: _PyIID
FOLDERID_Links: _PyIID
FOLDERID_LocalAppData: _PyIID
FOLDERID_LocalAppDataLow: _PyIID
FOLDERID_LocalizedResourcesDir: _PyIID
FOLDERID_Music: _PyIID
FOLDERID_MusicLibrary: _PyIID
FOLDERID_NetHood: _PyIID
FOLDERID_NetworkFolder: _PyIID
FOLDERID_OriginalImages: _PyIID
FOLDERID_PhotoAlbums: _PyIID
FOLDERID_Pictures: _PyIID
FOLDERID_PicturesLibrary: _PyIID
FOLDERID_Playlists: _PyIID
FOLDERID_PrintHood: _PyIID
FOLDERID_PrintersFolder: _PyIID
FOLDERID_Profile: _PyIID
FOLDERID_ProgramData: _PyIID
FOLDERID_ProgramFiles: _PyIID
FOLDERID_ProgramFilesCommon: _PyIID
FOLDERID_ProgramFilesCommonX64: _PyIID
FOLDERID_ProgramFilesCommonX86: _PyIID
FOLDERID_ProgramFilesX64: _PyIID
FOLDERID_ProgramFilesX86: _PyIID
FOLDERID_Programs: _PyIID
FOLDERID_Public: _PyIID
FOLDERID_PublicDesktop: _PyIID
FOLDERID_PublicDocuments: _PyIID
FOLDERID_PublicDownloads: _PyIID
FOLDERID_PublicGameTasks: _PyIID
FOLDERID_PublicLibraries: _PyIID
FOLDERID_PublicMusic: _PyIID
FOLDERID_PublicPictures: _PyIID
FOLDERID_PublicRingtones: _PyIID
FOLDERID_PublicVideos: _PyIID
FOLDERID_QuickLaunch: _PyIID
FOLDERID_Recent: _PyIID
FOLDERID_RecordedTVLibrary: _PyIID
FOLDERID_RecycleBinFolder: _PyIID
FOLDERID_ResourceDir: _PyIID
FOLDERID_Ringtones: _PyIID
FOLDERID_RoamingAppData: _PyIID
FOLDERID_SEARCH_CSC: _PyIID
FOLDERID_SEARCH_MAPI: _PyIID
FOLDERID_SampleMusic: _PyIID
FOLDERID_SamplePictures: _PyIID
FOLDERID_SamplePlaylists: _PyIID
FOLDERID_SampleVideos: _PyIID
FOLDERID_SavedGames: _PyIID
FOLDERID_SavedSearches: _PyIID
FOLDERID_SearchHome: _PyIID
FOLDERID_SendTo: _PyIID
FOLDERID_SidebarDefaultParts: _PyIID
FOLDERID_SidebarParts: _PyIID
FOLDERID_StartMenu: _PyIID
FOLDERID_Startup: _PyIID
FOLDERID_SyncManagerFolder: _PyIID
FOLDERID_SyncResultsFolder: _PyIID
FOLDERID_SyncSetupFolder: _PyIID
FOLDERID_System: _PyIID
FOLDERID_SystemX86: _PyIID
FOLDERID_Templates: _PyIID
FOLDERID_UserPinned: _PyIID
FOLDERID_UserProfiles: _PyIID
FOLDERID_UserProgramFiles: _PyIID
FOLDERID_UserProgramFilesCommon: _PyIID
FOLDERID_UsersFiles: _PyIID
FOLDERID_UsersLibraries: _PyIID
FOLDERID_Videos: _PyIID
FOLDERID_VideosLibrary: _PyIID
FOLDERID_Windows: _PyIID
FOLDERTYPEID_Communications: _PyIID
FOLDERTYPEID_CompressedFolder: _PyIID
FOLDERTYPEID_Contacts: _PyIID
FOLDERTYPEID_ControlPanelCategory: _PyIID
FOLDERTYPEID_ControlPanelClassic: _PyIID
FOLDERTYPEID_Documents: _PyIID
FOLDERTYPEID_Games: _PyIID
FOLDERTYPEID_Generic: _PyIID
FOLDERTYPEID_GenericLibrary: _PyIID
FOLDERTYPEID_GenericSearchResults: _PyIID
FOLDERTYPEID_Invalid: _PyIID
FOLDERTYPEID_Music: _PyIID
FOLDERTYPEID_NetworkExplorer: _PyIID
FOLDERTYPEID_OpenSearch: _PyIID
FOLDERTYPEID_OtherUsers: _PyIID
FOLDERTYPEID_Pictures: _PyIID
FOLDERTYPEID_Printers: _PyIID
FOLDERTYPEID_PublishedItems: _PyIID
FOLDERTYPEID_RecordedTV: _PyIID
FOLDERTYPEID_RecycleBin: _PyIID
FOLDERTYPEID_SavedGames: _PyIID
FOLDERTYPEID_SearchConnector: _PyIID
FOLDERTYPEID_SearchHome: _PyIID
FOLDERTYPEID_Searches: _PyIID
FOLDERTYPEID_SoftwareExplorer: _PyIID
FOLDERTYPEID_StartMenu: _PyIID
FOLDERTYPEID_UserFiles: _PyIID
FOLDERTYPEID_UsersLibraries: _PyIID
FOLDERTYPEID_Videos: _PyIID
def GetCurrentProcessExplicitAppUserModelID() -> typing.Any:
    ...

HOTKEYF_ALT: int
HOTKEYF_CONTROL: int
HOTKEYF_EXT: int
HOTKEYF_SHIFT: int
IID_CDefView: _PyIID
IID_IADesktopP2: _PyIID
IID_IActiveDesktop: _PyIID
IID_IActiveDesktopP: _PyIID
IID_IApplicationDestinations: _PyIID
IID_IApplicationDocumentLists: _PyIID
IID_IAsyncOperation: _PyIID
IID_IBrowserFrameOptions: _PyIID
IID_ICategorizer: _PyIID
IID_ICategoryProvider: _PyIID
IID_IColumnProvider: _PyIID
IID_IContextMenu: _PyIID
IID_IContextMenu2: _PyIID
IID_IContextMenu3: _PyIID
IID_ICopyHook: _PyIID
IID_ICopyHookA: _PyIID
IID_ICopyHookW: _PyIID
IID_ICurrentItem: _PyIID
IID_ICustomDestinationList: _PyIID
IID_IDefaultExtractIconInit: _PyIID
IID_IDeskBand: _PyIID
IID_IDisplayItem: _PyIID
IID_IDockingWindow: _PyIID
IID_IDropTargetHelper: _PyIID
IID_IEmptyVolumeCache: _PyIID
IID_IEmptyVolumeCache2: _PyIID
IID_IEmptyVolumeCacheCallBack: _PyIID
IID_IEnumExplorerCommand: _PyIID
IID_IEnumIDList: _PyIID
IID_IEnumObjects: _PyIID
IID_IEnumResources: _PyIID
IID_IEnumShellItems: _PyIID
IID_IExplorerBrowser: _PyIID
IID_IExplorerBrowserEvents: _PyIID
IID_IExplorerCommand: _PyIID
IID_IExplorerCommandProvider: _PyIID
IID_IExplorerPaneVisibility: _PyIID
IID_IExtractIcon: _PyIID
IID_IExtractIconW: _PyIID
IID_IExtractImage: _PyIID
IID_IFileOperation: _PyIID
IID_IFileOperationProgressSink: _PyIID
IID_IIdentityName: _PyIID
IID_IKnownFolder: _PyIID
IID_IKnownFolderManager: _PyIID
IID_INameSpaceTreeControl: _PyIID
IID_IObjectArray: _PyIID
IID_IObjectCollection: _PyIID
IID_IPersistFolder: _PyIID
IID_IPersistFolder2: _PyIID
IID_IQueryAssociations: _PyIID
IID_IRelatedItem: _PyIID
IID_IShellBrowser: _PyIID
IID_IShellCopyHook: _PyIID
IID_IShellCopyHookA: _PyIID
IID_IShellCopyHookW: _PyIID
IID_IShellExtInit: _PyIID
IID_IShellFolder: _PyIID
IID_IShellFolder2: _PyIID
IID_IShellIcon: _PyIID
IID_IShellIconOverlay: _PyIID
IID_IShellIconOverlayIdentifier: _PyIID
IID_IShellIconOverlayManager: _PyIID
IID_IShellItem: _PyIID
IID_IShellItem2: _PyIID
IID_IShellItemArray: _PyIID
IID_IShellItemResources: _PyIID
IID_IShellLibrary: _PyIID
IID_IShellLink: _PyIID
IID_IShellLinkA: _PyIID
IID_IShellLinkDataList: _PyIID
IID_IShellLinkW: _PyIID
IID_IShellView: _PyIID
IID_ITaskbarList: _PyIID
IID_ITransferAdviseSink: _PyIID
IID_ITransferDestination: _PyIID
IID_ITransferMediumItem: _PyIID
IID_ITransferSource: _PyIID
IID_IUniformResourceLocator: _PyIID
def IsUserAnAdmin() -> typing.Any:
    ...

def PIDLAsString() -> typing.Any:
    ...

ResourceTypeStream: _PyIID
def SHAddToRecentDocs() -> typing.Any:
    ...

def SHBrowseForFolder() -> typing.Any:
    ...

def SHChangeNotify() -> typing.Any:
    ...

def SHChangeNotifyDeregister() -> typing.Any:
    ...

def SHChangeNotifyRegister() -> typing.Any:
    ...

def SHCreateDataObject() -> typing.Any:
    ...

def SHCreateDefaultContextMenu() -> typing.Any:
    ...

def SHCreateDefaultExtractIcon() -> typing.Any:
    ...

def SHCreateItemFromIDList() -> typing.Any:
    ...

def SHCreateItemFromParsingName() -> typing.Any:
    ...

def SHCreateItemFromRelativeName() -> typing.Any:
    ...

def SHCreateItemInKnownFolder() -> typing.Any:
    ...

def SHCreateItemWithParent() -> typing.Any:
    ...

def SHCreateShellFolderView() -> typing.Any:
    ...

def SHCreateShellItem() -> typing.Any:
    ...

def SHCreateShellItemArray() -> typing.Any:
    ...

def SHCreateShellItemArrayFromDataObject() -> typing.Any:
    ...

def SHCreateShellItemArrayFromIDLists() -> typing.Any:
    ...

def SHCreateShellItemArrayFromShellItem() -> typing.Any:
    ...

def SHCreateStreamOnFileEx() -> typing.Any:
    ...

def SHEmptyRecycleBin() -> typing.Any:
    ...

def SHFileOperation() -> typing.Any:
    ...

def SHGetDesktopFolder() -> typing.Any:
    ...

def SHGetFileInfo() -> typing.Any:
    ...

def SHGetFolderLocation() -> typing.Any:
    ...

def SHGetFolderPath() -> typing.Any:
    ...

def SHGetIDListFromObject() -> typing.Any:
    ...

def SHGetInstanceExplorer() -> typing.Any:
    ...

def SHGetNameFromIDList() -> typing.Any:
    ...

def SHGetPathFromIDList() -> typing.Any:
    ...

def SHGetPathFromIDListW() -> typing.Any:
    ...

def SHGetSettings() -> typing.Any:
    ...

def SHGetSpecialFolderLocation() -> typing.Any:
    ...

def SHGetSpecialFolderPath() -> typing.Any:
    ...

def SHGetViewStatePropertyBag() -> typing.Any:
    ...

def SHILCreateFromPath() -> typing.Any:
    ...

def SHOpenFolderAndSelectItems() -> typing.Any:
    ...

def SHParseDisplayName() -> typing.Any:
    ...

def SHQueryRecycleBin() -> typing.Any:
    ...

def SHSetFolderPath() -> typing.Any:
    ...

def SHUpdateImage() -> typing.Any:
    ...

SID_CtxQueryAssociations: _PyIID
SID_DefView: _PyIID
SID_LinkSite: _PyIID
SID_MenuShellFolder: _PyIID
SID_SCommDlgBrowser: _PyIID
SID_SGetViewFromViewDual: _PyIID
SID_SInternetExplorer: _PyIID
SID_SMenuBandBKContextMenu: _PyIID
SID_SMenuBandBottom: _PyIID
SID_SMenuBandBottomSelected: _PyIID
SID_SMenuBandChild: _PyIID
SID_SMenuBandContextMenuModifier: _PyIID
SID_SMenuBandParent: _PyIID
SID_SMenuBandTop: _PyIID
SID_SMenuPopup: _PyIID
SID_SProgressUI: _PyIID
SID_SShellBrowser: _PyIID
SID_SShellDesktop: _PyIID
SID_STopLevelBrowser: _PyIID
SID_STopWindow: _PyIID
SID_SUrlHistory: _PyIID
SID_SWebBrowserApp: _PyIID
SID_ShellFolderViewCB: _PyIID
SLGP_RAWPATH: int
SLGP_SHORTPATH: int
SLGP_UNCPRIORITY: int
SLR_ANY_MATCH: int
SLR_INVOKE_MSI: int
SLR_NOLINKINFO: int
SLR_NOSEARCH: int
SLR_NOTRACK: int
SLR_NOUPDATE: int
SLR_NO_UI: int
SLR_UPDATE: int
def SetCurrentProcessExplicitAppUserModelID() -> typing.Any:
    ...

def ShellExecuteEx() -> typing.Any:
    ...

def StringAsCIDA() -> typing.Any:
    ...

def StringAsFILEGROUPDESCRIPTOR() -> typing.Any:
    ...

def StringAsPIDL() -> typing.Any:
    ...

VID_Details: _PyIID
VID_LargeIcons: _PyIID
VID_List: _PyIID
VID_SmallIcons: _PyIID
VID_ThumbStrip: _PyIID
VID_Thumbnails: _PyIID
VID_Tile: _PyIID
__doc__: str
__file__: str
__name__: str
__package__: str
error = _mod_pywintypes.com_error
def __getattr__(name) -> typing.Any:
    ...

