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

#service_obj = Service("/Users/Barry/Browsers/chromedriver")
#driver = webdriver.Chrome(service=service_obj)

driver.implicitly_wait(5) #Global wait even the elemets display it will automatic detect
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("Ber")
time.sleep(2) #special time -  since this is list and is not loaded yet
results = driver.find_elements(By.XPATH, "//div[@class='products']/div") #Chaining parent element
count = len(results)
assert count > 0
for result in results:
    result.find_element(By.XPATH, "div/button").click() #chaining of elements to this child  - find_element

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()

print(driver.find_element(By.CLASS_NAME, "promoInfo").text)

#assert driver.find_element(By.CSS_SELECTOR, ".promoInfo").get_attribute("value") == "Code applied ..!"












