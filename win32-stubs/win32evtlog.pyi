# Python: 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)]
# Library: win32evtlog, version: unspecified
# Module: win32evtlog, version: unspecified

''

import typing
import builtins as _mod_builtins
from .lib import pywintypes as _mod_pywintypes

def BackupEventLog() -> typing.Any:
    ...

def ClearEventLog() -> typing.Any:
    ...

def CloseEventLog() -> typing.Any:
    ...

def DeregisterEventSource() -> typing.Any:
    ...

EVENTLOG_AUDIT_FAILURE: int
EVENTLOG_AUDIT_SUCCESS: int
EVENTLOG_BACKWARDS_READ: int
EVENTLOG_END_ALL_PAIRED_EVENTS: int
EVENTLOG_END_PAIRED_EVENT: int
EVENTLOG_ERROR_TYPE: int
EVENTLOG_FORWARDS_READ: int
EVENTLOG_INFORMATION_TYPE: int
EVENTLOG_PAIRED_EVENT_ACTIVE: int
EVENTLOG_PAIRED_EVENT_INACTIVE: int
EVENTLOG_SEEK_READ: int
EVENTLOG_SEQUENTIAL_READ: int
EVENTLOG_START_PAIRED_EVENT: int
EVENTLOG_SUCCESS: int
EVENTLOG_WARNING_TYPE: int
EventMetadataEventChannel: int
EventMetadataEventID: int
EventMetadataEventKeyword: int
EventMetadataEventLevel: int
EventMetadataEventMessageID: int
EventMetadataEventOpcode: int
EventMetadataEventTask: int
EventMetadataEventTemplate: int
EventMetadataEventVersion: int
def EvtArchiveExportedLog() -> typing.Any:
    ...

EvtChannelConfigAccess: int
EvtChannelConfigClassicEventlog: int
EvtChannelConfigEnabled: int
EvtChannelConfigIsolation: int
EvtChannelConfigOwningPublisher: int
EvtChannelConfigPropertyIdEND: int
EvtChannelConfigType: int
EvtChannelLoggingConfigAutoBackup: int
EvtChannelLoggingConfigLogFilePath: int
EvtChannelLoggingConfigMaxSize: int
EvtChannelLoggingConfigRetention: int
EvtChannelPublisherList: int
EvtChannelPublishingConfigBufferSize: int
EvtChannelPublishingConfigClockType: int
EvtChannelPublishingConfigControlGuid: int
EvtChannelPublishingConfigKeywords: int
EvtChannelPublishingConfigLatency: int
EvtChannelPublishingConfigLevel: int
EvtChannelPublishingConfigMaxBuffers: int
EvtChannelPublishingConfigMinBuffers: int
EvtChannelPublishingConfigSidType: int
def EvtClearLog() -> typing.Any:
    ...

def EvtCreateBookmark() -> typing.Any:
    ...

def EvtCreateRenderContext() -> typing.Any:
    ...

EvtEventMetadataPropertyIdEND: int
EvtEventPath: int
EvtEventPropertyIdEND: int
EvtEventQueryIDs: int
def EvtExportLog() -> typing.Any:
    ...

EvtExportLogChannelPath: int
EvtExportLogFilePath: int
EvtExportLogTolerateQueryErrors: int
def EvtFormatMessage() -> typing.Any:
    ...

EvtFormatMessageChannel: int
EvtFormatMessageEvent: int
EvtFormatMessageId: int
EvtFormatMessageKeyword: int
EvtFormatMessageLevel: int
EvtFormatMessageOpcode: int
EvtFormatMessageProvider: int
EvtFormatMessageTask: int
EvtFormatMessageXml: int
def EvtGetChannelConfigProperty() -> typing.Any:
    ...

def EvtGetEventInfo() -> typing.Any:
    ...

def EvtGetEventMetadataProperty() -> typing.Any:
    ...

def EvtGetExtendedStatus() -> typing.Any:
    ...

def EvtGetLogInfo() -> typing.Any:
    ...

def EvtGetObjectArrayProperty() -> typing.Any:
    ...

def EvtGetObjectArraySize() -> typing.Any:
    ...

def EvtGetPublisherMetadataProperty() -> typing.Any:
    ...

EvtLogAttributes: int
EvtLogCreationTime: int
EvtLogFileSize: int
EvtLogFull: int
EvtLogLastAccessTime: int
EvtLogLastWriteTime: int
EvtLogNumberOfLogRecords: int
EvtLogOldestRecordNumber: int
def EvtNext() -> typing.Any:
    ...

def EvtNextChannelPath() -> typing.Any:
    ...

def EvtNextEventMetadata() -> typing.Any:
    ...

def EvtNextPublisherId() -> typing.Any:
    ...

def EvtOpenChannelConfig() -> typing.Any:
    ...

def EvtOpenChannelEnum() -> typing.Any:
    ...

EvtOpenChannelPath: int
def EvtOpenEventMetadataEnum() -> typing.Any:
    ...

EvtOpenFilePath: int
def EvtOpenLog() -> typing.Any:
    ...

def EvtOpenPublisherEnum() -> typing.Any:
    ...

def EvtOpenPublisherMetadata() -> typing.Any:
    ...

def EvtOpenSession() -> typing.Any:
    ...

