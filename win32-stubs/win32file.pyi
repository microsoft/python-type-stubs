# Python: 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)]
# Library: win32file, version: unspecified
# Module: win32file, version: unspecified

''

import typing
import builtins as _mod_builtins
from .lib import pywintypes as _mod_pywintypes

def AcceptEx() -> typing.Any:
    ...

def AddUsersToEncryptedFile() -> typing.Any:
    ...

def AllocateReadBuffer() -> typing.Any:
    ...

def AreFileApisANSI() -> typing.Any:
    ...

def BackupRead() -> typing.Any:
    ...

def BackupSeek() -> typing.Any:
    ...

def BackupWrite() -> typing.Any:
    ...

def BuildCommDCB() -> typing.Any:
    ...

CALLBACK_CHUNK_FINISHED: int
CALLBACK_STREAM_SWITCH: int
CBR_110: int
CBR_115200: int
CBR_1200: int
CBR_128000: int
CBR_14400: int
CBR_19200: int
CBR_2400: int
CBR_256000: int
CBR_300: int
CBR_38400: int
CBR_4800: int
CBR_56000: int
CBR_57600: int
CBR_600: int
CBR_9600: int
CLRBREAK: int
CLRDTR: int
CLRRTS: int
COPY_FILE_ALLOW_DECRYPTED_DESTINATION: int
COPY_FILE_FAIL_IF_EXISTS: int
COPY_FILE_OPEN_SOURCE_FOR_WRITE: int
COPY_FILE_RESTARTABLE: int
CREATE_ALWAYS: int
CREATE_FOR_DIR: int
CREATE_FOR_IMPORT: int
CREATE_NEW: int
def CalculateSocketEndPointSize() -> typing.Any:
    ...

def CancelIo() -> typing.Any:
    ...

def ClearCommBreak() -> typing.Any:
    ...

def ClearCommError() -> typing.Any:
    ...

def CloseEncryptedFileRaw() -> typing.Any:
    ...

def CloseHandle() -> typing.Any:
    ...

def ConnectEx() -> typing.Any:
    ...

def CopyFile() -> typing.Any:
    ...

def CopyFileEx() -> typing.Any:
    ...

def CopyFileW() -> typing.Any:
    ...

def CreateDirectory() -> typing.Any:
    ...

def CreateDirectoryEx() -> typing.Any:
    ...

def CreateDirectoryExW() -> typing.Any:
    ...

def CreateDirectoryW() -> typing.Any:
    ...

def CreateFile() -> typing.Any:
    ...

def CreateFileW() -> typing.Any:
    ...

def CreateHardLink() -> typing.Any:
    ...

def CreateIoCompletionPort() -> typing.Any:
    ...

def CreateMailslot() -> typing.Any:
    ...

def CreateSymbolicLink() -> typing.Any:
    ...

def DCB() -> typing.Any:
    ...

DRIVE_CDROM: int
DRIVE_FIXED: int
DRIVE_NO_ROOT_DIR: int
DRIVE_RAMDISK: int
DRIVE_REMOTE: int
DRIVE_REMOVABLE: int
DRIVE_UNKNOWN: int
DTR_CONTROL_DISABLE: int
DTR_CONTROL_ENABLE: int
DTR_CONTROL_HANDSHAKE: int
def DecryptFile() -> typing.Any:
    ...

def DefineDosDevice() -> typing.Any:
    ...

def DefineDosDeviceW() -> typing.Any:
    ...

def DeleteFile() -> typing.Any:
    ...

def DeleteFileW() -> typing.Any:
    ...

def DeleteVolumeMountPoint() -> typing.Any:
    ...

def DeviceIoControl() -> typing.Any:
    ...

def DuplicateEncryptionInfoFile() -> typing.Any:
    ...

EVENPARITY: int
EV_BREAK: int
EV_CTS: int
EV_DSR: int
EV_ERR: int
EV_RING: int
EV_RLSD: int
EV_RXCHAR: int
EV_RXFLAG: int
EV_TXEMPTY: int
def EncryptFile() -> typing.Any:
    ...

def EncryptionDisable() -> typing.Any:
    ...

def EscapeCommFunction() -> typing.Any:
    ...

