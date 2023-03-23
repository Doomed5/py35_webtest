import unittest

from unittestreport import TestRunner
from common.handle_path import DATA_DIR,CONF_DIR,TASTCASES_DIR,LOG_DIR,REPORT_DIR
suite = unittest.defaultTestLoader.discover(TASTCASES_DIR)

runner = TestRunner(suite,
                    filename="py35.html",
                    report_dir=REPORT_DIR,
                    )

runner.run()
