import os

_cur_path = os.path.dirname(os.path.abspath(__name__))

# General Flask configuration.
DEBUG = False
TESTING = False
LOGIN_DISABLED = False
SECRET_KEY = '?\xbf,\xb4\x8d\xa3"<\x9c\xb0@\x0f5\xab,w\xee\x8d$0\x13\x8b83'

# SQLAlchemy specific configuration.
SQLALCHEMY_DATBASE_URI = 'sqlite:///%s/data/geppettov.db' % _cur_path

# Geppetto specific configuration.
# Use mocks when GPIO are not available on system.
MOCK_PINS = False
