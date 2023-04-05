import time
import pytest
from PageObjetcs.LoginPage import LoginPage1
from PageObjetcs.SearchCustomerPage import SearchCustomer
from utilities.customlogger import LogGen
from utilities.readProperties import ReadConfig
from PageObjetcs.AddcustommerPage import AddCustomer


class Test_SearchCustomerByEmail_004:
    baseUrl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

   # @pytest.mark.sanity
    #@pytest.mark.regression
    def test_searchCustomerByEmail(self, setup):
        self.logger.info("*********** Test_004_SearchCustomerByEmail ***********")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()

        self.logger.info("******* Trying to Login *******")

        self.lp = LoginPage1(self.driver)
        self.lp.chandan(self.username)
        self.lp.setpassword(self.password)
        self.lp.login()

        self.logger.info("******* Login Successful *******")

        self.logger.info("******* Starting Search Customer By Email *******")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomerMenu()
        time.sleep(2)
        self.addcust.clickOnCustomerMenuItem()

        searchcust = SearchCustomer(self.driver)

        # #flag = searchcust.searchElementsVisible()
        # #if flag == True:
        #     self.logger.info("******* Search Elements already visible *******")
        #     pass
        # else:
        #     self.logger.info("******* CLicking on Search Dropdown *******")
        #     searchcust.clickDropdownSearch()

        time.sleep(2)

        self.logger.info("******* Searching Customer By Email *******")

        searchcust.setEmail("kiyjcycyhjc676008@gmail.com")
        searchcust.clickSearch()
        time.sleep(3)
        status = searchcust.searchCustomerByEmail("kiyjcycyhjc676008@gmail.com")
        if status == True:
            assert True
            self.logger.info("Customer found with given email")
        else:
            assert False == False
            self.logger.info("Customer is not available with given email")

        self.logger.info("******* Ending Test_004_SearchCustomerByEmail *******")
        self.driver.close()