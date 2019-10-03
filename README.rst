[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2Fcburgmer%2Fupsidedown.svg?type=shield)](https://app.fossa.io/projects/git%2Bgithub.com%2Fcburgmer%2Fupsidedown?ref=badge_shield)

==========
Upsidedown
==========

Upsidedown is a simple Python module that "flips" latin characters in a
string to create an "upside-down" impression. It makes extensive use of 
compatible latin characters as encoded in Unicode.

Example
=======

    >>> import upsidedown
    >>> print upsidedown.transform('hello world!')
    ¡pꞁɹoʍ oꞁꞁǝɥ

Installing
==========

Run the following to deploy the library on your system::

    $ python setup.py install

This does not only install the library but also registers an executable file
(on Win32 systems as ``upsidedown.exe`` in ``C:\Python26\Scripts\``).

Command line
============

You can also easily use this software on the command line::

    $ echo hello world\! | upsidedown
    ¡pꞁɹoʍ oꞁꞁǝɥ


## License
[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2Fcburgmer%2Fupsidedown.svg?type=large)](https://app.fossa.io/projects/git%2Bgithub.com%2Fcburgmer%2Fupsidedown?ref=badge_large)