from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from base.base_page import BasePage


class SinglePage(BasePage):
    url = BasePage.url + '/pm/production'
    #搜索
    name = (By.NAME,"search_name")
    kind = (By.ID,"dropdownBasic1")
    ele = (By.XPATH,"//button[contains(@class,'dropdown-item')]")
    #添加只含名称的（防火墙、QOS、流量监控、远程办公、登录认证）
    addbtn = (By.XPATH,"//button[text()='添加单品']")
    addkind = (By.XPATH,"//form/div/div/ul/li")
    proname = (By.ID,"name")
    savebtn = (By.XPATH,"//button[text()='保存']")
    #宽带
    bandkind = (By.NAME,"attr_value")
    bandvalue = (By.XPATH,"//input[@class='form-control ng-tns-c9-6 ng-pristine ng-valid ng-star-inserted ng-touched']")
    ipnum = (By.XPATH,"(//input[@class='form-control ng-tns-c9-6 ng-pristine ng-valid ng-star-inserted ng-touched'])[2]")

    def searchpro_name(self,name):
        self.open()
        self.wait(3)
        self.input(self.name,name)
        self.input(self.name, Keys.ENTER)
        self.wait(3)

    def searchpro_kind(self,idx):
        self.open()
        self.wait(3)
        self.click(self.kind)
        self.wait(2)
        self.webeleclick(self.ele,idx)
        self.wait(3)
    #i取值1-防护墙 2-qos 3-流量监控 5-vpn 10-登录认证
    def addpro_name(self,i,proname):
        self.open()
        self.wait(2)
        self.click(self.addbtn)
        self.wait(2)
        self.webeleclick(self.addkind,i)
        self.wait(2)
        self.input(self.proname,proname)
        self.wait(2)
        self.click(self.savebtn)
        self.wait(2)
