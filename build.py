#!/usr/bin/env python
import os
import sqlite3
from pynt import task
from uuid import uuid4

_cur_path = os.path.dirname(os.path.abspath(__name__))
db_path = os.path.join(_cur_path, 'data', 'gepetto.db')


@task()
def setup_db():
    """ Setup Sqlite database. """
    con = sqlite3.connect(db_path)

    with con:
        con.execute('CREATE TABLE api_keys (key text)')


@task()
def create_api_key():
    """ Create API key and add it to database. """
    con = sqlite3.connect(db_path)
    key = uuid4()

    with con:
        con.execute("INSERT INTO api_keys(key) VALUES (?)", (str(key),))

    print('An API key has been added to database: %s' % key)
