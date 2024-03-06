from pydantic import BaseModel

from enums import TokenType


class AccessTokenResponseSchema(BaseModel):
    access_token: str
    refresh_token: str
    expires_in: int
    token_type: TokenType = TokenType.BEARER

    class Config:
        use_enum_values = True
