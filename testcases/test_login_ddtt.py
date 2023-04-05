import pytest
from PageObjetcs.LoginPage import LoginPage1
from testcases.conftest import setup
from utilities.readProperties import ReadConfig
from utilities.customlogger import LogGen
from utilities import ExcelUtils
import time


class Test_002_Login:
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()
    path = "C:\\Users\\APOGEE\\PycharmProjects\\noncommerce\\testdata\\LoginData.xlsx"
    lst_status = []

    @pytest.mark.regression
    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage1(self.driver)

        self.rows = ExcelUtils.getRowCount(self.path, 'Sheet1')
        self.logger.info("************TEST_002_Login_DDT************")
        self.logger.info("*****Verifying Login using DDT*****")
        for r in range(2, self.rows + 1):
            self.user = ExcelUtils.readData(self.path, 'Sheet1', r, 1)
            self.password = ExcelUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = ExcelUtils.readData(self.path, 'Sheet1', r, 3)

            self.lp.chandan(self.user)
            self.lp.setpassword(self.password)
            self.lp.login()
            time.sleep(4)

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.exp == "Pass":
                    self.logger.info("*****Passed*****")
                    self.lp.logout()
                    self.lst_status.append("Pass")
                elif self.exp == "Fail":
                    self.logger.info("*****Failed*****")
                    self.lp.logout()
                    self.lst_status.append("Fail")
            elif act_title != exp_title:
                if self.exp == "Pass":
                    self.logger.info("*****Failed*****")
                    self.lst_status.append("Fail")
                elif self.exp == "Fail":
                    self.logger.info("*****Passed*****")
                    self.lst_status.append("Pass")

        if "Fail" not in self.lst_status:
            self.logger.info("***** Login DDT test passed *****")
            self.driver.close()
            assert True

        else:
            self.logger.info("***** Login DDT test failed *****")
            self.driver.close()
            assert False
            self.logger.info("*********** Completed TEST_002_Login_DDT ***********")

        self.logger.info("#### End of TEST_002_Login_DDT ####")



