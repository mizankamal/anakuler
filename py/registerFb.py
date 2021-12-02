import time
from selenium import webdriver


driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.facebook.com/")
time.sleep(10)
driver.find_element_by_xpath("//*[text()='Buat Akun Baru']").click()
time.sleep(5)

driver.quit()

