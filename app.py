#!.env/bin/python

import webbrowser
from flask import Flask, request
from auth.authentication import Microsoft365
import base64


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
    res = client.get_token(request.args.get('code'))  # type: ignore
    print('----------------------------------------------------------------')
    token = res.get('access_token')
    print(len(base64.b64encode(token.encode('ascii'))))
    print('----------------------------------------------------------------')
    return 'microsoft365'


if __name__ == '__main__':
    app.run(host=HOST, port=PORT)
