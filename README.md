[![Build Status](https://travis-ci.org/OrangeTux/Geppetto.svg?branch=develop)](https://travis-ci.org/OrangeTux/Geppetto)
[![Coverage Status](https://img.shields.io/coveralls/OrangeTux/Geppetto.svg)](https://coveralls.io/r/OrangeTux/Geppetto)
[![Code Health](https://landscape.io/github/OrangeTux/Geppetto/master/landscape.png)](https://landscape.io/github/OrangeTux/Geppetto/master)
Geppetto
=======
Geppetto exposes the GPIO pins of the Raspberry Pi using a HTTP API. Geppetto
works with Python 2.7, 3.3 and 3.4.

It's easy to set a GPIO either high with curl:

    $ curl -H "Content-Type: application/json" -d '{"value": 1}' http://geppet.to/gpio/1/setpoint
    
Or in Python:

    >>> import requests, json
    >>> data = {'value': 1}
    >>> header = {'Content-Type': 'application/json'}
    >>> request.post('http://geppet.to/gpio/1/setpoint', data=json.dumps(data), headers=header}
    Response[200]

Full documentation is available on [RTD][1].

[1]:http://geppetto-server.readthedocs.org/en/develop/
