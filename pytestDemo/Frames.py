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
driver.get("https://the-internet.herokuapp.com/iframe")
driver.switch_to.frame("mce_0_ifr")
driver.find_element(By.ID, "tinymce").clear()
driver.find_element(By.ID, "tinymce").send_keys("Testing this frame")
driver.switch_to.default_content()
print(driver.find_element(By.CSS_SELECTOR, "h3").text)

