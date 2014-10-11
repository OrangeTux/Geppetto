import os
import sys

_cur_path = os.path.dirname(os.path.abspath(__name__))
sys.path.append(os.path.join(_cur_path, '../', 'conf'))

import base64
import binascii
from flask import Flask, Response
from flask.ext.login import LoginManager, login_required
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.cors import CORS

app = Flask(__name__)
app.config.from_object('conf.default')

login_manager = LoginManager()
login_manager.init_app(app)

db = SQLAlchemy(app)
CORS(app, headers=['Content-Type', 'Authorization'])

from app.api import gpio
app.register_blueprint(gpio, url_prefix='/gpio')

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
        except (TypeError, binascii.Error):
            return None

        try:
            user = User.query.filter_by(api_key=key.decode('utf-8')).first()
        except UnicodeError:
            return None

        if user:
            return user

    return None


@app.route('/test_authentication')
@login_required
def test_authentication():
    """ Endpoint to test authentication. """
    return Response(status=200)
