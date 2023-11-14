import os
path1 = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
import sys
sys.path.append(path1)
from base.operation_element import OperationElement
from selenium import webdriver
from time import sleep
import os

class Login():
    def __init__(self):
        self.driver = webdriver.Chrome()        
        self.driver.get('https://www.zxxk.com/')
        self.driver.maximize_window()
        self.oper_ele = OperationElement(self.driver)
        self.username = ('name','username')
        self.password = ('name','password')
    def enter_login_page(self):
        data1 = ('xpath','/html/body/div[1]/div/a/img')
        self.oper_ele.click_element(data1)
        self.oper_ele.open_close_window(1)
        data2 = ('link text','登录')
        self.oper_ele.click_element(data2)
        sleep(1)
        data3 = ('xpath','/html/body/div[2]/div/div[2]/a')
        self.oper_ele.click_element(data3)
    def input_username(self,value):
        self.oper_ele.send_keys_element(self.username,value)
    def input_password(self,value):
        self.oper_ele.send_keys_element(self.password,value)

if __name__ == '__main__':
    login = Login()
    login.enter_login_page()
    login.input_username('13052256330')
    login.input_password('1991.11.11wang')


    