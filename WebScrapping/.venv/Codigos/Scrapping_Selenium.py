from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

service = Service() # é usada para instanciar o chrome webdriver
options = webdriver.ChromeOptions() # definir preferencias do chrome
driver = webdriver.Chrome(service=service, options=options)

url = "https://youtube.com"

driver.get(url)
driver.find_element(By.TAG_NAME, value="input").send_keys("Ghost")
driver.find_element(By.TAG_NAME, value="input").send_keys(Keys.ENTER)
time.sleep(5)

driver.find_element(By.LINK_TEXT, value="Ghost - Mary On A Cross (Live In Tampa 2022)").click()
time.sleep(10 )