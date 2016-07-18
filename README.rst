**Under Development**

EncryptXML: XML Encryption in Python
====================================
*EncryptXML* is an implementation of the W3C `XML Encryption <http://en.wikipedia.org/wiki/XML_Encryption>`_ standard in
Python. This standard is used along with `XML Signature <http://en.wikipedia.org/wiki/XML_Signature>`_ to provide
payload security in some implementations of `SAML 2.0 <http://en.wikipedia.org/wiki/SAML_2.0>`_, among other uses.
*EncryptXML* implements all of the required components of the standard, and most recommended ones.

Installation
------------
::

    pip install encryptxml

Please see the `SignXML documentation <https://github.com/kislyuk/signxml>`_ for installation notes, including notes on
dependencies that you must manually install.
    
Authors
-------
* Andrey Kislyuk

Links
-----
* `Project home page (GitHub) <https://github.com/kislyuk/encryptxml>`_
* `Documentation (Read the Docs) <https://encryptxml.readthedocs.io/en/latest/>`_
* `Package distribution (PyPI) <https://pypi.python.org/pypi/encryptxml>`_
* `Change log <https://github.com/kislyuk/encryptxml/blob/master/Changes.rst>`_
* `List of W3C XML Encryption standards and drafts <http://www.w3.org/TR/#tr_XML_Encryption>`_
* `W3C Recommendation: XML Encryption Syntax and Processing Version 1.1 <https://www.w3.org/TR/xmlenc-core1/>`_
* `W3C Working Group Note: Test cases for XML Encryption 1.1 <https://www.w3.org/TR/xmlenc-core1-testcases/>`_
* `XMLSec: Related links <https://www.aleksey.com/xmlsec/related.html>`_

Bugs
~~~~
Please report bugs, issues, feature requests, etc. on `GitHub <https://github.com/kislyuk/encryptxml/issues>`_.

License
-------
Licensed under the terms of the `Apache License, Version 2.0 <http://www.apache.org/licenses/LICENSE-2.0>`_.

.. image:: https://img.shields.io/travis/kislyuk/encryptxml.svg
        :target: https://travis-ci.org/kislyuk/encryptxml
.. image:: https://codecov.io/github/kislyuk/encryptxml/coverage.svg?branch=master
        :target: https://codecov.io/github/kislyuk/encryptxml?branch=master
.. image:: https://img.shields.io/pypi/v/encryptxml.svg
        :target: https://pypi.python.org/pypi/encryptxml
.. image:: https://img.shields.io/pypi/l/encryptxml.svg
        :target: https://pypi.python.org/pypi/encryptxml
.. image:: https://readthedocs.org/projects/encryptxml/badge/?version=latest
        :target: https://encryptxml.readthedocs.io/
