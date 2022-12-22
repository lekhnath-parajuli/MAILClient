import yaml
from pathlib import Path


credentials = yaml.safe_load(open(f"{Path(__file__).parent.parent}/credentials.yaml", "r"))


class Microsoft365:
    CLIENT_ID = credentials.get('CLIENT_ID')
    CLIENT_SECRET_VALUE = credentials.get('CLIENT_SECRET_VALUE')
    TENANT_ID = credentials.get('TENANT_ID')
    REDIRECT_URL = 'http://localhost:8080/microsoft365'
    AUTHORITY = f"https://login.microsoftonline.com/{TENANT_ID}"
    SCOPES = ['IMAP.AccessAsUser.All', 'SMTP.Send']
    IMAP_SERVER = 'outlook.office365.com'
    IMAP_PORT = 993


class Config:
    TLS_IMAP_PORT = 993
    IMAP_SERVER = 'imap-mail.outlook.com'
    MICROSOFT = Microsoft365


config = Config()
