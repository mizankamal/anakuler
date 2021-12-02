from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get ('https://www.facebook.com/')
#time.sleep(2)
#driver.maximize_window("678x728")


#login
driver.find_elements_by_name("email").sendkeys("mizan.kamal@yahoo.com " + Keys.ENTER)

#input password
driver.find_elements_by_name("pass").sendkeys("Forfacebook20." + Keys.ENTER)

#click button
driver.find_element_by_name("u_0_d_oX").click()


#quit
driver.quit()