EvtPublisherMetadataChannelReferenceFlags: int
EvtPublisherMetadataChannelReferenceID: int
EvtPublisherMetadataChannelReferenceIndex: int
EvtPublisherMetadataChannelReferenceMessageID: int
EvtPublisherMetadataChannelReferencePath: int
EvtPublisherMetadataChannelReferences: int
EvtPublisherMetadataHelpLink: int
EvtPublisherMetadataKeywordMessageID: int
EvtPublisherMetadataKeywordName: int
EvtPublisherMetadataKeywordValue: int
EvtPublisherMetadataKeywords: int
EvtPublisherMetadataLevelMessageID: int
EvtPublisherMetadataLevelName: int
EvtPublisherMetadataLevelValue: int
EvtPublisherMetadataLevels: int
EvtPublisherMetadataMessageFilePath: int
EvtPublisherMetadataOpcodeMessageID: int
EvtPublisherMetadataOpcodeName: int
EvtPublisherMetadataOpcodeValue: int
EvtPublisherMetadataOpcodes: int
EvtPublisherMetadataParameterFilePath: int
EvtPublisherMetadataPropertyIdEND: int
EvtPublisherMetadataPublisherGuid: int
EvtPublisherMetadataPublisherMessageID: int
EvtPublisherMetadataResourceFilePath: int
EvtPublisherMetadataTaskEventGuid: int
EvtPublisherMetadataTaskMessageID: int
EvtPublisherMetadataTaskName: int
EvtPublisherMetadataTaskValue: int
EvtPublisherMetadataTasks: int
def EvtQuery() -> typing.Any:
    ...

EvtQueryChannelPath: int
EvtQueryFilePath: int
EvtQueryForwardDirection: int
EvtQueryReverseDirection: int
EvtQueryTolerateQueryErrors: int
def EvtRender() -> typing.Any:
    ...

EvtRenderBookmark: int
EvtRenderContextSystem: int
EvtRenderContextUser: int
EvtRenderContextValues: int
EvtRenderEventValues: int
EvtRenderEventXml: int
EvtRpcLogin: int
EvtRpcLoginAuthDefault: int
EvtRpcLoginAuthKerberos: int
EvtRpcLoginAuthNTLM: int
EvtRpcLoginAuthNegotiate: int
def EvtSeek() -> typing.Any:
    ...

EvtSeekOriginMask: int
EvtSeekRelativeToBookmark: int
EvtSeekRelativeToCurrent: int
EvtSeekRelativeToFirst: int
EvtSeekRelativeToLast: int
EvtSeekStrict: int
def EvtSubscribe() -> typing.Any:
    ...

EvtSubscribeActionDeliver: int
EvtSubscribeActionError: int
EvtSubscribeOriginMask: int
EvtSubscribeStartAfterBookmark: int
EvtSubscribeStartAtOldestRecord: int
EvtSubscribeStrict: int
EvtSubscribeToFutureEvents: int
EvtSubscribeTolerateQueryErrors: int
EvtSystemActivityID: int
EvtSystemChannel: int
EvtSystemComputer: int
EvtSystemEventID: int
EvtSystemEventRecordId: int
EvtSystemKeywords: int
EvtSystemLevel: int
EvtSystemOpcode: int
EvtSystemProcessID: int
EvtSystemPropertyIdEND: int
EvtSystemProviderGuid: int
EvtSystemProviderName: int
EvtSystemQualifiers: int
EvtSystemRelatedActivityID: int
EvtSystemTask: int
EvtSystemThreadID: int
EvtSystemTimeCreated: int
EvtSystemUserID: int
EvtSystemVersion: int
def EvtUpdateBookmark() -> typing.Any:
    ...

EvtVarTypeAnsiString: int
EvtVarTypeBinary: int
EvtVarTypeBoolean: int
EvtVarTypeByte: int
EvtVarTypeDouble: int
EvtVarTypeEvtHandle: int
EvtVarTypeEvtXml: int
EvtVarTypeFileTime: int
EvtVarTypeGuid: int
EvtVarTypeHexInt32: int
EvtVarTypeHexInt64: int
EvtVarTypeInt16: int
EvtVarTypeInt32: int
EvtVarTypeInt64: int
EvtVarTypeNull: int
EvtVarTypeSByte: int
EvtVarTypeSid: int
EvtVarTypeSingle: int
EvtVarTypeSizeT: int
EvtVarTypeString: int
EvtVarTypeSysTime: int
EvtVarTypeUInt16: int
EvtVarTypeUInt32: int
EvtVarTypeUInt64: int
def GetNumberOfEventLogRecords() -> typing.Any:
    ...

def GetOldestEventLogRecord() -> typing.Any:
    ...

def NotifyChangeEventLog() -> typing.Any:
    ...

def OpenBackupEventLog() -> typing.Any:
    ...

def OpenEventLog() -> typing.Any:
    ...

def ReadEventLog() -> typing.Any:
    ...

def RegisterEventSource() -> typing.Any:
    ...

def ReportEvent() -> typing.Any:
    ...

UNICODE: int
__doc__: str
__file__: str
__name__: str
__package__: str
error = _mod_pywintypes.error
def __getattr__(name) -> typing.Any:
    ...

