#!/usr/bin/env python
import os
import sys

_curpath = os.path.dirname(os.path.abspath(__name__))
sys.path.append(_curpath)

from pynt import task
from uuid import uuid4

from app import db
from app.models import User


@task()
def setup_db():
    """ Setup database. """
    db.create_all()


@task()
def create_user():
    """ Create API key and add it to database. """
    key = str(uuid4())
    u = User(api_key=key)
    db.session.add(u)
    db.session.commit()

    print('User %s has been created.' % u)
