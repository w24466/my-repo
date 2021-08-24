# coding = utf-8
"""
租户页面：
    租户查询
    租户增加
    租户删除
    租户刷新
"""
from selenium import webdriver
from selenium.webdriver.common.by import By

from base.base_page import BasePage
from page_object.login_page import LoginPage


class TenantPage(BasePage):
    url = BasePage.url + '/account'

    #搜索元素
    tag_sel = (By.XPATH,"//a[text()='租户管理']")
    sel_kind = (By.XPATH,"//div/select")
    sechinput = (By.XPATH ,"//div/input[@class='form-control']")
    btn = (By.XPATH,"//button[text()='搜索']")
    #添加元素
    addbutton = (By.XPATH,"//button[text()=' 添加租户 ']")
    account = (By.NAME,"groupname")
    domain = (By.NAME,"domain")
    buslic = (By.ID,"file_businessLicence")
    user = (By.NAME,"adminUserName")
    pwd = (By.NAME,"adminUserPassword")
    role = (By.NAME,"role")
    phone = (By.NAME,"phone")
    email = (By.NAME,"email")
    idcard = (By.NAME,"idCard")
    savebtn = (By.XPATH,"//button[text()='保存 & 关闭 ']")
    #删除元素
    dele = (By.XPATH,"//button[text()='删除']")
    dis = (By.XPATH,"//button[text()='取消']")
    apt = (By.XPATH,"//button[text()='确定']")

    # 编辑元素
    edt = (By.XPATH, "//button[text()='编辑']")



    #业务流
    def search(self,chpath,keywd):
        self.open()
        self.wait(3)
        self.click(self.tag_sel)
        self.choose_value(self.sel_kind,chpath)
        self.input(self.sechinput,keywd)
        self.click(self.btn)
        self.wait(3)

    def addtenant(self,account,domain,buslic,user,pwd,rl,phone,email,idcard):
        self.open()
        self.wait(3)
        self.click(self.tag_sel)
        self.click(self.addbutton)
        self.input(self.account,account)
        self.input(self.domain,domain)
        self.input(self.buslic,buslic)
        self.input(self.user,user)
        self.input(self.pwd,pwd)
        self.choose_value(self.role,rl)
        self.input(self.phone,phone)
        self.input(self.email,email)
        self.input(self.idcard,idcard)
        self.click(self.savebtn)
        self.wait(3)
    #删除租户
    def deltenant(self,i):
        self.open()
        self.wait(3)
        self.webeleclick(self.dele, i)
        self.wait(3)
        self.click(self.dis)
        self.wait(3)



    # 编辑租户
    def edtenant(self,account,i,j):
        self.open()
        self.wait(3)
        self.webeleclick(self.edt,i)
        self.wait(3)
        self.input(self.account,account)
        self.webeleclick(self.savebtn,j)




