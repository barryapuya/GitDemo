import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

# This is for the Chrome for the to close after the Run
options = Options()
options.add_experimental_option('detach', True)
chrome_driver = webdriver.Chrome()
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(4)
driver.maximize_window()


browserSortedVeggie = []

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")

# click the sorted button
driver.find_element(By.XPATH, "//span[normalize-space()='Veg/fruit name']").click()

# collect all Veggie names -- > browserVeggieList(A, B, C)
browserVeggieList = driver.find_elements(By.XPATH, "//tr/td[1]")  # list Chaining parent element
for ele in browserVeggieList:
    browserSortedVeggie.append(ele.text)

originalBrowserSortedVeggie = browserSortedVeggie.copy()

# Sort this browserVeggieList - > newSortedList - > (A, B, C)
browserSortedVeggie.sort()

# browserVeggieList == newSortedList
assert browserSortedVeggie == originalBrowserSortedVeggie
print(browserSortedVeggie)