FD_ACCEPT: int
FD_ADDRESS_LIST_CHANGE: int
FD_CLOSE: int
FD_CONNECT: int
FD_GROUP_QOS: int
FD_OOB: int
FD_QOS: int
FD_READ: int
FD_ROUTING_INTERFACE_CHANGE: int
FD_WRITE: int
FILE_ALL_ACCESS: int
FILE_ATTRIBUTE_ARCHIVE: int
FILE_ATTRIBUTE_COMPRESSED: int
FILE_ATTRIBUTE_DIRECTORY: int
FILE_ATTRIBUTE_HIDDEN: int
FILE_ATTRIBUTE_NORMAL: int
FILE_ATTRIBUTE_OFFLINE: int
FILE_ATTRIBUTE_READONLY: int
FILE_ATTRIBUTE_SYSTEM: int
FILE_ATTRIBUTE_TEMPORARY: int
FILE_BEGIN: int
FILE_CURRENT: int
FILE_ENCRYPTABLE: int
FILE_END: int
FILE_FLAG_BACKUP_SEMANTICS: int
FILE_FLAG_DELETE_ON_CLOSE: int
FILE_FLAG_NO_BUFFERING: int
FILE_FLAG_OPEN_REPARSE_POINT: int
FILE_FLAG_OVERLAPPED: int
FILE_FLAG_POSIX_SEMANTICS: int
FILE_FLAG_RANDOM_ACCESS: int
FILE_FLAG_SEQUENTIAL_SCAN: int
FILE_FLAG_WRITE_THROUGH: int
FILE_GENERIC_READ: int
FILE_GENERIC_WRITE: int
FILE_IS_ENCRYPTED: int
def FILE_NOTIFY_INFORMATION() -> typing.Any:
    ...

FILE_READ_ONLY: int
FILE_ROOT_DIR: int
FILE_SHARE_DELETE: int
FILE_SHARE_READ: int
FILE_SHARE_WRITE: int
FILE_SYSTEM_ATTR: int
FILE_SYSTEM_DIR: int
FILE_SYSTEM_NOT_SUPPORT: int
FILE_TYPE_CHAR: int
FILE_TYPE_DISK: int
FILE_TYPE_PIPE: int
FILE_TYPE_UNKNOWN: int
FILE_UNKNOWN: int
FILE_USER_DISALLOWED: int
FileAllocationInfo: int
FileAttributeTagInfo: int
FileBasicInfo: int
FileCompressionInfo: int
FileDispositionInfo: int
def FileEncryptionStatus() -> typing.Any:
    ...

FileEndOfFileInfo: int
FileIdBothDirectoryInfo: int
FileIdBothDirectoryRestartInfo: int
FileIdType: int
FileIoPriorityHintInfo: int
FileNameInfo: int
FileRenameInfo: int
FileStandardInfo: int
FileStreamInfo: int
def FindClose() -> typing.Any:
    ...

def FindCloseChangeNotification() -> typing.Any:
    ...

def FindFileNames() -> typing.Any:
    ...

def FindFilesIterator() -> typing.Any:
    ...

def FindFilesW() -> typing.Any:
    ...

def FindFirstChangeNotification() -> typing.Any:
    ...

def FindNextChangeNotification() -> typing.Any:
    ...

def FindStreams() -> typing.Any:
    ...

def FlushFileBuffers() -> typing.Any:
    ...

GENERIC_EXECUTE: int
GENERIC_READ: int
GENERIC_WRITE: int
def GetAcceptExSockaddrs() -> typing.Any:
    ...

def GetBinaryType() -> typing.Any:
    ...

def GetCommMask() -> typing.Any:
    ...

def GetCommModemStatus() -> typing.Any:
    ...

def GetCommState() -> typing.Any:
    ...

def GetCommTimeouts() -> typing.Any:
    ...

def GetCompressedFileSize() -> typing.Any:
    ...

def GetDiskFreeSpace() -> typing.Any:
    ...

def GetDiskFreeSpaceEx() -> typing.Any:
    ...

def GetDriveType() -> typing.Any:
    ...

def GetDriveTypeW() -> typing.Any:
    ...

