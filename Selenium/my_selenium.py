from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from time import sleep
path = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(path)
driver.maximize_window()
driver.get("https://www.google.com/")
sleep(5)
input = driver.find_element(By.NAME , "q")
input.send_keys("kodlamaio")
serachButton= driver.find_element(By.NAME ,"btnK")
sleep(2)
serachButton.click()
sleep(1000)
firstResult =  driver.find_element(By.XPATH,"/html/body/div[5]/div/div[11]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div/div[1]/div/span/a" )
firstResult.click()
listCourses= driver.find_elements(By.CLASS_NAME,"course-listing")
print(f"Kodlama io sistesinde adet {len(listCourses)}")
# /html/body/div[5]/div/div[11]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div/div[1]/div/span/a
# data scraping sitelerden veri kazıma 
while True:
  continue
 