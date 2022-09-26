from dataclasses import dataclass
from msal import ConfidentialClientApplication

from .config import config

@dataclass
class Microsoft365:
    def __init__(self) -> None:
        self.client_id = config.MICROSOFT.CLIENT_ID
        self.client_secret_value = config.MICROSOFT.CLIENT_SECRET_VALUE
        self.scopes = config.MICROSOFT.SCOPES
        self.redirect_url = config.MICROSOFT.REDIRECT_URL
        self.authority = config.MICROSOFT.AUTHORITY

    def request_access_token_url(self):
        self.client = ConfidentialClientApplication(
            client_id=self.client_id,
            client_credential=self.client_secret_value,
            authority=self.authority)
        url = self.client.get_authorization_request_url(
            scopes=self.scopes,
            redirect_uri=self.redirect_url)
        return url

    def get_token(self, code: str):
        token = self.client.acquire_token_by_authorization_code(
            code=code,
            scopes=self.scopes,
            redirect_uri=self.redirect_url)
        return token
