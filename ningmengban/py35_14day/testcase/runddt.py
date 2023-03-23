import unittest
from unittestreport import TestRunner

suit = unittest.defaultTestLoader.discover(r'C:\Users\siyaowu\Desktop\pythonproject\ningmengban\py35_14day\testcase')
runner = TestRunner(suit)
runner.run()
