from  selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time

driver = webdriver.Chrome()
url = "https://www.kitapyurdu.com/index.php?route=product/search&page=2&filter_name=python&filter_in_stock=0"
driver.get(url)
time.sleep(3)#wait for page to load
#input="python"
#searchInput= driver.find_element(By.ID, 'search-input')
#searchInput.send_keys(input)
#searchInput.send_keys(Keys.ENTER)
#ürünlerin bulunduğu div'e erişim

productNumber=len( driver.find_element(By.CLASS_NAME,'product-list').find_elements(By.CLASS_NAME,"name"))

pageNumber=str(driver.find_element(By.CLASS_NAME,("pagination")).find_element(By.CLASS_NAME,"results").text)
i=10
pageNumber=int(pageNumber[pageNumber.find("(")+1:pageNumber.find(" S")])

priceöö=len(driver.find_elements(By.CLASS_NAME,("price"))[i].find_elements(By.TAG_NAME,("div")))
if priceöö !=2:
    fiyat=driver.find_elements(By.CLASS_NAME,("price"))[i].find_element(By.TAG_NAME,("span")).text
    print(fiyat)
else:
    fiyat=driver.find_elements(By.CLASS_NAME,("price"))[i].find_element(By.CLASS_NAME,("price-new")).find_elements(By.TAG_NAME,("span"))[1].text
    print(fiyat)



"""
for i in range(1,pageNumber+1):
    url = "https://www.kitapyurdu.com/index.php?route=product/search&page="+str(i)+"&filter_name=python&filter_in_stock=0"
    driver.get(url)
    for j in range(0,productNumber):
        title = driver.find_element(By.CLASS_NAME, 'product-list').find_elements(By.CLASS_NAME,"name")[j].text

        publisher=driver.find_element(By.CLASS_NAME, 'product-list').find_elements(By.CLASS_NAME, "publisher")[j].find_element(By.TAG_NAME,"a").find_element(By.TAG_NAME,"span").text

        author=driver.find_element(By.XPATH,("/html/body/div[5]/div/div/div[3]/div[4]/div[2]/div["+str(j+1)+"]/div[1]/div[3]/div[2]/span/a/span")).text

        price= driver.find_element(By.CLASS_NAME, 'product-list').find_elements(By.CLASS_NAME, 'price-new')[j].find_element(By.CLASS_NAME,"value").text
        
        print(str(j),title,publisher,author,price)

"""
time.sleep(2)#wait for page to load


