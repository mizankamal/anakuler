import time
from selenium import webdriver
from selenium.webdriver.support import select
from selenium.webdriver.support.select import Select


driver = webdriver.Chrome()

driver.get("https://dev-magento.techmetroindonesia.com/")
time.sleep(10)

driver.maximize_window()

driver.find_element_by_xpath("//a[contains(text(),'Sign In')]").click()
time.sleep(2)
driver.find_element_by_css_selector("#username").send_keys("kamalmizan7@gmail.com")
driver.find_element_by_id("form-login").click()

time.sleep(3)
driver.find_element_by_css_selector(".input-group > #pass").send_keys("Formetro20")

time.sleep(2)
driver.find_element_by_xpath("//button[@id='form-login']").click()

time.sleep(8)
driver.find_element_by_id("search").click()
driver.find_element_by_id("search").send_keys("28152367")
driver.find_element_by_css_selector(".actions > .search").click()
time.sleep(10)

driver.find_element_by_css_selector(".view-details").click()
time.sleep(3)

#driver.find_element_by_css_selector(".swatch-attribute-options > .color").click()

driver.find_element_by_xpath("//*[@id='product-options-wrapper']/div/div/div[1]/div/select/option[2]").click()
driver.find_element_by_xpath("//*[@id='product-options-wrapper']/div/div/div[3]/div/select/option[2]").click()
time.sleep(4)

driver.find_element_by_xpath("//*[@id='product-addtocart-button']").click()
time.sleep(10)

driver.find_element_by_css_selector(".showcart").click()
driver.find_element_by_css_selector(".checkout:nth-child(1)").click()
time.sleep(10)

driver.find_element_by_css_selector(".checkout:nth-child(1)").click()
driver.find_element_by_css_selector(".bx-payment:nth-child(4) label").click()
time.sleep(10)

driver.find_element_by_css_selector(".active .action > span").click()


