import os
import time
import unittest
from HwTestReport import HTMLTestReport
from time import sleep

import HTMLTestRunner

import openpyxl as openpyxl
from selenium import webdriver

from base.base_page import BasePage
from page_object.login_page import LoginPage
from page_object.order_page import OrderPage
from page_object.sigle_page import SinglePage
from page_object.tenant_page import TenantPage
from ddt import data, file_data, ddt, unpack


import test_case
from test_case.excel_handle import ExcelHandle

file = r"../data/users.xlsx"
sheet = "Sheet1"
excelhandle = ExcelHandle(file,sheet)
test_data = excelhandle.read_excel()
print(test_data)


@ddt
class TestDemo1(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.lp = LoginPage(cls.driver)


    @classmethod
    def tearDownClass(cls) -> None:
        sleep(3)
        cls.driver.quit()

    @data(*test_data)
    @unpack
    def test_01_login(self,id,user,pwd,res):
        TestResult = '用户名或密码错误'
        try:
            cur = self.lp.login(user,pwd)
            try:
                self.assertIn("account",cur)
                TestResult = 'Succed'  # 成功
            except AssertionError as e:
                TestResult = 'Failed'  # 失败
                raise e
        finally:  # 不管怎样，finally都会执行，所以将写入excel的方法写在该模块，不然用例执行失败了，也没法写入excel
                # write_back()里面的‘python’可换成别的sheet，用来写回不同模块数据
            ExcelHandle(file,sheet).write_back(id + 1,4, TestResult)


if __name__ == '__main__':
    #unittest.main()
    case_path = os.path.join(os.getcwd())
    print (case_path)
    now = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
    report_path = os.path.join(os.getcwd(), 'report')
    # 2、html报告文件路径
    report_abspath = os.path.join(report_path, "result_" + now + ".html")

    # 3、打开一个文件，将result写入此file中
    fp = open(report_abspath, "wb")
    #runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=r'自动化测试报告,测试结果如下：', description=r'用例执行情况：')
    runner = HTMLTestReport(stream=fp,
                   verbosity=2,
                   title='自动化测试',
                   description='带饼图，带详情',
                   tester='yue')
    suites = unittest.defaultTestLoader.discover(case_path, pattern="test*.py")
    print(suites)
    # 4、调用add_case函数返回值
    runner.run(suites)
    fp.close()