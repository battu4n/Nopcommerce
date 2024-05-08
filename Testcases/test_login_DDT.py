import time

import pytest

from Pageobjects.Loginpage import Loginpage
from utilities.readproperties import Readconfig
from utilities.customLogger import LogGen
from utilities import Xlutils


class Test_002_DDT_Login:
    baseURL = Readconfig.getApplicationURL()
    path = ".//Testdata/Logintest.xlsx"
    logger = LogGen.loggen()
    @pytest.mark.sanity
    def test_login_ddt(self, setup):
        self.logger.info("****This is my TS_002 Test case ****")
        self.logger.info("********verify login DDT_test*********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = Loginpage(self.driver)
        self.rows = Xlutils.getRowCount(self.path, 'Sheet1')
        print(self.rows)

        lst_status = []  # EMpty list created

        for r in range(2, self.rows + 1):
            self.user = Xlutils.readData(self.path, 'Sheet1', r, 1)
            self.password = Xlutils.readData(self.path, 'Sheet1', r, 2)
            self.exp = Xlutils.readData(self.path, 'Sheet1', r, 3)

            self.lp.setUserName(self.user)
            self.lp.setpassowrd(self.password)
            self.lp.clicklogin()
            time.sleep(5)

            act_title = self.driver.title
            exp_title = "Dashboard /nopCommerce administration"

            if act_title == exp_title:
                if self.exp == "Pass":
                    self.logger.info("****Test is passed*****")
                    self.lp.clicklogout()
                    lst_status.append("Pass")
                elif self.exp == "Fail":
                    self.logger.info("***Failed the test case****")
                    self.lp.clicklogout()
                    lst_status.append("Fail")
            elif act_title != exp_title:
                if self.exp == 'Pass':
                    self.logger.info("**** Failed****")
                    lst_status.append("Fail")

                elif self.exp == "Fail":
                    self.logger.info("***Passed****")
                    lst_status.append("Pass")

        if "Fail" not in lst_status:
            self.logger.info("Login DDT test Passed....")
            self.driver.close()
            assert True

        else:
            self.logger.info("****Login DDT Failed****")
            self.driver.close()
            assert False
        self.logger.info("****ENd of the DDT Test cases****")
        self.logger.info("***** completed TC_LoginDDT_002*****")
