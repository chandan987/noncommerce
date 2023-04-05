from selenium.webdriver.common.by import By
class SearchCustomer:
    txtEmail_xpath = "//input[@id='SearchEmail']"
    txtFirstName_xpath = "//input[@id='SearchFirstName']"
    txtLastName_xpath = "//input[@id='SearchLastName']"
    btnSearch_xpath = "//button[@id='search-customers']"

    #tblSearchResults_xpath = "//table[@role='grid']"
    tblSearchResults_xpath="// *[ @ id = 'customers-grid_wrapper'] / div[1] / div / div / div[1] / div / table"
    table_xpath = "//table[@id='customers-grid']"
    tableRows_xpath = "//table[@id='customers-grid']//tbody/tr"
    tableColumns_xpath = "//table[@id='customers-grid']//tbody/tr/td"
    drpSearchCustomer_xpath = "//i[@class='far fa-angle-down']"

    labelEmailText_xpath = "//label[contains(text(),'Email')]"

    def __init__(self, driver):
        self.driver = driver

    def clickDropdownSearch(self):
        self.driver.find_element(By.XPATH,self.drpSearchCustomer_xpath).click()

    def searchElementsVisible(self):
        # element_visible = self.driver.find_element_by_xpath(self.labelEmailText_xpath).isDisplayed()
        # print(element_visible)
        # if element_visible == True:
        #    return True
        # else:
        #    return False
        if self.driver.find_element(By.XPATH, self.labelEmailText_xpath).is_displayed():
            return True
        else:
            return False

    def setEmail(self, email):
        self.driver.find_element(By.XPATH,self.txtEmail_xpath).clear()
        self.driver.find_element(By.XPATH,self.txtEmail_xpath).send_keys(email)

    def setFirstName(self, fname):
        self.driver.find_element(By.XPATH,self.txtFirstName_xpath).clear()
        self.driver.find_element(By.XPATH,self.txtFirstName_xpath).send_keys(fname)

    def setLastName(self, lname):
        self.driver.find_element(By.XPATH,self.txtLastName_xpath).clear()
        self.driver.find_element(By.XPATH,self.txtLastName_xpath).send_keys(lname)

    def clickSearch(self):
        self.driver.find_element(By.XPATH,self.btnSearch_xpath).click()

    def getNoOfRows(self):
        return len(self.driver.find_elements(By.XPATH,self.tableRows_xpath))

    def getNoOfColumns(self):
        return len(self.driver.find_elements(By.XPATH,self.tableColumns_xpath))

    def searchCustomerByEmail(self, email):
        flag = False
        for r in range(1, self.getNoOfRows() + 1):
            table = self.driver.find_element(By.XPATH,self.table_xpath)
            emailid = table.find_element(By.XPATH,"//table[@id='customers-grid']/tbody/tr[" + str(r) + "]/td[2]").text
            if emailid == email:
                flag = True
                return flag
                break

    def searchCustomerByName(self, Name):
        flag = False
        for r in range(1, self.getNoOfRows() + 1):
            table = self.driver.find_element(By.XPATH,self.table_xpath)
            name = table.find_element(By.XPATH,"//table[@id='customers-grid']/tbody/tr[" + str(r) + "]/td[3]").text
            if name == Name:
                flag = True
                return flag
                break

    def searchElementsVisible(self):
        pass
