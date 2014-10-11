Configuration
=============
Gepppetto has a default configuration which can be found in in 
`conf/default.py`. 

.. literalinclude:: ../conf/default.py

If you want to override the default settings you can add config file inside the
`conf` directory and override the settings you want to be configured 
differently. Assume you want to have `DEBUG` and `LOGIN_DISABLED` enabled 
during development. Save the following data to `conf/dev.py`.

::

    DEBUG = True
    LOGIN_DISABLED = True


In order to use this config, export the name of the config file (without 
suffix `.py`) to `GEPPETTO_ENV` and start Geppetto. 

::
    
    $ export GEPPETO_ENV=dev
    $ ./server.py
