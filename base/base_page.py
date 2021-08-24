# coding = utf-8
"""
主要包括：打开url,定位，点击，输入，等待，退出
"""
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.select import Select

class BasePage:
    url = "http://192.168.33.121"
    def __init__(self,driver):
        self.driver=driver
    #获取当前窗口
    def cur_wid(self):
        now_url = self.driver.current_url
        print(now_url)
        return now_url
    #打开url
    def open(self):
        self.driver.get(self.url)

    #定位
    def locate(self,loc):
        return self.driver.find_element(*loc)

    def webele(self,loc):
        return self.driver.find_elements(*loc)

    #点击
    def click(self,loc):
        self.locate(loc).click()

    def webeleclick(self,loc,i):
        self.webele(loc)[i].click()

    #输入
    def input(self,loc,txt):
        self.locate(loc).send_keys(txt)
    #选择
    def choose_value(self,loc,txt):
        Select(self.locate(loc)).select_by_value(txt)

    def choose_index(self,loc,idx):
        Select(self.locate(loc)).select_by_index(idx)
    #等待
    def wait(self,time_):
        sleep(time_)

    #弹窗
    def dialog(self):
        alt = self.driver.switch_to.alter
        print(alt.text)
        return alt



    #取消
    def closedialog(self):

        self.dialog().dismiss()

    #确认
    def acceptdialog(self):
        self.dialog().accept()

    #关闭
    def quit(self):
        self.driver.quit()
