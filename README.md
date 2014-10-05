[![Build Status](https://travis-ci.org/OrangeTux/Geppetto.svg?branch=develop)](https://travis-ci.org/OrangeTux/Geppetto)
[![Coverage Status](https://img.shields.io/coveralls/OrangeTux/Geppetto.svg)](https://coveralls.io/r/OrangeTux/Geppetto)
Geppetto
=======
Geppetto is a home automation server. It's written for the Raspberry Pi but with
some small modification you should be able to run it on other devices with GPIO
pins. Geppetto provides a REST API which let you control the GPIO pins of your
Raspberry Pi. Apps can be build on top of this API in order to control the GPIO
pins easily.

Full documentation is available on [RTD][6].

Installation
------------
Geppetto has been tested under Python 3.3 and Python 3.4. Geppetto uses 
Quick2Wire's [gpio-admin][3] and its [Python wrapper][4]. The documentation of
this wrapper says that it works with Python 3, but my experience is that it
works well with Python 2.7 too.

    $ pyvenv-3.4 .env
    $ source .env/bin/activate
    $ pip install -r requirements.txt

Install GPIO ADMIN by following the [installation instructions][5].

Create a database database and generate an API key:
    
    $ pynt setup_db
    [ build.py - Starting task "setup_db" ]
    [ build.py - Completed task "setup_db" ]
    $ pynt create_user
    [ build.py - Starting task "create_user" ]
    User <User 1, api_key: b'fcba99ca-3360-4683-a54d-1ce8ad1f20f3'> has been created.
    [ build.py - Completed task "create_user" ]


Running
-------
In order to start the webserver in development mode, set environment variable 
`GEPPETTO_ENV` to `dev`.
    
    $ export GEPPETTO_ENV=dev
    $ ./server.py

Tests
-----
Tests are written using [py.test][1]. Run the test suite with:

    $ py.test tests/

Documentation
-------------
The documentation is powered by [Sphinx][2] and can be build with:

    $ sphinx-build -aE -b html docs docs/_build

or with
    
    $ make -C docs html

[1]:http://pytest.org
[2]:http://sphinx-doc.org/
[3]:https://github.com/quick2wire/quick2wire-gpio-admin
[4]:https://github.com/quick2wire/quick2wire-python-api
[5]:https://github.com/quick2wire/quick2wire-gpio-admin#installation
[6]:http://geppetto-server.readthedocs.org/en/develop/
