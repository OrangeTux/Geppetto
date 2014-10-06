import os
import base64
from flask import Flask
from flask.ext.login import LoginManager
from flask.ext.sqlalchemy import SQLAlchemy

from app.api import gpio

_cur_path = os.path.dirname(os.path.abspath(__name__))

app = Flask(__name__)
app.secret_key = os.urandom(24)

app.register_blueprint(gpio, url_prefix='/gpio')
app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'sqlite:///%s/data/geppettov.db' % _cur_path

if 'GEPPETTO_ENV' in os.environ and os.environ['GEPPETTO_ENV'] == 'dev':
    app.config.update(
        DEBUG=True,
        LOGIN_DISABLED=True,
        TESTING=True,
        SQLALCHEMY_DATABASE_URI='sqlite:///%s/data/geppetto_dev.db' % _cur_path
    )

if 'GEPPETTO_ENV' in os.environ and os.environ['GEPPETTO_ENV'] == 'test':
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'

login_manager = LoginManager()
login_manager.init_app(app)

db = SQLAlchemy(app)

from app.models import User


@login_manager.request_loader
def load_user_from_request(request):
    """ Grant user access to API or not.

    :param request: A Request instance.
    :return: User instance or None.

    """
    key = request.headers.get('Authorization')
    if key:
        key = key.replace('Basic ', '', 1)
        try:
            key = base64.b64decode(key)
        except TypeError:
            pass

        user = User.query.filter_by(api_key=key).first()
        if user:
            return user

    return None
