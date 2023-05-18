import time
from selenium import webdriver
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

#Execercise
#Grab the two values
#Total amount
#Total after discount
#Put assertion that Total after discount is less than Total amount value

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.implicitly_wait(2) #Global wait even the elemets display it will automatic detect
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
wait = WebDriverWait(driver, 10) #Explicit wait
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "promoInfo")))
print(driver.find_element(By.CLASS_NAME, "promoInfo").text)

#Grab the Values
print(driver.find_element(By.CSS_SELECTOR, ".totAmt").text)
print(driver.find_element(By.CSS_SELECTOR, ".discountAmt").text)

totalAmount = int(driver.find_element(By.CSS_SELECTOR, ".totAmt").text)
totalAfterDiscount = float(driver.find_element(By.CSS_SELECTOR, ".discountAmt").text)

assert totalAfterDiscount < totalAmount


























