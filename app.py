#!.env/bin/python

import webbrowser
from flask import Flask, request
from social_authorization.authentication import Microsoft365


SCOPES = ['IMAP.AccessAsUser.All']
PORT = 8080
HOST = "localhost"


app = Flask(__name__)


client = Microsoft365(scopes=SCOPES)
authentication_request_uri = client.get_confidential_client_request_uri()
webbrowser.open(authentication_request_uri, new=False)


@app.route('/microsoft365', methods=['GET'])
def microsoft365():
    '''
    to get the information register http://localhost:8080/microsoft365
    in azure as a redirect url  so azure will call this url with the
    information you asked for
    '''
    # access_token is not comming as parameter insted its comming as
    # #access_token like a page jumper so for now you can only see
    # access_token in browser url after azure redirect you to the
    # http://localhost:8080/microsoft365 page
    print(request.url)
    return 'microsoft365'


if __name__ == '__main__':
    app.run(host=HOST, port=PORT)
