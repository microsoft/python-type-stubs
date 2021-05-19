# Python: 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)]
# Library: win32security, version: unspecified
# Module: win32security, version: unspecified

''

import typing
import builtins as _mod_builtins
from .lib import pywintypes as _mod_pywintypes

ACCESS_ALLOWED_ACE_TYPE: int
ACCESS_ALLOWED_OBJECT_ACE_TYPE: int
ACCESS_DENIED_ACE_TYPE: int
ACCESS_DENIED_OBJECT_ACE_TYPE: int
def ACL() -> typing.Any:
    ...

ACL_REVISION: int
ACL_REVISION_DS: int
def AcceptSecurityContext() -> typing.Any:
    ...

def AcquireCredentialsHandle() -> typing.Any:
    ...

def AdjustTokenGroups() -> typing.Any:
    ...

def AdjustTokenPrivileges() -> typing.Any:
    ...

def AllocateLocallyUniqueId() -> typing.Any:
    ...

AuditCategoryAccountLogon: int
AuditCategoryAccountManagement: int
AuditCategoryDetailedTracking: int
AuditCategoryDirectoryServiceAccess: int
AuditCategoryLogon: int
AuditCategoryObjectAccess: int
AuditCategoryPolicyChange: int
AuditCategoryPrivilegeUse: int
AuditCategorySystem: int
CONTAINER_INHERIT_ACE: int
def CheckTokenMembership() -> typing.Any:
    ...

def ConvertSecurityDescriptorToStringSecurityDescriptor() -> typing.Any:
    ...

def ConvertSidToStringSid() -> typing.Any:
    ...

def ConvertStringSecurityDescriptorToSecurityDescriptor() -> typing.Any:
    ...

def ConvertStringSidToSid() -> typing.Any:
    ...

def CreateRestrictedToken() -> typing.Any:
    ...

def CreateWellKnownSid() -> typing.Any:
    ...

CredHandleType = _mod_builtins.PyCredHandle
def CryptEnumProviders() -> typing.Any:
    ...

CtxtHandleType = _mod_builtins.PyCtxtHandle
DACL_SECURITY_INFORMATION: int
DENY_ACCESS: int
DISABLE_MAX_PRIVILEGE: int
DS_SPN_ADD_SPN_OP: int
DS_SPN_DELETE_SPN_OP: int
DS_SPN_DNS_HOST: int
DS_SPN_DN_HOST: int
DS_SPN_DOMAIN: int
DS_SPN_NB_DOMAIN: int
DS_SPN_NB_HOST: int
DS_SPN_REPLACE_SPN_OP: int
DS_SPN_SERVICE: int
def DsBind() -> typing.Any:
    ...

def DsCrackNames() -> typing.Any:
    ...

def DsGetDcName() -> typing.Any:
    ...

def DsGetSpn() -> typing.Any:
    ...

def DsListDomainsInSite() -> typing.Any:
    ...

def DsListInfoForServer() -> typing.Any:
    ...

def DsListRoles() -> typing.Any:
    ...

def DsListServersForDomainInSite() -> typing.Any:
    ...

def DsListServersInSite() -> typing.Any:
    ...

def DsListSites() -> typing.Any:
    ...

def DsUnBind() -> typing.Any:
    ...

def DsWriteAccountSpn() -> typing.Any:
    ...

def DuplicateToken() -> typing.Any:
    ...

def DuplicateTokenEx() -> typing.Any:
    ...

def EnumerateSecurityPackages() -> typing.Any:
    ...

FAILED_ACCESS_ACE_FLAG: int
GRANT_ACCESS: int
GROUP_SECURITY_INFORMATION: int
def GetBinarySid() -> typing.Any:
    ...

def GetFileSecurity() -> typing.Any:
    ...

def GetKernelObjectSecurity() -> typing.Any:
    ...

def GetNamedSecurityInfo() -> typing.Any:
    ...

def GetPolicyHandle() -> typing.Any:
    ...

def GetSecurityInfo() -> typing.Any:
    ...

def GetTokenInformation() -> typing.Any:
    ...

