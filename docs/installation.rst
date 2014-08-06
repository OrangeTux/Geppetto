Installation
============

Download the source from GitHub and install the requirements.

::

    $ git clone https://github.com/OrangeTux/Geppetto.git

Install Python dependencies:

:: 

    $ cd Geppetto
    $ virtualenv .env
    $ source .env/bin/activate
    $ pip install -r requirements.txt


.. note::
    
    Gepppetto can be used with Python 2.7. It might also work with Python >= 
    3.3.

Geppetto uses `Quick2Wire's`_ `GPIO Admin`_ to use GPIO pins without root 
permissions. Download this utility and follow the `installation instructions`_

.. _Quick2Wire's: http://quick2wire.com/
.. _GPIO Admin: https://github.com/quick2wire/quick2wire-gpio-admin
.. _installation instructions: https://github.com/quick2wire/quick2wire-gpio-admin#installation
