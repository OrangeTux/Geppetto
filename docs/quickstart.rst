Quickstart
==========

Download the source from GitHub and install the requirements.

::

    $ git clone https://github.com/OrangeTux/Geppetto.git

Install depedencies:

:: 

    $ cd Geppetto
    $ pyvenv-3.4 .env
    $ source .env/bin/activate
    $ pip install -r requirements.txt

When on a Raspberry Pi, install also requirements listed in arm_requirements.txt:

:: 

    $ pip install -r arm_requirements.txt

Create a database and add an user with a API key:

:: 

    $ export GEPETTO_ENV=dev
    $ pynt setup_db
    [ build.py - Starting task "setup_db" ]
    [ build.py - Completed task "setup_db" ]
    $ pynt create_user
    [ build.py - Starting task "create_user" ]
    User <User 1, api_key: b'fcba99ca-3360-4683-a54d-1ce8ad1f20f3'> has been created.
    [ build.py - Completed task "create_user" ]

Start the server:

::

    $ sudo GEPETTO_ENV=dev .env/bin/python server.py
    * Running on http://127.0.0.1:5000/
    * Restarting with reloader
    [2014-06-25 19:12] DEBUG: app.tasks: Wrote 1 to pin 15.
    127.0.0.1 - - [25/Jun/2014 21:12:33] "POST /gpio/15/setpoint HTTP/1.1" 200 -

When the server is running do a POST request, for example from the Python 
interpreter. Use the API key generated earlier:

::

    >>> import requests, json, base64
    >>> # Create Authorization header.
    >>> auth = {'Authorization': base64.b64encode('fcba99ca-3360-4683-a54d-1ce8ad1f20f3').encode('utf-8')}
    >>> # Create body of POST request.
    >>> data = json.dumps({'value': 1})
    >>> # Do POST request
    >>> requests.post('http://localhost:5000/gpio/15/setpoint', headers=auth, data=data)
    <Response [200]>

