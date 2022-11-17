from selenium.webdriver.common.by import By

class Dashboard:
    link_logout_xpath="//a[normalize-space()='Logout']"

    def __init__(self, driver):  # initializing driver
        self.driver = driver

    def clicklogout(self):
        self.driver.find_element(By.XPATH,self.link_logout_xpath).click()



