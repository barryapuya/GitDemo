import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait



service_obj = Service("/Users/Barry/Browsers/geckodriver")
driver = webdriver.Firefox(service=service_obj)

driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/windows")
print(driver.find_element(By.TAG_NAME, "h3").text)
assert "Opening a new window" == driver.find_element(By.TAG_NAME, "h3").text

driver.find_element(By.LINK_TEXT, "Click Here").click()
windowsOpened = driver.window_handles

#Switch to Child window
driver.switch_to.window(windowsOpened[1])
print(driver.find_element(By.TAG_NAME, "h3").text)
assert "New Window" == driver.find_element(By.TAG_NAME, "h3").text


driver.close() #close the child window

#switch to Parent window
driver.switch_to.window(windowsOpened[0])
assert "Opening a new window" == driver.find_element(By.TAG_NAME, "h3").text

