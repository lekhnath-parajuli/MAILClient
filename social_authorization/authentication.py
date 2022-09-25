from dataclasses import dataclass
from typing import Optional
from msal import ConfidentialClientApplication


class AuthenticationProcessor:
    pass


class Oauth2Processor:
    pass


@dataclass
class Microsoft365:
    scopes: list[str]
    kwargs: Optional[dict] = None

    authority_url: str = 'https://login.microsoftonline.com/common/'
    client_id: str = '1ca437be-f627-497e-acc3-86586497f26a'
    client_secret_value: str = 'yhw8Q~ifB3zQd0d6Mi~FRnLOYWil0gHtbINlfbCL'

    def get_confidential_client_request_uri(self) -> str:
        '''
        this generates a uri for resource owner to give permission
        to the client to have access to there data
        '''
        self.client = ConfidentialClientApplication(
            client_id=self.client_id,
            client_credential=self.client_secret_value,
            authority=self.authority_url)
        uri = self.client.get_authorization_request_url(
            scopes=self.scopes,
            response_type='token')
        return uri
