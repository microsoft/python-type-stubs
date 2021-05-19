# Python: 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)]
# Library: win32cred, version: unspecified
# Module: win32cred, version: unspecified

'Interface to credentials management functions.'

import typing
import builtins as _mod_builtins

CREDUI_FLAGS_ALWAYS_SHOW_UI: int
CREDUI_FLAGS_COMPLETE_USERNAME: int
CREDUI_FLAGS_DO_NOT_PERSIST: int
CREDUI_FLAGS_EXCLUDE_CERTIFICATES: int
CREDUI_FLAGS_EXPECT_CONFIRMATION: int
CREDUI_FLAGS_GENERIC_CREDENTIALS: int
CREDUI_FLAGS_INCORRECT_PASSWORD: int
CREDUI_FLAGS_KEEP_USERNAME: int
CREDUI_FLAGS_PASSWORD_ONLY_OK: int
CREDUI_FLAGS_PERSIST: int
CREDUI_FLAGS_PROMPT_VALID: int
CREDUI_FLAGS_REQUEST_ADMINISTRATOR: int
CREDUI_FLAGS_REQUIRE_CERTIFICATE: int
CREDUI_FLAGS_REQUIRE_SMARTCARD: int
CREDUI_FLAGS_SERVER_CREDENTIAL: int
CREDUI_FLAGS_SHOW_SAVE_CHECK_BOX: int
CREDUI_FLAGS_USERNAME_TARGET_CREDENTIALS: int
CREDUI_FLAGS_VALIDATE_USERNAME: int
CREDUI_MAX_CAPTION_LENGTH: int
CREDUI_MAX_DOMAIN_TARGET_LENGTH: int
CREDUI_MAX_GENERIC_TARGET_LENGTH: int
CREDUI_MAX_MESSAGE_LENGTH: int
CREDUI_MAX_PASSWORD_LENGTH: int
CREDUI_MAX_USERNAME_LENGTH: int
CRED_ALLOW_NAME_RESOLUTION: int
CRED_CACHE_TARGET_INFORMATION: int
CRED_FLAGS_OWF_CRED_BLOB: int
CRED_FLAGS_PASSWORD_FOR_CERT: int
CRED_FLAGS_PROMPT_NOW: int
CRED_FLAGS_USERNAME_TARGET: int
CRED_FLAGS_VALID_FLAGS: int
CRED_MAX_ATTRIBUTES: int
CRED_MAX_DOMAIN_TARGET_NAME_LENGTH: int
CRED_MAX_GENERIC_TARGET_NAME_LENGTH: int
CRED_MAX_STRING_LENGTH: int
CRED_MAX_USERNAME_LENGTH: int
CRED_MAX_VALUE_SIZE: int
CRED_PERSIST_ENTERPRISE: int
CRED_PERSIST_LOCAL_MACHINE: int
CRED_PERSIST_NONE: int
CRED_PERSIST_SESSION: int
CRED_PRESERVE_CREDENTIAL_BLOB: int
CRED_TI_CREATE_EXPLICIT_CRED: int
CRED_TI_DOMAIN_FORMAT_UNKNOWN: int
CRED_TI_ONLY_PASSWORD_REQUIRED: int
CRED_TI_SERVER_FORMAT_UNKNOWN: int
CRED_TI_USERNAME_TARGET: int
CRED_TI_VALID_FLAGS: int
CRED_TI_WORKGROUP_MEMBER: int
CRED_TYPE_DOMAIN_CERTIFICATE: int
CRED_TYPE_DOMAIN_PASSWORD: int
CRED_TYPE_DOMAIN_VISIBLE_PASSWORD: int
CRED_TYPE_GENERIC: int
CertCredential: int
def CredDelete() -> typing.Any:
    'Deletes a stored credential'
    ...

def CredEnumerate() -> typing.Any:
    'Lists stored credentials for current logon session'
    ...

def CredGetTargetInfo() -> typing.Any:
    'Determines type and location of credential target'
    ...

def CredIsMarshaledCredential() -> typing.Any:
    'Checks if a string matches the form of a marshaled credential'
    ...

def CredMarshalCredential() -> typing.Any:
    'Marshals a credential into a unicode string'
    ...

def CredRead() -> typing.Any:
    'Retrieves a stored credential'
    ...

def CredReadDomainCredentials() -> typing.Any:
    "Retrieves a user's credentials for a domain or server"
    ...

def CredRename() -> typing.Any:
    'Changes the target name of stored credentials'
    ...

def CredUICmdLinePromptForCredentials() -> typing.Any:
    'Prompt for username/passwd from a console app'
    ...

def CredUIConfirmCredentials() -> typing.Any:
    'Confirms whether credentials entered by user are valid or not'
    ...

def CredUIParseUserName() -> typing.Any:
    'Parses a full username into domain and username'
    ...

def CredUIPromptForCredentials() -> typing.Any:
    'Initiates dialog to request user credentials'
    ...

def CredUIReadSSOCredW() -> typing.Any:
    'Retrieves single sign on username'
    ...

def CredUIStoreSSOCredW() -> typing.Any:
    'Creates a single sign on credential'
    ...

def CredUnmarshalCredential() -> typing.Any:
    'Unmarshals credentials formatted using <om win32cred.CredMarshalCredential>'
    ...

def CredWrite() -> typing.Any:
    'Creates or updates a stored credential'
    ...

def CredWriteDomainCredentials() -> typing.Any:
    'Creates or updates credential for a domain or server'
    ...

UsernameTargetCredential: int
__doc__: str
__file__: str
__name__: str
__package__: str
def __getattr__(name) -> typing.Any:
    ...

