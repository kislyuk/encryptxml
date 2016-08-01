#!/usr/bin/env python
# coding: utf-8

from __future__ import absolute_import, division, print_function, unicode_literals

import os, sys, unittest, itertools, re
from glob import glob
from xml.etree import ElementTree as stdlibElementTree

from lxml import etree
import cryptography.exceptions
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa, dsa, ec
from eight import str, bytes

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from encryptxml import *

class TestEncryptXML(unittest.TestCase):
    def setUp(self):
        pass

    def test_basic_encryptxml_statements(self):
        pass

if __name__ == '__main__':
    unittest.main()
