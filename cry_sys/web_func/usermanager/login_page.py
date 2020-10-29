#coding utf-8
import time
from argparse import Action

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert

from crm_sys.cry_sys.config.log_crm import AutoLog
from crm_sys.cry_sys.util.execl_operation import OperationExcel


class Login:
    def __init__(self,url):
        self.log = AutoLog()
        self.op=OperationExcel('../../../../auto_excel/config/test_case.xlsx','用例参数')
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        # self.driver.implicitly_wait(10)
        self.driver.get(url)

    def login(self,user,pwd):
        self.log.set_mes('登录功能开始','info')
        username = self.driver.find_element_by_name('userNum')
        username.send_keys(user)
        self.log.set_mes('-输入用户名-','info')
        self.driver.find_element_by_name('userPw').clear()
        self.driver.find_element_by_name('userPw').send_keys(pwd)
        self.log.set_mes('-输入密码-','info')
        self.driver.find_element_by_xpath('//*[@id="in1"]').click()
        self.log.set_mes('-点击登录-','info')

    def addcustomer(self,name,date,founder,email):
        self.login(self.op.get_cell(2,2),self.op.get_cell(2,3))
        self.driver.switch_to.parent_frame()
        time.sleep(2)
        self.driver.switch_to.frame('topFrame')
        time.sleep(2)
        self.log.set_mes('添加客户信息开始', 'info')
        clik=self.driver.find_element_by_xpath('/html/body/form/table/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr/td[5]/table/tbody/tr/td/div/a')
        clik.click()
        time.sleep(2)
        self.driver.switch_to.parent_frame()
        self.driver.switch_to.frame('mainFrame')
        cll=self.driver.find_element_by_xpath('/html/body/form/table/tbody/tr[1]/td/table/tbody/tr/td[2]/table/tbody/tr/td[4]/input')
        cll.click()
        time.sleep(2)
        self.driver.find_element_by_name('customerName').send_keys(name)
        self.log.set_mes('添加客户姓名', 'info')
        self.driver.find_element_by_name('customerBirthday').click()
        self.driver.execute_script("document.getElementById('customerBirthday').readOnly=false")
        self.driver.find_element_by_id('customerBirthday').clear()
        self.driver.find_element_by_name('customerBirthday').send_keys(date)
        self.log.set_mes('添加客户出生日期', 'info')
        self.driver.find_element_by_name('customerAddMan').send_keys(founder)
        self.log.set_mes('添加客户创建人', 'info')
        self.driver.find_element_by_name('customerEmail').send_keys(email)
        self.log.set_mes('添加客户email', 'info')
        button = self.driver.find_element_by_name('submit')
        self.driver.execute_script("arguments[0].click()", button)
        # self.driver.find_element_by_name('submit').click()
        time.sleep(5)


    def alert_text(self):
        alert = Alert(self.driver)
        return alert.text

    def alert_accept(self):
        alert = Alert(self.driver)
        alert.accept()



