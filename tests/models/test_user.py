from app import db
from app.models import User


def test_repr():
    """ Test __repr__. """
    u = User(api_key=3)

    assert u.__repr__() == '<User None, api_key: 3>'

    db.session.add(u)
    db.session.commit()

    assert u.__repr__() == '<User %d, api_key: 3>' % u.id
