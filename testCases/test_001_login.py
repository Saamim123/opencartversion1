from Utilities.readProperties import ReadConfig
from pageObjects import LoginPage
from pageObjects.LoginPage import LoginPage
import os
from Utilities.customLogger import LogGen


class Test_001_login:
    Baseurl = ReadConfig.getApplicationURl()
    logger=LogGen.loggen()

    def test_login(self,setup):
        self.logger.info('******** test_login Test started *****')
        self.driver = setup
        self.driver.get(self.Baseurl)
        self.logger.info('******** launching application *****')
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.logger.info('******** setting username *****')
        self.lp.setusername('admin@yourstore.com')
        self.lp.password('admin')
        self.lp.clickLogin()
        self.logger.info('******** Getting logged in *****')
        self.confmsg = self.lp.getconfirmationmsg()
        self.driver.close()
        if self.confmsg == "Dashboard":
            self.logger.info('******** login pass *****')
            assert True
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir)+"\\screenshots\\" + "test_login.png")
            self.driver.close()
            self.logger.error('******** login Fail *****')
            assert False
        self.logger.info('******** test_login Test finished *****')
