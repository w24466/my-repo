# coding=utf-8
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
ele = driver.get("http://192.168.33.121/login")
driver.find_element(By.NAME,"username").send_keys("admin")
driver.find_element(By.NAME,"password").send_keys("fnic1234")
driver.find_element(By.XPATH,"//button[text()='登录']").click()
sleep(3)
ele = driver.get("http://192.168.33.121/pm/order")
sleep(3)
ele12=driver.find_element(By.XPATH,"//thead/tr/th[3]/div/select")
Select(ele12).select_by_index(2)
sleep(3)
ele3=driver.find_element(By.XPATH,"//thead/tr/th[3]/div/select[2]")
Select(ele3).select_by_index(2)

a = self.locate(self.ass)
if a == "":
    res = "失败"
else:
    res = "成功"
file = "../data/users.xlsx"
sheet = "Sheet1"
ExcelHandle.write_back(file, sheet, id, 4, res)