def GetUserObjectSecurity() -> typing.Any:
    ...

INHERITED_ACE: int
INHERIT_ONLY_ACE: int
def ImpersonateAnonymousToken() -> typing.Any:
    ...

def ImpersonateLoggedOnUser() -> typing.Any:
    ...

def ImpersonateNamedPipeClient() -> typing.Any:
    ...

def ImpersonateSelf() -> typing.Any:
    ...

def InitializeSecurityContext() -> typing.Any:
    ...

def IsTokenRestricted() -> typing.Any:
    ...

LABEL_SECURITY_INFORMATION: int
LOGON32_LOGON_BATCH: int
LOGON32_LOGON_INTERACTIVE: int
LOGON32_LOGON_NETWORK: int
LOGON32_LOGON_NETWORK_CLEARTEXT: int
LOGON32_LOGON_NEW_CREDENTIALS: int
LOGON32_LOGON_SERVICE: int
LOGON32_LOGON_UNLOCK: int
LOGON32_PROVIDER_DEFAULT: int
LOGON32_PROVIDER_WINNT35: int
LOGON32_PROVIDER_WINNT40: int
LOGON32_PROVIDER_WINNT50: int
def LogonUser() -> typing.Any:
    ...

def LogonUserEx() -> typing.Any:
    ...

def LookupAccountName() -> typing.Any:
    ...

def LookupAccountSid() -> typing.Any:
    ...

def LookupPrivilegeDisplayName() -> typing.Any:
    ...

def LookupPrivilegeName() -> typing.Any:
    ...

def LookupPrivilegeValue() -> typing.Any:
    ...

def LsaAddAccountRights() -> typing.Any:
    ...

def LsaCallAuthenticationPackage() -> typing.Any:
    ...

def LsaClose() -> typing.Any:
    ...

def LsaConnectUntrusted() -> typing.Any:
    ...

def LsaDeregisterLogonProcess() -> typing.Any:
    ...

def LsaEnumerateAccountRights() -> typing.Any:
    ...

def LsaEnumerateAccountsWithUserRight() -> typing.Any:
    ...

def LsaEnumerateLogonSessions() -> typing.Any:
    ...

def LsaGetLogonSessionData() -> typing.Any:
    ...

def LsaLookupAuthenticationPackage() -> typing.Any:
    ...

def LsaOpenPolicy() -> typing.Any:
    ...

def LsaQueryInformationPolicy() -> typing.Any:
    ...

def LsaRegisterLogonProcess() -> typing.Any:
    ...

def LsaRegisterPolicyChangeNotification() -> typing.Any:
    ...

def LsaRemoveAccountRights() -> typing.Any:
    ...

def LsaRetrievePrivateData() -> typing.Any:
    ...

def LsaSetInformationPolicy() -> typing.Any:
    ...

def LsaStorePrivateData() -> typing.Any:
    ...

def LsaUnregisterPolicyChangeNotification() -> typing.Any:
    ...

MICROSOFT_KERBEROS_NAME_A: bytes
MSV1_0_PACKAGE_NAME: bytes
def MapGenericMask() -> typing.Any:
    ...

NOT_USED_ACCESS: int
NO_INHERITANCE: int
NO_PROPAGATE_INHERIT_ACE: int
OBJECT_INHERIT_ACE: int
OWNER_SECURITY_INFORMATION: int
def OpenProcessToken() -> typing.Any:
    ...

def OpenThreadToken() -> typing.Any:
    ...

