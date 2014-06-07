import os
from flask import Flask

app = Flask(__name__)

if 'GEPETTO_ENV' in os.environ and os.environ['GEPETTO_ENV'] == 'dev':
    app.debug = True
