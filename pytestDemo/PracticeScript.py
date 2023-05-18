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
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.find_element(By.XPATH, "//input[@value='radio2']").click()
dropdown = Select(driver.find_element(By.ID, "dropdown-class-example"))
dropdown.select_by_value("option1") #Use this if there a value on the objects

driver.find_element(By.ID, "autocomplete").send_keys('Aus')
time.sleep(2)

countries = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item']")
#For loop for clicking the Australia text
print(len(countries))

#Loop to the list until find the Australia text and click
for country in countries:
    if country.text == "Australia":
        country.click()
        assert driver.find_element(By.ID, "autocomplete").get_attribute("value") == "Australia"
        break