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
