from selenium import webdriver
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select

class OperationElement():
    def __init__(self,driver,timeout=5,pf=0.5,ignored_exceptions=None):
        self.driver = driver
        self.timeout = timeout
        self.pf = pf
        self.ignored_exceptions=ignored_exceptions
    def find_element(self,data,):
        try:
            ele = WebDriverWait(self.driver,self.timeout,self.pf,self.ignored_exceptions).until(
                lambda x:x.find_element(*data)
            )
            return ele
        except:
            return None
    def send_keys_element(self,data,value):
        ele = self.find_element(data)
        ele.send_keys(value)
        
    def click_element(self,data):
        ele = self.find_element(data)
        ele.click()
        
    def title_is_text(self,value):
        try:
            ele = WebDriverWait(self.driver,self.timeout,self.pf,self.ignored_exceptions).until(
                EC.title_is(value)
            )
            return True
        except:
            return None
    def open_close_window(self,num):
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[num])
        sleep(2)
        self.driver.close()
        self.driver.switch_to.window(windows[0])
    def get_text_element(self,data):
        try:
            t = self.find_element(data).text
            return t
        except:
            print('没有获取到！')
            return None
    def move_to_element(self,data):
        '''鼠标悬停操作'''
        ele = self.find_element(data)
        ActionChains(self.driver).move_to_element(ele).perform()
    
    def select_by_index(self,data,index=0):
        ele = self.find_element(data)
        Select(ele).select_by_index(index)
        

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get('https://www.baidu.com/')
    data = ('xpath','//*[@id="s-top-left"]/a[6]')
    aa = OperationElement(driver)
    bb = aa.get_text_element(data)
    print(bb=='贴吧23')





            