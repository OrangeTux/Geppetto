from flask.ext.login import UserMixin

from app import db


class User(db.Model, UserMixin):
    """ User model, used for authenticating with API. """
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    api_key = db.Column(db.String(50))

    def __repr__(self):
        """ Return string representation of instance.

        :return: String.

        """
        return '<User %s, api_key: %s>' %\
            (self.id if hasattr(self, 'id') else None, self.api_key)
