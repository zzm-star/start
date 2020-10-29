# -*- coding: utf-8 -*-\
import time
import unittest
import sys
sys.path.append('D:\\Program Files\\python_program files\\venv\\auto')
from crm_sys.cry_sys.util.execl_operation import OperationExcel
from HTMLTestRunner import HTMLTestRunner
from crm_sys.cry_sys.web_func.usermanager.login_page import Login


class TestLogin(unittest.TestCase):

    def setUp(self) -> None:
        self.op=OperationExcel('../../../../auto_excel/config/test_case.xlsx','用例参数')
        self.login=Login(self.op.get_cell(1,1))    #获取地址

    def test_login_name_pwd_error(self):
        self.login.login(self.op.get_cell(1,2),self.op.get_cell(1,3))
        alert_text = self.login.alert_text()
        self.login.log.set_mes('-获取弹出框内容-','info')
        self.assertEqual(alert_text,self.op.get_cell(1,8))

    def test_login_name__null(self):
        self.login.login(self.op.get_cell(3,2),self.op.get_cell(3,3))
        alert_text = self.login.alert_text()
        self.login.log.set_mes('-获取弹出框内容-','info')
        self.assertEqual(alert_text,self.op.get_cell(3,8))

    def test_login_pwd__null(self):
        self.login.login(self.op.get_cell(4,2),self.op.get_cell(4,3))
        alert_text = self.login.alert_text()
        self.login.log.set_mes('-获取弹出框内容-','info')
        self.assertEqual(alert_text,self.op.get_cell(4,8))

    def test_login_name__error(self):
        self.login.login(self.op.get_cell(5,2),self.op.get_cell(5,3))
        alert_text = self.login.alert_text()
        self.login.log.set_mes('-获取弹出框内容-','info')
        self.assertEqual(alert_text,self.op.get_cell(5,8))
    #
    def test_login_success(self):
        self.login.login(self.op.get_cell(2,2),self.op.get_cell(2,3))
        self.login.driver.switch_to.frame('mainFrame')
        tipp=self.login.driver.find_element_by_xpath('/html/body/form/table/tbody/tr[1]/td[1]').text
        self.assertEqual(tipp,self.op.get_cell(2,8))

    # def test_customeradd_success(self):
    #     self.login.addcustomer(self.op.get_cell(6,4),self.op.get_cell(6,5),self.op.get_cell(6,6),self.op.get_cell(6,7))
    #     alert_text = self.login.alert_text()
    #     self.login.log.set_mes('-获取弹出框内容-','info')
    #     self.assertEqual(alert_text,self.op.get_cell(6,8))
    #     self.login.alert_accept()



    def tearDown(self) -> None:
        self.login.driver.quit()
        # pass
if __name__=='__main__':
    # unittest.main()
    # 添加套件
    suite=unittest.TestSuite()
    test_case=unittest.TestLoader().loadTestsFromTestCase(TestLogin)
    suite.addTest(test_case)
    date_now = time.strftime('%y-%m-%d', time.localtime())
    # 创建HTML的报告
    with open('../../report/report.html', 'wb+')as file:
        runner = HTMLTestRunner(stream=file, verbosity=1, title='auto_test')
        runner.run(suite)

