from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from time import sleep
path = "C:\Program Files (x86)\chromedriver.exe"

class Test_Sauce:
    def test_invalid_login(self):
     driver = webdriver.Chrome(path)
     driver.maximize_window()
     driver.get("https://www.saucedemo.com/")
     sleep(2)
     userNameInput= driver.find_element(By.ID , "user-name")
     passwordInput = driver.find_element(By.ID,"password")
     sleep(2)
     userNameInput.send_keys("1")
     passwordInput.send_keys("1")
     sleep(2)
     loginBtn= driver.find_element(By.ID , "login-button")
     sleep(2)
     loginBtn.click()
     
     errorMassage= driver.find_element(By.ID , "error-button ")
     print(errorMassage)
     sleep(3)

testClass= Test_Sauce()
testClass.test_invalid_login()
while True:
  continue