def GetFileAttributes() -> typing.Any:
    ...

def GetFileAttributesEx() -> typing.Any:
    ...

def GetFileAttributesExW() -> typing.Any:
    ...

def GetFileAttributesW() -> typing.Any:
    ...

GetFileExInfoStandard: int
def GetFileInformationByHandle() -> typing.Any:
    ...

def GetFileInformationByHandleEx() -> typing.Any:
    ...

def GetFileSize() -> typing.Any:
    ...

def GetFileTime() -> typing.Any:
    ...

def GetFileType() -> typing.Any:
    ...

def GetFinalPathNameByHandle() -> typing.Any:
    ...

def GetFullPathName() -> typing.Any:
    ...

def GetLogicalDrives() -> typing.Any:
    ...

def GetLongPathName() -> typing.Any:
    ...

def GetMailslotInfo() -> typing.Any:
    ...

def GetOverlappedResult() -> typing.Any:
    ...

def GetQueuedCompletionStatus() -> typing.Any:
    ...

def GetVolumeNameForVolumeMountPoint() -> typing.Any:
    ...

def GetVolumePathName() -> typing.Any:
    ...

def GetVolumePathNamesForVolumeName() -> typing.Any:
    ...

INVALID_HANDLE_VALUE: int
IoPriorityHintLow: int
IoPriorityHintNormal: int
IoPriorityHintVeryLow: int
def LockFile() -> typing.Any:
    ...

def LockFileEx() -> typing.Any:
    ...

MARKPARITY: int
MOVEFILE_COPY_ALLOWED: int
MOVEFILE_CREATE_HARDLINK: int
MOVEFILE_DELAY_UNTIL_REBOOT: int
MOVEFILE_FAIL_IF_NOT_TRACKABLE: int
MOVEFILE_REPLACE_EXISTING: int
MOVEFILE_WRITE_THROUGH: int
def MoveFile() -> typing.Any:
    ...

def MoveFileEx() -> typing.Any:
    ...

def MoveFileExW() -> typing.Any:
    ...

def MoveFileW() -> typing.Any:
    ...

def MoveFileWithProgress() -> typing.Any:
    ...

NOPARITY: int
ODDPARITY: int
ONE5STOPBITS: int
ONESTOPBIT: int
OPEN_ALWAYS: int
OPEN_EXISTING: int
def OVERLAPPED() -> typing.Any:
    ...

OVERWRITE_HIDDEN: int
ObjectIdType: int
def OpenEncryptedFileRaw() -> typing.Any:
    ...

def OpenFileById() -> typing.Any:
    ...

PROGRESS_CANCEL: int
PROGRESS_CONTINUE: int
PROGRESS_QUIET: int
PROGRESS_STOP: int
PURGE_RXABORT: int
PURGE_RXCLEAR: int
PURGE_TXABORT: int
PURGE_TXCLEAR: int
def PostQueuedCompletionStatus() -> typing.Any:
    ...

def PurgeComm() -> typing.Any:
    ...

def QueryDosDevice() -> typing.Any:
    ...

def QueryRecoveryAgentsOnEncryptedFile() -> typing.Any:
    ...

def QueryUsersOnEncryptedFile() -> typing.Any:
    ...

REPLACEFILE_IGNORE_MERGE_ERRORS: int
REPLACEFILE_WRITE_THROUGH: int
RTS_CONTROL_DISABLE: int
RTS_CONTROL_ENABLE: int
RTS_CONTROL_HANDSHAKE: int
RTS_CONTROL_TOGGLE: int
def ReOpenFile() -> typing.Any:
    ...

def ReadDirectoryChangesW() -> typing.Any:
    ...

def ReadEncryptedFileRaw() -> typing.Any:
    ...

def ReadFile() -> typing.Any:
    ...

def RemoveDirectory() -> typing.Any:
    ...

def RemoveUsersFromEncryptedFile() -> typing.Any:
    ...

def ReplaceFile() -> typing.Any:
    ...

