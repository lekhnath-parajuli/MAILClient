#!.env/bin/python3

import webbrowser
from flask import Flask, request
from auth.authentication import Microsoft365

PORT = 8080
HOST = "localhost"


app = Flask(__name__)


client = Microsoft365()
authentication_request_uri = client.request_access_token_url()
webbrowser.open(authentication_request_uri, new=False)


@app.route('/microsoft365', methods=['GET'])
def microsoft365():
    '''
    here azure will pass the authentication code
    wiith the help of which we will get access_token
    '''
    authorization_code: str = request.args.get('code')
    print(authorization_code)
    res = client.get_token(authorization_code)
    print(res.keys())
    user: str = res.get('id_token_claims').get('preferred_username')
    token: str = res.get('access_token')
    print('----------------------------------------------------------------')
    print(token)
    # print(Oauth2Client.generate_oauth2_string(user, token))
    # client.oauth2_imap_login(user=user, access_token=token)
    # print(len(base64.b64encode(token.encode('ascii'))))
    print('----------------------------------------------------------------')
    client.oauth2_login(user, token)
    return 'microsoft365'


if __name__ == '__main__':
    app.run(host=HOST, port=PORT)
