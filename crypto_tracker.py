from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.get("https://coinmarketcap.com/")

time.sleep(15)
rows=driver.find_elements(By.XPATH,"//tbody/tr")
print("top 10 cryptocurrencies\n")

for i in range(10):
    data=rows[i].text.split("\n")
    
    rank=data[0]
    coin_name=data[1]
    price=data[4]

    print(f"{rank}.{coin_name:<12}-{price}")
driver.quit()    

     



