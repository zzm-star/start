#
# import time
#
# from crm_sys.cry_sys.web_func.usermanager.login_page import Login
#
#
# class CustomerAdd:
#     def __init__(self):
#         self.login=Login()
#
#     def addcustomer(self, name, date, email, founder):
#         self.log.set_mes('登录功能开始', 'info')
#         self.login(self.op.get_cell(2, 2), self.op.get_cell(2, 3))
#         self.driver.switch_to.parent_frame()
#         time.sleep(2)
#         self.driver.switch_to.frame('topFrame')
#         time.sleep(2)
#         self.log.set_mes('添加客户信息开始', 'info')
#         self.driver.find_element_by_xpath('//*[@id="submenu1"]/div/table/tbody/tr[1]/td/table/tbody/tr[1]/td[2]/table/tbody/tr/td/span/a').click()
#         self.driver.switch_to.parent_frame()
#         self.driver.switch_to.frame('mainFrame')
#         self.driver.find_element_by_xpath('/html/body/form/table/tbody/tr[1]/td/table/tbody/tr/td[2]/table/tbody/tr/td[4]/input').click()
#         self.driver.switch_to.parent_frame()
#         time.sleep(2)
#         customer_name = self.driver.find_element_by_name('customerName').send_keys(name)
#         self.log.set_mes('添加客户姓名', 'info')
#         self.driver.find_element_by_name('customerBirthday').send_keys(date)
#         self.log.set_mes('添加客户出生日期', 'info')
#         self.driver.find_element_by_name('customerEmail').send_keys(email)
#         self.log.set_mes('添加客户email', 'info')
#         self.driver.find_element_by_name('customerAddMan').send_keys(founder)
#         self.log.set_mes('添加客户创建人', 'info')
#         self.driver.find_element_by_name().click()
#         self.log.set_mes('点击添加', 'info')
#
#
#
#
#     def change_window(self, window_handles=None):
#         self.driver.switch_to.window(window_handles[-1])
#         return self.driver.title