from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
import time
service=Service("./chromedriver.exe")
driver=webdriver.Chrome(service=service)
driver.get("https://www.kitapyurdu.com/")

searchBox=driver.find_element(By.ID,"search-input")
searchBox.send_keys("python")   
searchBox.send_keys(Keys.ENTER)
time.sleep(10)

for i in range(len(driver.find_elements(By.CLASS_NAME, "name"))):
    title=str(driver.find_elements(By.CLASS_NAME, "name")[i].find_element(By.TAG_NAME,"a").get_attribute("title"))
    publisher=str(driver.find_elements(By.CLASS_NAME, "publisher")[i].find_element(By.TAG_NAME,"a").find_element(By.TAG_NAME,"span").text)
    author=str(driver.find_elements(By.CLASS_NAME, "author")[i].text)
    price=str(driver.find_elements(By.CLASS_NAME,"price-new")[i].text)

    print(title, publisher, author, price)
  