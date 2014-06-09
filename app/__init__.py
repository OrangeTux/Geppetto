import os
from flask import Flask

from app.api import gpio

app = Flask(__name__)
app.register_blueprint(gpio, url_prefix='/gpio')

if 'GEPETTO_ENV' in os.environ and os.environ['GEPETTO_ENV'] == 'dev':
    app.debug = True
