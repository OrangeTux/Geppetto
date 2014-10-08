import os
from base64 import b64encode

try:
    from importlib import reload
except ImportError:
    try:
        from imp import reload
    except ImportError:
        pass

import app


def test_app():
    """ Test configuration of app in different environment. """
    assert app.app.debug is False

    os.environ['GEPPETTO_ENV'] = 'dev'
    reload(app)
    assert app.app.debug is True
    os.environ['GEPPETTO_ENV'] = 'test'


def test_load_user_from_request(client, auth_header):
    """ Test succesful authentication. """
    with client as cl:
        res = cl.get('/test_authentication',
                     headers=auth_header)

        assert res.status_code == 200


def test_load_user_from_request_with_non_existing_api_key(client):
    """ Test authentication with a non existing api key. """
    with client as cl:
        res = cl.get('/test_authentication',
                     headers={'Authorization': b64encode(b'invalid')})
        assert res.status_code == 401


def test_load_user_from_request_with_invalid_api_key(client, user):
    """ Test authentication with a invalid existing api key. """
    with client as cl:
        # Should raise UnicodeError.
        res = cl.get('/test_authentication',
                     headers={'Authorization': user.api_key})
        assert res.status_code == 401

        # Should raise TypeError
        res = cl.get('/test_authentication',
                     headers={'Authorization': 'invalid'})

        assert res.status_code == 401


def test_access_control_headers(client, auth_header):
    """ Test if correct Access-Control-* headers are returned. """
    with client as cl:
        res = cl.get('/test_authentication',
                     headers=auth_header)

        assert res.headers.get('Access-Control-Allow-Headers') ==\
            'Authorization, Content-Type'
        assert res.headers.get('Access-Control-Allow-Origin') == '*'
