import time
import pytest
from PageObjetcs.LoginPage import LoginPage1
from PageObjetcs.SearchCustomerPage import SearchCustomer
from utilities.customlogger import LogGen
from utilities.readProperties import ReadConfig
from PageObjetcs.AddcustommerPage import AddCustomer


class Test_SearchCustomerByName_005:
    baseUrl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    #@pytest.mark.regression
    def test_searchCustomerByName(self, setup):
        self.logger.info("*********** Test_005_SearchCustomerByName ***********")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()

        self.logger.info("******* Trying to Login *******")
        self.lp = LoginPage1(self.driver)
        self.lp.chandan(self.username)
        self.lp.setpassword(self.password)
        self.lp.login()

        self.logger.info("******* Login Successful *******")

        self.logger.info("******* Starting Search Customer By Name *******")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomerMenu()
        time.sleep(3)
        self.addcust.clickOnCustomerMenuItem()


        searchcust = SearchCustomer(self.driver)

        flag = searchcust.searchElementsVisible()
        if (flag == True):
            self.logger.info("******* Search Elements already visible *******")
            pass
        else:
            self.logger.info("******* CLicking on Search Dropdown *******")
            searchcust.clickDropdownSearch()

        time.sleep(2)

        self.logger.info("******* Searching Customer By Name *******")
        searchcust.setFirstName("Virat")
        searchcust.setLastName("Kohli")
        searchcust.clickSearch()
        time.sleep(3)
        status = searchcust.searchCustomerByName("Virat Kohli")
        if status == True:
            assert True
            self.logger.info("******* Customer found with the given Name  *******")

        else:
            assert False == False
            time.sleep(2)
            self.driver.save_screenshot(
                "C:\\Users\\APOGEE\\PycharmProjects\\noncommerce\\screenshots\\CustomerByName.png")
            self.logger.info("******* Customer not found with the given Name  *******")

        self.logger.info("******* Ending Test_005_SearchCustomerByName *******")
        self.driver.close()
