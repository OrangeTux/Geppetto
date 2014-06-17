[![Build Status](https://travis-ci.org/OrangeTux/Gepetto.svg?branch=develop)](https://travis-ci.org/OrangeTux/Gepetto)
[![Coverage Status](https://coveralls.io/repos/OrangeTux/Gepetto/badge.png)](https://coveralls.io/r/OrangeTux/Gepetto)
Gepetto
=======
Gepetto is a home automation server. It's written for the Raspberry Pi but with
some small modification you should be able to run it on other devices with GPIO
pins. Gepetto provides a REST API which let you control the GPIO pins of your
Raspberry Pi. Apps can be build on top of this API in order to control the GPIO
pins easily.

Installation
------------
Python runs with Python 2.7, 3.3 and 3.4. Create a virtualenv and install
depencies:

    $ pyvenv-3.4 .env
    $ source .env/bin/activate
    $ pip install -r requirements.txt

When installing Gepetto on your Raspberry Pi install ARM requirements also:

    $ pip install -r arm_requirements.txt

Create a database database and generate an API key:
    
    $ pynt setup_db
    [ build.py - Starting task "setup_db" ]
    [ build.py - Completed task "setup_db" ]
    $ pynt create_api_key
    [ build.py - Starting task "create_api_key" ]
    An API key has been added to database: d0d41996-64d2-4171-a436-b295cb657368
    [ build.py - Completed task "create_api_key" ]

Running
-------
In order to start the webserver in development mode, set environment variable 
`GEPETTO_ENV` to `dev`.
    
    $ export GEPETTO_ENV=dev
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
