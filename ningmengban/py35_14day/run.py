import unittest
from unittestreport import TestRunner

suit = unittest.defaultTestLoader.discover(r'/py35_14day/testcase')
runner = TestRunner(suit)
runner.run()
