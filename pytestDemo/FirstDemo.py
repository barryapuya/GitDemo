from selenium import webdriver
from selenium.webdriver.chrome.service import Service
#from selenium.webdriver.firefox.service import Service

service_obj = Service("/Users/Barry/Browsers/chromedriver")
driver = webdriver.Chrome(service=service_obj)

#service_obj = Service("/Users/Barry/Browsers/geckodriver")
#driver = webdriver.Firefox(service=service_obj)

#service_obj = Service("/Users/Barry/Browsers/msedgedriver")
#driver = webdriver.Edge(service=service_obj)

driver.get("https://rahulshettyacademy.com/")
driver.maximize_window()
print(driver.title)
print(driver.current_url)
driver.get("https://rahulshettyacademy.com/practice-project")
print(driver.current_url)
#driver.minimize_window()
driver.back()
driver.refresh()
driver.forward()