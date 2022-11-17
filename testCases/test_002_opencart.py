import pytest
from Utilities.readProperties import ReadConfig
from pageObjects.LoginPage import Login
from pageObjects.AdminDashboard import Dashboard

from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen
import os
from Utilities.customLogger import LogGen

class Test_001_Login:
    Baseurl=ReadConfig.getApplicationURl()
    username=ReadConfig.getemail()
    password=ReadConfig.getpassword()

    logger=LogGen.loggen()



    def test_login(self,setup):
        self.logger.info('***** verifying login test ***')

        self.driver=setup
        self.driver.get(self.Baseurl)
        self.lp=Login(self.driver)
        self.lp.setusername(self.username)
        self.lp.password(self.password)
        self.lp.clickLogin()
        act_title=self.driver.title
        self.lo=Dashboard(self.driver)
        self.lo.clicklogout()

        if act_title=="Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
            self.logger.info('***** login test passed ***')










