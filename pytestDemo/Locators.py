from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

#This is for the Chrome for the to close after the Run
options = Options()
options.add_experimental_option('detach', True)
chrome_driver = webdriver.Chrome()
driver = webdriver.Chrome(options=options)


#service_obj = Service("/Users/Barry/Browsers/chromedriver")
#driver = webdriver.Chrome(service=service_obj)

#service_obj = Service("/Users/Barry/Browsers/geckodriver")
#driver = webdriver.Firefox(service=service_obj)

#service_obj = Service("/Users/Barry/Browsers/msedgedriver")
#driver = webdriver.Edge(service=service_obj)

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")


driver.find_element(By.NAME, "email").send_keys("hello@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("123456")
driver.find_element(By.ID, "exampleCheck1").click()

#Creating a Xpath
# //tagname[@attribute='value'] -> //input[@type='submit']

#Creating a CSS
# tagname[attribute='value'] -> input[type='submit']

driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Barry")
driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click()
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("Testing")
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").clear()
driver.find_element(By.XPATH, "//input[@type='submit']").click()
message = driver.find_element(By.CLASS_NAME, "alert-success").text
print(message)
assert "Success" in message




