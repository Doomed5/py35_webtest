import unittest

from unittestreport import ddt, list_data

from py35_14day.register import register

from py35_14day.testcase.handle_excel import ReadExcel

excel = ReadExcel(r"C:\Users\siyaowu\Desktop\pythonproject\ningmengban\py35_14day\testcase\testcase.xlsx", 'register')
cases = excel.read_cases()


@ddt
class TestRegister(unittest.TestCase):
    @list_data(cases)
    def test_register(self, case):
        excepted = eval(case['excepted'])
        data = eval(case['data'])
        res = register(*data)
        try:
            self.assertEqual(excepted, res)
        except AssertionError as e:
            excel.write_data(row=case['case_id'] + 1, column=5, value='未通过')
            raise e
        else:
            excel.write_data(row=case['case_id'] + 1, column=5, value='通过')
