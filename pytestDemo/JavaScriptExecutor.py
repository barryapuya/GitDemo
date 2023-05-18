import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless") #headless run
chrome_options.add_argument("--ignore-certificate-err") #ignore Certicate


service_obj = Service("/Users/Barry/Browsers/chromedriver")
driver = webdriver.Chrome(service=service_obj, options=chrome_options)
driver.implicitly_wait(2)
driver.maximize_window()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
driver.get_screenshot_as_file("Test.png")



