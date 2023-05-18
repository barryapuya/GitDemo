import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select

#This is for the Chrome for the to close after the Run
#options = Options()
#options.add_experimental_option('detach', True)
#chrome_driver = webdriver.Chrome()
#driver = webdriver.Chrome(options=options)

service_obj = Service("/Users/Barry/Browsers/chromedriver")
driver = webdriver.Chrome(service=service_obj)

name = "Barry"
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")


driver.find_element(By.ID, "name").send_keys(name)
driver.find_element(By.ID, "alertbtn").click()
alert = driver.switch_to.alert
alertText = alert.text
print(alertText)
assert name in alertText
alert.accept()










