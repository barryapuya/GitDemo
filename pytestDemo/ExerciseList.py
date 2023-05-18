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


#2. List
#Create a list of the 3 elements when you search the ber
#Grab the products text of the 3 products list
#Put assertion with the actual list to expected list

expectedList = ['Cucumber - 1 Kg', 'Raspberry - 1/4 Kg', 'Strawberry - 1/4 Kg']
actualList = []

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.implicitly_wait(2) #Global wait even the elemets display it will automatic detect
driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("Ber")
time.sleep(2) #special time -  since this is list and is not loaded yet
results = driver.find_elements(By.XPATH, "//div[@class='products']/div") # list Chaining parent element
count = len(results)
assert count > 0
for result in results:
    actualList.append(result.find_element(By.XPATH, "h4").text)

assert expectedList == actualList


