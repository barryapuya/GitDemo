from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

#This is for the Chrome for the to close after the Run
options = Options()
options.add_experimental_option('detach', True)
chrome_driver = webdriver.Chrome()
driver = webdriver.Chrome(options=options)

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/client")


#driver.find_element(By.ID, "userEmail").send_keys("test@gmail.com")
#driver.find_element(By.ID, "userPassword").send_keys("123456")
driver.find_element(By.LINK_TEXT, "Forgot password?").click()
driver.find_element(By.XPATH, "//form/div[1]/input").send_keys("Test") #sample of xpath that travel to parent to child
driver.find_element(By.XPATH, "//form/div[2]/input").send_keys("Test")
driver.find_element(By.XPATH, "//button[@type='submit']").click()


