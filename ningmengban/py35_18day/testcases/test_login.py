import unittest
import os
from unittestreport import ddt, list_data
from common.handle_excel import HandleExcel
from login_func import login_check
from common.handler_log import my_log
from common.handle_path import DATA_DIR, CONF_DIR, TASTCASES_DIR, LOG_DIR, REPORT_DIR


@ddt
class TestLogin(unittest.TestCase):
    excel = HandleExcel(os.path.join(DATA_DIR, 'cases.xlsx'), "login")
    cases = excel.read_data()

    @list_data(cases)
    def test_login(self, item):
        # 1、准备用例数据
        expected = eval(item["expected"])
        params = eval(item["data"])
        row = item["case_id"] + 1
        # 2、调用功能函数（接口）进行测试，获取结果
        res = login_check(**params)
        # 3、断言-->测试结果回写，日志输出
        try:
            self.assertEqual(expected, res)
        except AssertionError as e:
            self.excel.write_data(row=row, column=5, value='不通过')
            my_log.error("用例--【{}】---执行失败".format(item['title']))
            my_log.error(e)
            # 记录详细的错误信息到日志用exception方法
            # my_log.exception(e)
            raise e
        else:
            self.excel.write_data(row=row, column=5, value='通过')
            my_log.info("用例--【{}】---执行成功".format(item['title']))
