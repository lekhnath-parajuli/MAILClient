#!.env/bin/python3

import webbrowser
import requests
from flask import Flask, request as req
from auth.authentication import Microsoft365

PORT = 8080
HOST = "localhost"


app = Flask(__name__)


client = Microsoft365()
auth_code_flow = client.request_access_token_url()
uri = '''https://login.microsoftonline.com/e01c2ead-9e0c-4ba9-abc5-65637df647a9/oauth2/authorize?
response_type=code
&client_id=5baa7bc4-a6e8-4d9a-a3ef-4598c3612b60
&redirect_uri=http://localhost:8080/microsoft365
&state=IezHVrWJlsSqbRXg
&scope=https://outlook.office.com/IMAP.AccessAsUser.All'''
webbrowser.open(uri, new=False)


@app.route('/microsoft365', methods=['GET'])
def microsoft365():
    '''
    here azure will pass the authentication code
    wiith the help of which we will get access_token
    '''
    auth_response: dict = req.args
    url = "https://login.microsoftonline.com/{tenant}/oauth2/v2.0/token".format(tenant="e01c2ead-9e0c-4ba9-abc5-65637df647a9")
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data = {
        "client_id": "5baa7bc4-a6e8-4d9a-a3ef-4598c3612b60",
        "client_secret": "Rbz8Q~Sf-nj0D78YcXW43yACjssRivrs.SkTAbi~",
        "grant_type": "authorization_code",
        "code": auth_response.get("code"),
        "redirect_uri": "http://localhost:8080/microsoft365",
        "scope": "https://outlook.office.com/IMAP.AccessAsUser.All"
    }
    response = requests.post(url, headers=headers, data=data)
    print(response.json())
    return 'microsoft365'


if __name__ == '__main__':
    app.run(host=HOST, port=PORT)