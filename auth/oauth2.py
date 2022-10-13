import base64


class Oauth2Client:
    @classmethod
    def generate_oauth2_string(self,
                               username: str,
                               access_token: str) -> bytes:
        oauth2_string: bytes = base64.b64encode(
            f"user={username}%x01auth=Bearer {access_token}%x01%x01".encode())
        return oauth2_string
