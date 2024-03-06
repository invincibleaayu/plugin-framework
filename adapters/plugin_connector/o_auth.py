import httpx
import urllib.parse
from domain.enums import CRMName, TokenType, GrantType
from domain.schema import AccessTokenResponseSchema
import yaml


class CRMConnector:
    def __init__(
        self,
        crm_name: CRMName,
    ):
        self.crm_name = crm_name

    def load_config(self):
        with open(f"/plugin_config_path/{self.crm_name}.yaml", "r") as file:
            config_data = yaml.safe_load(file)
        self.base_oauth_url = config_data.get(self.crm_name).get("base_oauth_url", "")
        self.token_endpoint = config_data.get(self.crm_name).get("token_endpoint", "")
        self.oauth_scopes = config_data.get(self.crm_name).get("oauth_scopes", ())
        self.client_id = config_data.get(self.crm_name).get("client_id", "")
        self.client_secret = config_data.get(self.crm_name).get("client_secret", "")
        self.redirect_uri = config_data.get(self.crm_name).get("redirect_uri", "")
        self.user_info_url = config_data.get(self.crm_name).get("user_info_url", "")
        self.auth_url = config_data.get(self.crm_name).get("auth_url", "")
        self.query_params = config_data.get(self.crm_name).get("query_params")
        self.revoke_url = config_data.get(self.crm_name).get("revoke_url")

    @property
    def token_url(self) -> str:
        return f"{self.base_oauth_url}/{self.token_endpoint}"

    async def get_auth_url(self) -> str:
        params = urllib.parse.urlencode(
            self.query_params,
            safe="",
            quote_via=urllib.parse.quote,
        )

        return f"{self.auth_url}?{params}"

    async def get_access_token(self, code: str) -> AccessTokenResponseSchema:
        with httpx.Client() as client:
            response = client.post(
                self.token_url,
                data={
                    "code": code,
                    "client_id": self.client_id,
                    "client_secret": self.client_secret,
                    "redirect_uri": self.redirect_uri,
                    "grant_type": str(GrantType.AUTHORIZATION_CODE.value),
                },
            )
        json_data = response.json()
        return AccessTokenResponseSchema(
            access_token=json_data.get("access_token"),
            refresh_token=json_data.get("refresh_token"),
            expires_in=json_data.get("expires_in"),
            token_type=str(TokenType(json_data.get("token_type").title()).value),
        )
