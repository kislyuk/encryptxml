from __future__ import absolute_import, division, print_function, unicode_literals

import os
from base64 import b64encode, b64decode
from enum import Enum
from xml.etree import ElementTree as stdlibElementTree

from eight import str, bytes
from lxml import etree
from lxml.etree import Element, SubElement
from defusedxml.lxml import fromstring

import cryptography.exceptions
from cryptography.hazmat.primitives.asymmetric import rsa, dsa, ec
from cryptography.hazmat.primitives.asymmetric.padding import PKCS1v15
from cryptography.hazmat.primitives.hashes import Hash, SHA1, SHA224, SHA256, SHA384, SHA512
from cryptography.hazmat.backends import default_backend

from pyasn1.type import univ
from pyasn1.codec.der import encoder as der_encoder, decoder as der_decoder

from signxml import namespaces
from signxml.util import bytes_to_long, long_to_bytes, strip_pem_header, add_pem_header, ensure_bytes, ensure_str, _Namespace
from collections import namedtuple

def xenc_tag(tag):
    return "{" + namespaces.xenc + "}" + tag

def xenc11_tag(tag):
    return "{" + namespaces.xenc11 + "}" + tag

class xmlenc(object):
    """
    Create a new XML Encryption object. This is the main entry point to the functionality of the module.

    :param data: Data to encrypt or decrypt
    :type data: String or XML ElementTree Element API compatible object
    """
    def __init__(self, data):
        self.data = data

        if isinstance(data, stdlibElementTree.Element):
            self.data = fromstring(stdlibElementTree.tostring(data, encoding="utf-8"))

    def encrypt(self):
        raise NotImplementedError()

    def decrypt(self):
        raise NotImplementedError()
