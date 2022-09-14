from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service


driver = webdriver.Firefox(service=Service(executable_path=GeckoDriverManager().install()))
driver.get("https://www.shorturl.at/")
driver.implicitly_wait(3)
search = driver.find_element(By.CSS_SELECTOR, "input[name='u']")
search.send_keys(input("Enter URL: "))
driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
driver.implicitly_wait(5)
print(driver.find_element(By.CSS_SELECTOR, "[type='text']").get_attribute('value'))
driver.close
