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


driver.get("https://rahulshettyacademy.com/angularpractice/")
# for xpath //a[contains(@href, 'shop')]   CSS - a[href*='shop']
driver.find_element(By.LINK_TEXT, "Shop").click()

products = driver.find_elements(By.XPATH, "//div[@class='card h-100']")
for product in products:
    ProductName = product.find_element(By.XPATH, "div/h4/a").text  # chaning elements
    print(ProductName)
    if ProductName == "Blackberry":
        product.find_element(By.XPATH, "div/button").click()

driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
driver.find_element(By.ID, "country").send_keys("ind")
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"India")))
driver.find_element(By.LINK_TEXT, "India").click()
driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
driver.find_element(By.CSS_SELECTOR, "[type='submit'").click()
SuccessText = driver.find_element(By.CLASS_NAME, "alert-success").text

assert "Success! Thank you!" in SuccessText