POLICY_ALL_ACCESS: int
POLICY_AUDIT_EVENT_FAILURE: int
POLICY_AUDIT_EVENT_NONE: int
POLICY_AUDIT_EVENT_SUCCESS: int
POLICY_AUDIT_EVENT_UNCHANGED: int
POLICY_AUDIT_LOG_ADMIN: int
POLICY_CREATE_ACCOUNT: int
POLICY_CREATE_PRIVILEGE: int
POLICY_CREATE_SECRET: int
POLICY_EXECUTE: int
POLICY_GET_PRIVATE_INFORMATION: int
POLICY_LOOKUP_NAMES: int
POLICY_NOTIFICATION: int
POLICY_READ: int
POLICY_SERVER_ADMIN: int
POLICY_SET_AUDIT_REQUIREMENTS: int
POLICY_SET_DEFAULT_QUOTA_LIMITS: int
POLICY_TRUST_ADMIN: int
POLICY_VIEW_AUDIT_INFORMATION: int
POLICY_VIEW_LOCAL_INFORMATION: int
POLICY_WRITE: int
PROTECTED_DACL_SECURITY_INFORMATION: int
PROTECTED_SACL_SECURITY_INFORMATION: int
PolicyAccountDomainInformation: int
PolicyAuditEventsInformation: int
PolicyAuditFullQueryInformation: int
PolicyAuditFullSetInformation: int
PolicyAuditLogInformation: int
PolicyDefaultQuotaInformation: int
PolicyDnsDomainInformation: int
PolicyLsaServerRoleInformation: int
PolicyModificationInformation: int
PolicyNotifyAccountDomainInformation: int
PolicyNotifyAuditEventsInformation: int
PolicyNotifyDnsDomainInformation: int
PolicyNotifyDomainEfsInformation: int
PolicyNotifyDomainKerberosTicketInformation: int
PolicyNotifyMachineAccountPasswordInformation: int
PolicyNotifyServerRoleInformation: int
PolicyPdAccountInformation: int
PolicyPrimaryDomainInformation: int
PolicyReplicaSourceInformation: int
PolicyServerDisabled: int
PolicyServerEnabled: int
PolicyServerRoleBackup: int
PolicyServerRolePrimary: int
PyCredHandleType = _mod_builtins.PyCredHandle
PyCtxtHandleType = _mod_builtins.PyCtxtHandle
PySecBufferDescType = _mod_builtins.PySecBufferDesc
PySecBufferType = _mod_builtins.PySecBuffer
def QuerySecurityPackageInfo() -> typing.Any:
    ...

REVOKE_ACCESS: int
def RevertToSelf() -> typing.Any:
    ...

SACL_SECURITY_INFORMATION: int
SANDBOX_INERT: int
SDDL_REVISION_1: int
SECPKG_CRED_BOTH: int
SECPKG_CRED_INBOUND: int
SECPKG_CRED_OUTBOUND: int
SECPKG_FLAG_ACCEPT_WIN32_NAME: int
SECPKG_FLAG_CLIENT_ONLY: int
SECPKG_FLAG_CONNECTION: int
SECPKG_FLAG_DATAGRAM: int
SECPKG_FLAG_EXTENDED_ERROR: int
SECPKG_FLAG_IMPERSONATION: int
SECPKG_FLAG_INTEGRITY: int
SECPKG_FLAG_MULTI_REQUIRED: int
SECPKG_FLAG_PRIVACY: int
SECPKG_FLAG_STREAM: int
SECPKG_FLAG_TOKEN_ONLY: int
def SECURITY_ATTRIBUTES() -> typing.Any:
    ...

SECURITY_CREATOR_SID_AUTHORITY: int
def SECURITY_DESCRIPTOR() -> typing.Any:
    ...

