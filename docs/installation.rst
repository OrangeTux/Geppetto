Installation
============

.. note::
    
    Gepppetto works with Python 2.7 and Python >= 3.3.

Download the source from GitHub and install the requirements.

::

    $ git clone https://github.com/OrangeTux/Geppetto.git

Install Python dependencies:

:: 

    $ cd Geppetto
    $ virtualenv .env
    $ source .env/bin/activate
    $ pip install -r requirements.txt


Setup the database and create a user with an API key:

::

    $ pynt setup_db create_user
    [ build.py - Starting task "setup_db" ]
    [ build.py - Completed task "setup_db" ]
    [ build.py - Starting task "create_user" ]
    User <User 1, api_key: b'fcba99ca-3360-4683-a54d-1ce8ad1f20f3'> has been created.
    [ build.py - Completed task "create_user" ]

You can use generated API key for authentication


Geppetto uses `Quick2Wire's`_ `GPIO Admin`_ to use GPIO pins without root 
permissions. Download this utility and follow the `installation instructions`_

.. _Quick2Wire's: http://quick2wire.com/
.. _GPIO Admin: https://github.com/quick2wire/quick2wire-gpio-admin
.. _installation instructions: https://github.com/quick2wire/quick2wire-gpio-admin#installation
