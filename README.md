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
