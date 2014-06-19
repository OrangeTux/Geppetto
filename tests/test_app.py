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

    os.environ['GEPETTO_ENV'] = 'dev'
    reload(app)
    assert app.app.debug is True


def test_login(api_key, db_con):
    """ Test login function. """
    pass
