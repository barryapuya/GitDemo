import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select

#This is for the Chrome for the to close after the Run
options = Options()
options.add_experimental_option('detach', True)
chrome_driver = webdriver.Chrome()
driver = webdriver.Chrome(options=options)

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")


driver.find_element(By.ID, "checkBoxOption1").click()
assert driver.find_element(By.ID, "checkBoxOption1").is_selected()


#checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
#print(len(checkboxes))

#for checkbox in checkboxes:
#    if checkbox.get_attribute("value") == "option2":
#        #checkbox.click()
#        assert checkbox.is_selected()
#$        break

