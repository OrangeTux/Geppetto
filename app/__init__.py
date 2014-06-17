import os
import sqlite3
import base64
from flask import Flask
from flask.ext.login import LoginManager

from app.api import gpio

_cur_path = os.path.dirname(os.path.abspath(__name__))
db_path = os.path.join(_cur_path, 'data', 'gepetto.db')

app = Flask(__name__)
app.register_blueprint(gpio, url_prefix='/gpio')

login_manager = LoginManager()
login_manager.init_app(app)

if 'GEPETTO_ENV' in os.environ and os.environ['GEPETTO_ENV'] == 'dev':
    app.debug = True


@login_manager.request_loader
def login(request):
    """ Grant user access to API or not.

    :param request: A Request instance.

    """
    con = sqlite3.connect(db_path)

    key = request.headers.get('Authorization')
    if key:
        key = key.replace('Basic', '', 1)
        try:
            key = base64.base64decode(key)
        except TypeError:
            pass

        with con:
            con.execute('SELECT key FROM api_keys WHERE key = (?)', (key,))
            key = con.fetchone()

            if key:
                return key

    return None
