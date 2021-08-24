from selenium.webdriver.common.by import By

from base.base_page import BasePage


class OrderPage(BasePage):
    #页面url
    url = BasePage.url + '/pm/order'
    #搜索类型 name xpath= start
    start = (By.XPATH,"//thead/tr/th[3]/div/select")
    next = (By.XPATH,"//thead/tr/th[3]/div/select[2]")
    end = (By.ID,"dropdownBasic1")
    #//thead/tr//div/div/button
    endidx = (By.XPATH,"//div[contains(@class,'show')]/div/button")


    def sechorderbystart(self,idx1,idx2):
        self.open()
        self.wait(2)
        self.choose_index(self.start, idx1)
        self.wait(2)
        self.choose_index(self.next, idx2)
        self.wait(2)

    def sechorderbyend(self,idx):
        self.open()
        self.wait(2)
        self.click(self.end)
        self.webeleclick(self.endidx,idx)
        self.wait(2)
