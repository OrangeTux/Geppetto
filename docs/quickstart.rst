Quickstart
==========

.. note::

     Do not start Geppetto like this in a production environment! Running
     Geppetto as root is dangerous!
    
Inside your virtualenv set the environmnent `GEPPETTO_ENV` and start the 
server:

::

    $ export GEPETTO_ENV=dev
    $ .env/bin/python server.py
    * Running on http://127.0.0.1:5000/
    * Restarting with reloader

Now you interact with the API on 127.0.0.1:5000. See :ref:`Usage` how 
to use the API and how to toggle GPIO pins.
