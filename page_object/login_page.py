# coding = utf-8
'''
登录页面对象
登录流程
关联元素：
    账号
    密码
    登录按钮
'''
from selenium import webdriver
from selenium.webdriver.common.by import By

from base.base_page import BasePage


class LoginPage(BasePage):
    #页面url
    url = BasePage.url + '/login'
    #页面元素
    user = (By.NAME , "username")
    pd = (By.NAME , "password")
    btn = (By.XPATH , "//button")
    #业务流
    def login(self,username,password):
        self.open()
        self.wait(3)
        self.input(self.user,username)
        self.input(self.pd,password)
        self.click(self.btn)
        self.wait(3)
        return self.cur_wid()


