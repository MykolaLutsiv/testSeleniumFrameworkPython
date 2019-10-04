import logging
import utilities.custom_logger as cl
from base.basepage import BasePage

class NavigationPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _logo = '.navbar-brand'  #css
    _my_courses = '//a[@class="fedora-navbar-link navbar-link" and contains(text(), "My Courses")]'
    _all_courses = '//a[@class="fedora-navbar-link navbar-link" and contains(text(), "All Courses")]'
    _practice = '//a[@class="fedora-navbar-link navbar-link" and contains(text(), "Practice")]'
    _user_avatar = '.gravatar'
    _logOut = "//div[@id='navbar']//a[@href='/sign_out']"  #xpath

    def clickLogo(self):
        self.elementClick(self._logo, locatorType='css')

    def clickMyCourses(self):
        self.elementClick(self._my_courses, locatorType='xpath')

    def clickAllCourses(self):
        self.elementClick(self._all_courses, locatorType='xpath')

    def clickPractice(self):
        self.elementClick(self._practice, locatorType='xpath')

    def clickUser(self):
        userSetting = self.waitForElement(self._user_avatar, locatorType='css')
        self.elementClick(element=userSetting)


