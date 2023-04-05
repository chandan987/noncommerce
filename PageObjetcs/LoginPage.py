from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
class LoginPage1:

    textbox_username_xpath = "//*[@id='Email']"
    textbox_password_xpath = "//*[@id='Password']"
    textbox_login_xpath = "/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/button"
    textbox_logout_linkTest = "Logout"

    def __init__(self,driver):
        self.driver = driver

    def chandan(self, username):

        self.driver.find_element(By.XPATH,self.textbox_username_xpath).clear()
        self.driver.find_element(By.XPATH,self.textbox_username_xpath).send_keys(username)

    def setpassword(self,password):

        self.driver.find_element(By.XPATH,self.textbox_password_xpath).clear()
        self.driver.find_element(By.XPATH,self.textbox_password_xpath).send_keys(password)

    def login(self):

        self.driver.find_element(By.XPATH,self.textbox_login_xpath).click()

    def logout(self):
        self.driver.find_element(By.LINK_TEXT,self.textbox_logout_linkTest).click()

