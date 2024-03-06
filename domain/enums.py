from enum import Enum


class CRMName(Enum):
    HUBSPOT = "hubspot"
    ZAPIER = "zapier"
    PIPEDRIVE = "pipedrive"
    SLACK = "slack"


class GrantType(Enum):
    AUTHORIZATION_CODE = "authorization_code"
    REFRESH_TOKEN = "refresh_token"  # nosec

    class Config:
        use_enum_value = True


class TokenType(Enum):
    BEARER = "Bearer"


class AuthenticationType(Enum):
    OAUTH = "oauth"  # nosec
    ACCESS_TOKEN = "access_token"  # nosec
