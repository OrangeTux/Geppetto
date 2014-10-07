import os

os.environ['GEPPETTO_ENV'] = 'test'

import pytest
from base64 import b64encode

from app import app as application
from app import db
from app.models import User


@pytest.fixture(scope='module', autouse=True)
def setup_db():
    db.create_all()


@pytest.fixture(scope='function', autouse=True)
def patch(monkeypatch, tmpdir):
    """ Monkey patch some functions of quick2wire module. """
    monkeypatch.setattr('quick2wire.gpio.gpio_admin',
                        lambda subcommand, pin, pull=None: None)

    def mock_pin_path(self, filename):
        f = tmpdir.join(filename)
        f.write(0)
        return f.strpath

    monkeypatch.setattr('quick2wire.gpio.Pin._pin_path', mock_pin_path)


@pytest.fixture
def user():
    """ Add API key to db and return the key. """
    u = User(api_key='c7dc072d-6c5d-4b16-8189-6f95147275e5')
    db.session.add(u)
    db.session.commit()

    return u


@pytest.fixture
def auth_header(user):
    """ Return Authorization header. """
    return {'Authorization': b64encode(user.api_key.encode('utf-8'))}


@pytest.fixture
def client():
    """ Return test instance of app. """
    return application.test_client()
