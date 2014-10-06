import os

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
                     headers={'Authorization': 'invalid'})
        assert res.status_code == 401


def test_load_user_from_request_with_invalid_api_key(client, user):
    """ Test authentication with a non existing api key. """
    with client as cl:
        res = cl.get('/test_authentication',
                     headers={'Authorization': user.api_key})
        assert res.status_code == 401
