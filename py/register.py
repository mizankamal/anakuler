import time
from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://dev-magento.techmetroindonesia.com/")
time.sleep(10)

driver.maximize_window()

driver.find_element_by_link_text("linkText=Register").click()
time.sleep(4)
driver.find_element_by_id("name").click()
driver.find_element_by_id("name").send_keys("testing metro")
driver.find_element_by_id("email").send_keys("testing.metro05@gmail.com")
driver.find_element_by_id("telephone").send_keys("71234567")
driver.find_element_by_id("password").send_keys("Formetro20")
driver.find_element_by_id("password-confirmation").send_keys("Formetro20")
driver.find_element_by_id("city").click()
driver.find_element_by_css_selector("#city-list > li:nth-child(2)").click()
time.sleep(4)

driver.find_element_by_id("button-register").click()  
#driver.find_element_by_css_selector("#button-register").click()
#driver.find_element_by_xpath("//button[@id='button-register']").click()