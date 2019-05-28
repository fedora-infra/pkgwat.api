pkgwat.api
==========

:Author: Ralph Bean <rbean@redhat.com>

.. comment: split here

Python API for `pkgwat <http://pypi.python.org/pypi/pkgwat.cli>`_.

Documentation:  http://pkgwat.rtfd.org


Setting up development environment
----------------------------------

Make sure you have ``virtualenv`` installed and create a new venv::

  $ virtualenv env
  $ source env/bin/activate
  $ pip install -e .

Running the test suite
----------------------

Make sure you have ``tox`` installed and run it (outside of any virtualenv)::

  $ tox