SECURITY_LOCAL_SID_AUTHORITY: int
SECURITY_NON_UNIQUE_AUTHORITY: int
SECURITY_NT_AUTHORITY: int
SECURITY_NULL_SID_AUTHORITY: int
SECURITY_RESOURCE_MANAGER_AUTHORITY: int
SECURITY_WORLD_SID_AUTHORITY: int
SET_ACCESS: int
SET_AUDIT_FAILURE: int
SET_AUDIT_SUCCESS: int
SE_ASSIGNPRIMARYTOKEN_NAME: str
SE_AUDIT_NAME: str
SE_BACKUP_NAME: str
SE_BATCH_LOGON_NAME: str
SE_CHANGE_NOTIFY_NAME: str
SE_CREATE_GLOBAL_NAME: str
SE_CREATE_PAGEFILE_NAME: str
SE_CREATE_PERMANENT_NAME: str
SE_CREATE_SYMBOLIC_LINK_NAME: str
SE_CREATE_TOKEN_NAME: str
SE_DACL_AUTO_INHERITED: int
SE_DACL_DEFAULTED: int
SE_DACL_PRESENT: int
SE_DACL_PROTECTED: int
SE_DEBUG_NAME: str
SE_DENY_BATCH_LOGON_NAME: str
SE_DENY_INTERACTIVE_LOGON_NAME: str
SE_DENY_NETWORK_LOGON_NAME: str
SE_DENY_REMOTE_INTERACTIVE_LOGON_NAME: str
SE_DENY_SERVICE_LOGON_NAME: str
SE_DS_OBJECT: int
SE_DS_OBJECT_ALL: int
SE_ENABLE_DELEGATION_NAME: str
SE_FILE_OBJECT: int
SE_GROUP_DEFAULTED: int
SE_GROUP_ENABLED: int
SE_GROUP_ENABLED_BY_DEFAULT: int
SE_GROUP_INTEGRITY: int
SE_GROUP_INTEGRITY_ENABLED: int
SE_GROUP_LOGON_ID: int
SE_GROUP_MANDATORY: int
SE_GROUP_OWNER: int
SE_GROUP_RESOURCE: int
SE_GROUP_USE_FOR_DENY_ONLY: int
SE_IMPERSONATE_NAME: str
SE_INCREASE_QUOTA_NAME: str
SE_INC_BASE_PRIORITY_NAME: str
SE_INC_WORKING_SET_NAME: str
SE_INTERACTIVE_LOGON_NAME: str
SE_KERNEL_OBJECT: int
SE_LMSHARE: int
SE_LOAD_DRIVER_NAME: str
SE_LOCK_MEMORY_NAME: str
SE_MACHINE_ACCOUNT_NAME: str
SE_MANAGE_VOLUME_NAME: str
SE_NETWORK_LOGON_NAME: str
SE_OWNER_DEFAULTED: int
SE_PRINTER: int
SE_PRIVILEGE_ENABLED: int
SE_PRIVILEGE_ENABLED_BY_DEFAULT: int
SE_PRIVILEGE_REMOVED: int
SE_PRIVILEGE_USED_FOR_ACCESS: int
SE_PROF_SINGLE_PROCESS_NAME: str
SE_PROVIDER_DEFINED_OBJECT: int
SE_REGISTRY_KEY: int
SE_REGISTRY_WOW64_32KEY: int
SE_RELABEL_NAME: str
SE_REMOTE_INTERACTIVE_LOGON_NAME: str
SE_REMOTE_SHUTDOWN_NAME: str
SE_RESTORE_NAME: str
SE_SACL_AUTO_INHERITED: int
SE_SACL_DEFAULTED: int
SE_SACL_PRESENT: int
SE_SACL_PROTECTED: int
SE_SECURITY_NAME: str
SE_SELF_RELATIVE: int
SE_SERVICE: int
SE_SERVICE_LOGON_NAME: str
SE_SHUTDOWN_NAME: str
SE_SYNC_AGENT_NAME: str
SE_SYSTEMTIME_NAME: str
SE_SYSTEM_ENVIRONMENT_NAME: str
SE_SYSTEM_PROFILE_NAME: str
SE_TAKE_OWNERSHIP_NAME: str
SE_TCB_NAME: str
SE_TIME_ZONE_NAME: str
SE_TRUSTED_CREDMAN_ACCESS_NAME: str
SE_UNDOCK_NAME: str
SE_UNKNOWN_OBJECT_TYPE: int
SE_UNSOLICITED_INPUT_NAME: str
SE_WINDOW_OBJECT: int
SE_WMIGUID_OBJECT: int
def SID() -> typing.Any:
    ...

