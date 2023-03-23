import unittest

from unittestreport import TestRunner

suite = unittest.defaultTestLoader.discover(r'C:\Users\siyaowu\Desktop\pythonproject\ningmengban\py35_17day_project'
                                            r'\testcases')

runner = TestRunner(suite,
                    filename="py35.html",
                    report_dir=r"C:\Users\siyaowu\Desktop\pythonproject\ningmengban\py35_17day_project\reports",
                    )

runner.run()
