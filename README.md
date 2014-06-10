Gepetto
=======
Gepetto is a home automation server. It's written for the Raspberry Pi but with
some small modification you should be able to run it on other devices with GPIO
pins. Gepetto provides a REST API which let you control the GPIO pins of your
Raspberry Pi. Apps can be build on top of this API in order to control the GPIO
pins easily.

Installation
------------
Create a Python 3.4 virtualenv and install dependencies:

    $ pyvenv-3.4 .env
    $ source .env/bin/activate
    $ pip install -r requirements

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
