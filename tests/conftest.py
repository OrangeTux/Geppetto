import os

os.environ['GEPETTO_ENV'] = 'test'

import pytest
import sqlite3
from uuid import uuid4
import base64

from app import app as application
from app import db_path


def setup_db(con):
    """ Create testing database. """
    with con:
        con.execute('CREATE TABLE api_key (key text)')


@pytest.fixture
def db_con():
    """ Returns a database connection. """
    con = sqlite3.connect(db_path)
    setup_db(con)

    return con


@pytest.fixture
def api_key(db_con):
    """ Add API key to db and return the key. """
    key = str(uuid4()).encode('utf-8')

    with db_con:
        db_con.execute("INSERT INTO api_key(key) VALUES (?)", (key,))

    return key


@pytest.fixture
def auth_header(api_key):
    """ Return Authorization header. """
    return {'Authorization': base64.b64encode(api_key)}


@pytest.fixture
def client():
    """ Return test instance of app. """
    return application.test_client()
