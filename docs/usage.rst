.. _usage:

Usage
=====

Request
-------
The following example shows how to enable GPIO 15. When you run Geppetto in 
development mode the Authorization header redundant. Authentication has been
disabled in development mode.

::

    >>> import requests, json, base64
    >>> # Create Authorization header.
    >>> auth = {'Authorization': base64.b64encode('fcba99ca-3360-4683-a54d-1ce8ad1f20f3').encode('utf-8')}
    >>> # Create body of POST request.
    >>> data = json.dumps({'value': 1})
    >>> # Do POST request.
    >>> requests.post('http://localhost:5000/gpio/15/setpoint', headers=auth, data=data)
    <Response [200]>

Docs
----
If you want to build the documentation you've to get the `Diaoul Sphinx theme`_
. This Git repository has been added as submodule. Fetch the data:

::

    $ git submodule init
    $ git submodule update

The documenation can be build with:

:: 

    $ sphinx-build -aE -b html docs docs/_build

or:

::

    $ make -C docs html

.. _Diaoul Sphinx theme: https://github.com/Diaoul/diaoul-sphinx-thEmes