SCS_32BIT_BINARY: int
SCS_DOS_BINARY: int
SCS_OS216_BINARY: int
SCS_PIF_BINARY: int
SCS_POSIX_BINARY: int
SCS_WOW_BINARY: int
SECURITY_ANONYMOUS: int
SECURITY_CONTEXT_TRACKING: int
SECURITY_DELEGATION: int
SECURITY_EFFECTIVE_ONLY: int
SECURITY_IDENTIFICATION: int
SECURITY_IMPERSONATION: int
SETBREAK: int
SETDTR: int
SETRTS: int
SETXOFF: int
SETXON: int
SO_CONNECT_TIME: int
SO_UPDATE_ACCEPT_CONTEXT: int
SO_UPDATE_CONNECT_CONTEXT: int
SPACEPARITY: int
SYMBOLIC_LINK_FLAG_ALLOW_UNPRIVILEGED_CREATE: int
SYMBOLIC_LINK_FLAG_DIRECTORY: int
def SetCommBreak() -> typing.Any:
    ...

def SetCommMask() -> typing.Any:
    ...

def SetCommState() -> typing.Any:
    ...

def SetCommTimeouts() -> typing.Any:
    ...

def SetCurrentDirectory() -> typing.Any:
    ...

def SetEndOfFile() -> typing.Any:
    ...

def SetFileApisToANSI() -> typing.Any:
    ...

def SetFileApisToOEM() -> typing.Any:
    ...

def SetFileAttributes() -> typing.Any:
    ...

def SetFileAttributesW() -> typing.Any:
    ...

def SetFileInformationByHandle() -> typing.Any:
    ...

def SetFilePointer() -> typing.Any:
    ...

def SetFileShortName() -> typing.Any:
    ...

def SetFileTime() -> typing.Any:
    ...

def SetMailslotInfo() -> typing.Any:
    ...

def SetVolumeLabel() -> typing.Any:
    ...

def SetVolumeMountPoint() -> typing.Any:
    ...

def SetupComm() -> typing.Any:
    ...

def SfcGetNextProtectedFile() -> typing.Any:
    ...

def SfcIsFileProtected() -> typing.Any:
    ...

TF_DISCONNECT: int
TF_REUSE_SOCKET: int
TF_USE_DEFAULT_WORKER: int
TF_USE_KERNEL_APC: int
TF_USE_SYSTEM_THREAD: int
TF_WRITE_BEHIND: int
TRUNCATE_EXISTING: int
TWOSTOPBITS: int
def TransmitCommChar() -> typing.Any:
    ...

def TransmitFile() -> typing.Any:
    ...

UNICODE: int
def UnlockFile() -> typing.Any:
    ...

def UnlockFileEx() -> typing.Any:
    ...

def WSAAsyncSelect() -> typing.Any:
    ...

WSAECONNABORTED: int
WSAECONNRESET: int
WSAEDISCON: int
WSAEFAULT: int
WSAEINPROGRESS: int
WSAEINTR: int
WSAEINVAL: int
WSAEMSGSIZE: int
WSAENETDOWN: int
WSAENETRESET: int
WSAENOBUFS: int
WSAENOTCONN: int
WSAENOTSOCK: int
WSAEOPNOTSUPP: int
WSAESHUTDOWN: int
WSAEWOULDBLOCK: int
def WSAEnumNetworkEvents() -> typing.Any:
    ...

def WSAEventSelect() -> typing.Any:
    ...

def WSARecv() -> typing.Any:
    ...

def WSASend() -> typing.Any:
    ...

WSA_IO_PENDING: int
WSA_OPERATION_ABORTED: int
def WaitCommEvent() -> typing.Any:
    ...

def Wow64DisableWow64FsRedirection() -> typing.Any:
    ...

def Wow64RevertWow64FsRedirection() -> typing.Any:
    ...

def WriteEncryptedFileRaw() -> typing.Any:
    ...

def WriteFile() -> typing.Any:
    ...

__doc__: str
__file__: str
__name__: str
__package__: str
def _get_osfhandle() -> typing.Any:
    ...

def _getmaxstdio() -> typing.Any:
    ...

def _open_osfhandle() -> typing.Any:
    ...

def _setmaxstdio() -> typing.Any:
    ...

error = _mod_pywintypes.error
def __getattr__(name) -> typing.Any:
    ...

