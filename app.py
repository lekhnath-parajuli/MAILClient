#!.env/bin/python3

import webbrowser
from flask import Flask, request
from auth.authentication import Microsoft365
from auth.oauth2 import Oauth2Client

PORT = 8080
HOST = "localhost"


app = Flask(__name__)


client = Microsoft365()
auth_code_flow = client.request_access_token_url()
uri: str = str(auth_code_flow.get('auth_uri'))
webbrowser.open(uri, new=False)


@app.route('/microsoft365', methods=['GET'])
def microsoft365():
    '''
    here azure will pass the authentication code
    wiith the help of which we will get access_token
    '''
    auth_response: dict = request.args
    response = client.get_token(
        auth_code_flow=auth_code_flow,
        auth_response=auth_response
    )
    user: str = response.get('id_token_claims').get('preferred_username')
    access_token: str = response.get('access_token')
    print('----------------------------------------------------------------')
    print(Oauth2Client.generate_oauth2_string(user, access_token))
    print('----------------------------------------------------------------')
    client.oauth2_login(user, access_token)
    return 'microsoft365'


if __name__ == '__main__':
    app.run(host=HOST, port=PORT)
