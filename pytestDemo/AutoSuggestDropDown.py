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
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")

driver.find_element(By.ID, "autosuggest").send_keys("Ind")
time.sleep(2)

#driver.find_element(By.LINK_TEXT, "India").click() #you can use linktext

countries = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item']")
#For loop for clicking the india text
print(len(countries))

for country in countries:
    if country.text == "India":
        country.click()
        break


#print(driver.find_element(By.ID, "autosuggest").get_attribute("value")) #to get the value of the textbox fields
#assert driver.find_element(By.ID, "autosuggest").get_attribute("value") == "BIndia"

