import pytest
from selenium import webdriver
from PageObjetcs.LoginPage import LoginPage1
from testcases.conftest import setup
from utilities.readProperties import ReadConfig
from utilities.customlogger import LogGen


class Test_001_login:
    baseUrl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_homepageTitle(self, setup):

        self.logger.info("**********************Test_001_login****************")
        self.logger.info("**********************test_homepageTitle****************")

        self.driver = setup
        self.driver.get(self.baseUrl)
        act_title = self.driver.title

        if act_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("**********************test_homepageTitle PASS****************")
        else:
            self.driver.save_screenshot("C:\\Users\\APOGEE\\PycharmProjects\\noncommerce\\screenshots\\test_homepageTitle.png")
            self.driver.close()
            self.logger.error("**********************test_homepageTitle Failed****************")
            assert False

    def test_login(self, setup):
        self.logger.info("**********************verify test login****************")
        self.driver = setup
        self.driver.get(self.baseUrl)

        self.lp = LoginPage1(self.driver)
        self.lp.chandan(self.username)
        self.lp.setpassword(self.password)
        self.lp.login()

        act_title = self.driver.title

        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
            self.logger.info("**********************login PAge PASS****************")
        else:
            self.driver.save_screenshot("C:\\Users\\APOGEE\\PycharmProjects\\noncommerce\\screenshots\\test_login.png")
            self.driver.close()
            self.logger.error("**********************login page is Failed****************")
            assert False

