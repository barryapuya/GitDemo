import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

#This is for the Chrome for the to close after the Run
options = Options()
options.add_experimental_option('detach', True)
chrome_driver = webdriver.Chrome()
driver = webdriver.Chrome(options=options)

#service_obj = Service("/Users/Barry/Browsers/chromedriver")
#driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/loginpagePractise/")

driver.find_element(By.CSS_SELECTOR, ".blinkingText").click()
windowsOpened = driver.window_handles

#Switch to Child window
driver.switch_to.window(windowsOpened[1])
#print(driver.find_element(By.LINK_TEXT, "mentor@rahulshettyacademy.com").text)
#assert "mentor@rahulshettyacademy.com" == driver.find_element(By.LINK_TEXT, "mentor@rahulshettyacademy.com").text
email = driver.find_element(By.LINK_TEXT, "mentor@rahulshettyacademy.com").text
print(email)
driver.close() #close the child window

#switch to Parent window
driver.switch_to.window(windowsOpened[0])
driver.find_element(By.ID, "username").send_keys(email)
driver.find_element(By.ID, "password").send_keys("12345")
driver.find_element(By.ID, "signInBtn").click()

wait = WebDriverWait(driver,10)
wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".alert-danger")))
print(driver.find_element(By.CSS_SELECTOR, ".alert-danger").text)
#print(driver.find_element(By.CSS_SELECTOR, "div[class='alert alert-danger col-md-12'] strong").text)
#assert "Incorrect username/password." == driver.find_element(By.TAG_NAME, "strong").text



