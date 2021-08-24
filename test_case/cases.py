import os
import time
import unittest
from HwTestReport import HTMLTestReport
from time import sleep

import HTMLTestRunner
from selenium import webdriver
from page_object.login_page import LoginPage
from page_object.order_page import OrderPage
from page_object.sigle_page import SinglePage
from page_object.tenant_page import TenantPage
from ddt import data, file_data, ddt, unpack


@ddt
class TestDemo(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.lp = LoginPage(cls.driver)
        cls.tp = TenantPage(cls.driver)
        cls.sp = SinglePage(cls.driver)
        cls.op = OrderPage(cls.driver)

    @classmethod
    def tearDownClass(cls) -> None:
        sleep(3)
        cls.driver.quit()

    @file_data('../data/user_data.yaml')
    def test_01_login(self, **kwargs):
        self.lp.login(kwargs['user'], kwargs['pwd'])

    # @file_data('../data/tenantsearch_data.yaml')
    # def test_02_tensech(self, **kwargs):
    #     self.tp.search(kwargs['chspath'], kwargs['keywd'])
    #
    # @file_data('../data/userinfo.yaml')
    # def test_03_teadd(self, account, domain, buslic, user, pwd, rl, phone, email, idcard):
    #     self.tp.addtenant(account, domain, buslic, user, pwd, rl, phone, email, idcard)
    #
    # @data(["test1234", 8, 0])
    # @unpack
    # def test_04_tedt(self, account, i, j):
    #     self.tp.edtenant(account, i, j)
    #
    # @data(8)
    # def test_05_tdel(self, i):
    #     self.tp.deltenant(i)

    @data("弹性带宽")
    def test_06_sigprosechname(self, name):
        self.sp.searchpro_name(name)
    @unittest.skip("此用例不执行")
    @data(2, 3)
    def test_07_sigprosechkind(self, idx):
        self.sp.searchpro_kind(idx)

    # @file_data("../data/sigpro_name.yaml")
    # def test_08_sigproadd(self, i, proname):
    #     self.sp.addpro_name(i, proname)
    #
    # @data([2, 2], [1, 4])
    # @unpack
    # def test_09_orderbystart(self, idx1, idx2):
    #     self.op.sechorderbystart(idx1, idx2)
    #
    # @data(2, 1)
    # def test_10_orderbyend(self, idx):
    #     self.op.sechorderbyend(idx)


if __name__ == '__main__':
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
    suites = unittest.defaultTestLoader.discover(case_path, pattern="*.py")
    print(suites)
    # 4、调用add_case函数返回值
    runner.run(suites)
    fp.close()