STYPE_DEVICE: int
STYPE_DISKTREE: int
STYPE_IPC: int
STYPE_PRINTQ: int
STYPE_SPECIAL: int
STYPE_TEMPORARY: int
SUB_CONTAINERS_AND_OBJECTS_INHERIT: int
SUB_CONTAINERS_ONLY_INHERIT: int
SUB_OBJECTS_ONLY_INHERIT: int
SUCCESSFUL_ACCESS_ACE_FLAG: int
SYSTEM_AUDIT_ACE_TYPE: int
SYSTEM_AUDIT_OBJECT_ACE_TYPE: int
SYSTEM_MANDATORY_LABEL_NO_EXECUTE_UP: int
SYSTEM_MANDATORY_LABEL_NO_READ_UP: int
SYSTEM_MANDATORY_LABEL_NO_WRITE_UP: int
SYSTEM_MANDATORY_LABEL_VALID_MASK: int
SecBufferDescType = _mod_builtins.PySecBufferDesc
SecBufferType = _mod_builtins.PySecBuffer
SecurityAnonymous: int
SecurityDelegation: int
SecurityIdentification: int
SecurityImpersonation: int
def SetFileSecurity() -> typing.Any:
    ...

def SetKernelObjectSecurity() -> typing.Any:
    ...

def SetNamedSecurityInfo() -> typing.Any:
    ...

def SetSecurityInfo() -> typing.Any:
    ...

def SetThreadToken() -> typing.Any:
    ...

def SetTokenInformation() -> typing.Any:
    ...

def SetUserObjectSecurity() -> typing.Any:
    ...

SidTypeAlias: int
SidTypeComputer: int
SidTypeDeletedAccount: int
SidTypeDomain: int
SidTypeGroup: int
SidTypeInvalid: int
SidTypeUnknown: int
SidTypeUser: int
SidTypeWellKnownGroup: int
TOKEN_ADJUST_DEFAULT: int
TOKEN_ADJUST_GROUPS: int
TOKEN_ADJUST_PRIVILEGES: int
TOKEN_ALL_ACCESS: int
TOKEN_ASSIGN_PRIMARY: int
TOKEN_DUPLICATE: int
TOKEN_EXECUTE: int
TOKEN_IMPERSONATE: int
TOKEN_MANDATORY_POLICY_NEW_PROCESS_MIN: int
TOKEN_MANDATORY_POLICY_NO_WRITE_UP: int
TOKEN_MANDATORY_POLICY_OFF: int
TOKEN_MANDATORY_POLICY_VALID_MASK: int
TOKEN_QUERY: int
TOKEN_QUERY_SOURCE: int
TOKEN_READ: int
TOKEN_WRITE: int
TRUSTEE_BAD_FORM: int
TRUSTEE_IS_ALIAS: int
TRUSTEE_IS_COMPUTER: int
TRUSTEE_IS_DELETED: int
TRUSTEE_IS_DOMAIN: int
TRUSTEE_IS_GROUP: int
TRUSTEE_IS_INVALID: int
TRUSTEE_IS_NAME: int
TRUSTEE_IS_OBJECTS_AND_NAME: int
TRUSTEE_IS_OBJECTS_AND_SID: int
TRUSTEE_IS_SID: int
TRUSTEE_IS_UNKNOWN: int
TRUSTEE_IS_USER: int
TRUSTEE_IS_WELL_KNOWN_GROUP: int
TokenAccessInformation: int
TokenAuditPolicy: int
TokenDefaultDacl: int
TokenElevation: int
TokenElevationType: int
TokenElevationTypeDefault: int
TokenElevationTypeFull: int
TokenElevationTypeLimited: int
TokenGroups: int
TokenGroupsAndPrivileges: int
TokenHasRestrictions: int
TokenImpersonation: int
TokenImpersonationLevel: int
TokenIntegrityLevel: int
TokenLinkedToken: int
TokenLogonSid: int
TokenMandatoryPolicy: int
TokenOrigin: int
TokenOwner: int
TokenPrimary: int
TokenPrimaryGroup: int
TokenPrivileges: int
TokenRestrictedSids: int
TokenSandBoxInert: int
TokenSessionId: int
TokenSessionReference: int
TokenSource: int
TokenStatistics: int
TokenType: int
TokenUIAccess: int
TokenUser: int
TokenVirtualizationAllowed: int
TokenVirtualizationEnabled: int
def TranslateName() -> typing.Any:
    ...

