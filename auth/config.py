class Microsoft365:
    CLIENT_ID = '1ca437be-f627-497e-acc3-86586497f26a'
    CLIENT_SECRET_VALUE = '1bX8Q~TIrc8kEE1KK7cguZl6abHqXqNwrXSG2cUP'
    TANENT_ID = 'e01c2ead-9e0c-4ba9-abc5-65637df647a9'
    REDIRECT_URL = 'http://localhost:8080/microsoft365'
    AUTHORITY = f"https://login.microsoftonline.com/{TANENT_ID}"
    SCOPES = ['IMAP.AccessAsUser.All']


class Config:
    TLS_IMAP_PORT = 993
    IMAP_SERVER = 'imap-mail.outlook.com'
    USERNAME = 'lekhnathparajuli4@gmail.com'
    PASSWORD = 'wbmoskptxzlybisw'
    MICROSOFT = Microsoft365


config = Config()
