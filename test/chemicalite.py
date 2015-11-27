#!/bin/env python
import sys
import unittest

try:
    from pysqlite2 import dbapi2 as sqlite3
except ImportError:
    import sqlite3

class ChemicaLiteTestCase(unittest.TestCase):

    def setUp(self):
        self.db = sqlite3.connect(':memory:')
        self.db.enable_load_extension(True)
        self.db.load_extension('chemicalite')
        self.db.enable_load_extension(False)