TrustedControllersInformation: int
TrustedDomainAuthInformation: int
TrustedDomainAuthInformationInternal: int
TrustedDomainFullInformation: int
TrustedDomainFullInformation2Internal: int
TrustedDomainFullInformationInternal: int
TrustedDomainInformationBasic: int
TrustedDomainInformationEx: int
TrustedDomainInformationEx2Internal: int
TrustedDomainNameInformation: int
TrustedPasswordInformation: int
TrustedPosixOffsetInformation: int
UNICODE: int
UNPROTECTED_DACL_SECURITY_INFORMATION: int
UNPROTECTED_SACL_SECURITY_INFORMATION: int
WinAccountAdministratorSid: int
WinAccountCertAdminsSid: int
WinAccountComputersSid: int
WinAccountControllersSid: int
WinAccountDomainAdminsSid: int
WinAccountDomainGuestsSid: int
WinAccountDomainUsersSid: int
WinAccountEnterpriseAdminsSid: int
WinAccountGuestSid: int
WinAccountKrbtgtSid: int
WinAccountPolicyAdminsSid: int
WinAccountRasAndIasServersSid: int
WinAccountReadonlyControllersSid: int
WinAccountSchemaAdminsSid: int
WinAnonymousSid: int
WinAuthenticatedUserSid: int
WinBatchSid: int
WinBuiltinAccountOperatorsSid: int
WinBuiltinAdministratorsSid: int
WinBuiltinAuthorizationAccessSid: int
WinBuiltinBackupOperatorsSid: int
WinBuiltinCryptoOperatorsSid: int
WinBuiltinDCOMUsersSid: int
WinBuiltinDomainSid: int
WinBuiltinEventLogReadersGroup: int
WinBuiltinGuestsSid: int
WinBuiltinIUsersSid: int
WinBuiltinIncomingForestTrustBuildersSid: int
WinBuiltinNetworkConfigurationOperatorsSid: int
WinBuiltinPerfLoggingUsersSid: int
WinBuiltinPerfMonitoringUsersSid: int
WinBuiltinPowerUsersSid: int
WinBuiltinPreWindows2000CompatibleAccessSid: int
WinBuiltinPrintOperatorsSid: int
WinBuiltinRemoteDesktopUsersSid: int
WinBuiltinReplicatorSid: int
WinBuiltinSystemOperatorsSid: int
WinBuiltinTerminalServerLicenseServersSid: int
WinBuiltinUsersSid: int
WinCacheablePrincipalsGroupSid: int
WinCreatorGroupServerSid: int
WinCreatorGroupSid: int
WinCreatorOwnerRightsSid: int
WinCreatorOwnerServerSid: int
WinCreatorOwnerSid: int
WinDialupSid: int
WinDigestAuthenticationSid: int
WinEnterpriseControllersSid: int
WinEnterpriseReadonlyControllersSid: int
WinHighLabelSid: int
WinIUserSid: int
WinInteractiveSid: int
WinLocalServiceSid: int
WinLocalSid: int
WinLocalSystemSid: int
WinLogonIdsSid: int
WinLowLabelSid: int
WinMediumLabelSid: int
WinNTLMAuthenticationSid: int
WinNetworkServiceSid: int
WinNetworkSid: int
WinNonCacheablePrincipalsGroupSid: int
WinNtAuthoritySid: int
WinNullSid: int
WinOtherOrganizationSid: int
WinProxySid: int
WinRemoteLogonIdSid: int
WinRestrictedCodeSid: int
WinSChannelAuthenticationSid: int
WinSelfSid: int
WinServiceSid: int
WinSystemLabelSid: int
WinTerminalServerSid: int
WinThisOrganizationSid: int
WinUntrustedLabelSid: int
WinWorldSid: int
WinWriteRestrictedCodeSid: int
__doc__: str
__file__: str
__name__: str
__package__: str
error = _mod_pywintypes.error
def __getattr__(name) -> typing.Any:
    ...

