import logging
import utilities.custom_logger as cl
from base.basepage import BasePage
from pages.home.navigaion_page import NavigationPage
from selenium import webdriver

class LoginPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.navigation = NavigationPage(driver)

    # Locators
    _login_link = 'Login'
    _email_field = 'user_email'
    _password_field = 'user_password'
    _login_button = '.login-button'

    def clickLoginLink(self):
        self.elementClick(self._login_link, locatorType='link')

    def enterEmail(self, email):
        self.sendKeys(email, self._email_field, )

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field, )

    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType='css')



    def login(self, email='', password=''):

        self.clickLoginLink()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()

    def verifyLoginSuccessful(self):
        return self.isElementDisplayed(self.navigation._user_avatar, locatorType='css')

    def verifyLoginFailed(self):
        result = self.isElementDisplayed("//div[contains(text(), 'Invalid email or password.')]",
                                       locatorType='xpath')

        return result

    def verifyTitle(self):
        return self.verifyPageTitle("Let's Kode It" )

    def logout(self):
        self.navigation.clickUser()
        logOutlinkElement = self.waitForElement(self.navigation._logOut,
                                                locatorType='xpath')
        self.elementClick(element=logOutlinkElement)

