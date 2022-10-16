from msal import ConfidentialClientApplication
from imapclient import IMAPClient
from .config import config


class Microsoft365:
    def __init__(self) -> None:
        self.client_id = config.MICROSOFT.CLIENT_ID
        self.client_secret_value = config.MICROSOFT.CLIENT_SECRET_VALUE
        self.scopes = config.MICROSOFT.SCOPES
        self.redirect_url = config.MICROSOFT.REDIRECT_URL
        self.authority = config.MICROSOFT.AUTHORITY
        self.imap_server = config.MICROSOFT.IMAP_SERVER
        self.imap_port = config.MICROSOFT.IMAP_PORT

    def request_access_token_url(self):
        self.client = ConfidentialClientApplication(
            client_id=self.client_id,
            client_credential=self.client_secret_value,
            authority=self.authority)
        url = self.client.initiate_auth_code_flow(
            scopes=self.scopes,
            redirect_uri=self.redirect_url)
        return url

    def get_token(self, auth_code_flow: dict, auth_response: dict):
        token = self.client.acquire_token_by_auth_code_flow(
            auth_code_flow=auth_code_flow,
            auth_response=auth_response,
            scopes=self.scopes)
        return token

    def oauth2_login(self, user, token):
        with IMAPClient(self.imap_server) as server:
            server.oauth2_login(user, token)
