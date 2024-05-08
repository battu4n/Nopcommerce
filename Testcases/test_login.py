import pytest

from Pageobjects.Loginpage import Loginpage
from utilities.readproperties import Readconfig
from utilities.customLogger import LogGen


class Test_001_Login:
    baseURL = Readconfig.getApplicationURL()
    username = Readconfig.getUseremail()
    password = Readconfig.getuserpasswor()
    logger = LogGen.loggen()
    @pytest.mark.sanity
    @pytest.mark.regression
    def test_homepagetittle(self, setup):
        self.logger.info("*********Test_001_Login********")
        self.logger.info("********Verify Home pagetittle********")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title == "Your store. Login":
            assert True
            print(act_title)
            self.logger.info("*****Home pagetittle is passed********")

        else:
            self.driver.save_screenshot(".\\Screensots\\" + "test_homepage.png")
            self.driver.close()
            self.logger.error("*****Home pagetittle is Failed********")
            assert False

    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info("********verify login test*********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Loginpage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setpassowrd(self.password)
        self.lp.clicklogin()
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("*****Home Login test case is passed********")
        else:
            self.driver.save_screenshot(".\\Screensots\\" + "test_loginpage.png")
            self.logger.error("*****Home Login test case is failed********")
            self.driver.close()
            print(act_title)
            assert False
