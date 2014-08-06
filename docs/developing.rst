Developing
==========

Tests
-----
If you want to run the unittests you've to install `pytest`_ and some other
dependencies:

::
    
    pip install -r test_dependecies.txt


Run tests with:

::  
    
    py.test tests/

Docs
----
If you want to build the documentation you've to get the `Diaoul Sphinx theme`_
. This Git repository has been added as submodule. Fetch the data:

::

    $ git submodule init
    $ git submodule update

The documenation can be build either with:

:: 

    $ sphinx-build -aE -b html docs docs/_build

or:

::

    $ make -C docs html

.. _Diaoul Sphinx theme: https://github.com/Diaoul/diaoul-sphinx-thEmes
.. _pytest: http://pytest.org
