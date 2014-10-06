Deployment
==========

This section describes how to deploy Geppetto with `Nginx`_ and `uWSGI`_. You
can use other web servers and other WSGI servers if you desire. 

.. note::

    Throughout this page the location `/var/www/geppetto` is used. 
    If you put Geppetto somewhere else, set correct path.

Nginx
-----
Install Nginx.

::
    
    $ sudo apt-get install nginx

Nginx runs default as user `www-data` and so this user will run Geppetto. Add
the user `www-data` to the group `gpio`, so it can interact with the GPIO pins
without root permissions.

::

    $ sudo adduser www-data gpio

Put the configuration below inside `/etc/nginx/sites-available/geppetto`.

::

    server {
      server_name localhost;

      location / {
        try_files $uri @geppetto;
      }

      location @geppetto {
        include uwsgi_params;
        uwsgi_modifier1 30;
        uwsgi_pass unix:/var/www/geppetto/data/geppetto.sock;
      }
    }

and create a symbolic link to `/etc/nginx/sites-enabled/`:

::
    
    $ sudo ln -s /etc/nginx/site-available/geppetto /etc/nginx/sites-enabled/geppetto

Restart Nginx.

::
    
    $ sudo service restart nginx
    
uWSGI
-----
Install uWSGI inside your virtualenv, but install it also system wide.
Althought the latter is not necessarily required, the system wide installation 
copies some uWSGI configuration to the correct places. In order you install 
uWSGI inside your virtualenv Python's development headers are required. 

::

    $ sudo apt-get install uwsgi python-dev
    $ pip install uwsgi

When running Gepppetto we use uWSGI binary inside the virtualenv.
The reason that we use this binary is that the version from PyPi is newer than
the one from the Debian repositories.


Put the following configuration inside 
`/etc/uwsgi/apps-available/geppetto.ini`.

::

    [uwsgi]
    chdir = /var/www/geppetto
    uid = www-data
    gid = www-data
    chmod-socket = 666
    socket = /var/www/geppetto/data/geppetto.sock
    module = server
    callable = app
    virtualenv = /var/www/geppetto/.env
    plugins = python
    env = GEPPETTO_ENV=prod

Create a symbolic link to the `app-enabled` folder:

:: 

    ln -s /etc/uwsgi/apps-available/geppetto.ini /etc/uwsgi/apps-enabled/geppetto.ini

Now you can start uWSGI. Make sure you run the version of uWSGI installed in
your virtualenv!

::

    $ cd /var/www/geppetto
    $ source .env/bin/activate
    $ uwsgi --emperor /etc/uwsgi/sites-enabled --daemonize /var/www/geppetto/logs/uwsgi.log

Congratulations, Geppetto is running on port 80 of your Raspberry Pi.

.. _Nginx: http://nginx.org/
.. _uWSGI: https://uwsgi-docs.readthedocs.org/en/latest/
