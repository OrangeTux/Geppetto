Quickstart
==========

.. note::

    It is not safe to start Geppetto like this in a production environment.
    When running in development mode API authentication has been disabled.
    
Inside your virtualenv set the environmnent `GEPPETTO_ENV` and start the 
server:

::

    $ export GEPETTO_ENV=dev
    $ .env/bin/python server.py
    * Running on http://127.0.0.1:5000/
    * Restarting with reloader

When the server is running do a POST request, for example from the Python 
interpreter. Use the API key generated earlier:

See :ref:`Usage` how to interact with API and how to toggle GPIO pins.
