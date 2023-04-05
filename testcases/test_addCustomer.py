from PageObjetcs.AddcustommerPage import AddCustomer
from utilities.readProperties import ReadConfig
from utilities.customlogger import LogGen
from testcases.conftest import setup
from PageObjetcs.LoginPage import LoginPage1
import random
import string
import time
import pytest
from selenium.webdriver.common.by import By


class Test_003_AddCustomer:
    baseUrl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    #@pytest.mark.sanity
    def test_addCustomer(self, setup):
        self.logger.info("*********** Test_003_AddCustomer ***********")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()

        self.logger.info("******* Trying to Login *******")

        self.lp = LoginPage1(self.driver)
        self.lp.chandan(self.username)
        self.lp.setpassword(self.password)
        self.lp.login()

        self.logger.info("******* Login Successful *******")
        self.logger.info("******* Starting Add Customer Test *******")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomerMenu()
        time.sleep(1)
        self.addcust.clickOnCustomerMenuItem()

        self.addcust.clickOnAddnew()
        self.logger.info("******* Providing Customer info *******")

        self.email = random_generator() + "@gmail.com"
        self.addcust.setEmail(self.email)
        self.addcust.setPassword("test123")
        self.addcust.setFirstname("Salim")
        self.addcust.setLastname("Khan")
        self.addcust.setGender("Male")
        self.addcust.setDOB("01/11/1995")
        self.addcust.setCompanyName("QA Automation")
        self.addcust.setCustomerRole("Guests")
        self.addcust.setManagerOfVendor("Vendor 2")
        self.addcust.setAdminContent("This is for testing purpose......")
        self.addcust.clickOnSave()

        self.logger.info("******* Saving Customer info *******")
        self.logger.info("******* Add Customer Validation started *******")

        self.msg = self.driver.find_element(By.TAG_NAME,"body").text
        if 'customer has been added successfully' in self.msg:
            assert True
            self.logger.info("******* Add Customer Test Passed *******")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer_scr.png")
            assert False
            self.logger.info("******* Add Customer Test Failed *******")

        self.driver.close()
        self.logger.info("******* Ending Test_003_AddCustomer Test *******")


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))
