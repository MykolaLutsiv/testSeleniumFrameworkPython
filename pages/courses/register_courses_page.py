import logging
import utilities.custom_logger as cl
from base.basepage import BasePage
import time

class RegisterCoursesPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _search_box = "search-courses" #ID
    _course = '//div[@class="course-listing"]//div[contains(text(),"{0}")]' #XPath
    _all_courses = "course-listing"  #class
    _enroll_button = "enroll-button-top" #ID
    _cc_num = 'cardnumber' #name # fiframeName="__privateStripeFrame8"
    _cc_exp = "exp-date"  #name fiframeName="__privateStripeFrame9"
    _cc_cvv = "cvc"  #name fiframeName="__privateStripeFrame10"
    _postal_code = "postal" #name # fiframeName="__privateStripeFrame11"
    _agree_checkmark = 'agreed_to_terms_checkbox' #id
    _submit_enroll = 'confirm-purchase' #css
    _enroll_error_message = "//div[@class='payment-error-box']//span" #xpath (2 elements)
    _author_btn = "/html//div[@role='main']//div[@class='row search']/div[2]/div[@class='btn-group']" #xpath
    _author_dropdown = "//ul[@class='dropdown-menu']"
    _exact_author = '//a[contains(text(),"{0}")]'
    _selected_author = '//div[@class="btn-group"]//button[contains(text(),"{0}")]'

    def enterCourseName(self, name):
        self.sendKeys(data=name, locator=self._search_box,)
        self.elementClick(locator='search-course-button')

    def selectCourseToEnroll(self, fullCourseName):
        self.elementClick(self._course.format(fullCourseName), locatorType='xpath')


    def clickOnEnrollButton(self):
        self.elementClick(self._enroll_button)

    def enterCardNum(self, num):
        self.switchToFrame(name="__privateStripeFrame8")
        el = self.getElement(locator=self._cc_num, locatorType='name')
        for i in num:
            self.sendKeys(element=el, data=i)
            time.sleep(0.15)

        # self.sendKeys(data=num, locator=self._cc_num, locatorType='name')
        self.driver.switch_to.default_content()

    def enterCardExp(self, exp):
        self.switchToFrame(name="__privateStripeFrame9")
        self.sendKeys(data=exp, locator=self._cc_exp, locatorType='name')
        self.switchToDefaultContent()

    def enterCardCvv(self, cvv):
        self.switchToFrame(name="__privateStripeFrame10")
        self.sendKeys(data=cvv, locator=self._cc_cvv, locatorType='name')
        self.switchToDefaultContent()

    def enterPostalCode(self, postal_code):
        self.switchToFrame(name="__privateStripeFrame11")
        self.sendKeys(data=postal_code, locator=self._postal_code, locatorType='name')
        self.switchToDefaultContent()

    def enterCreditCardInformation(self, num, exp, cvv, postal_code):
        self.enterCardNum(num)
        self.enterCardExp(exp)
        self.enterCardCvv(cvv)
        self.enterPostalCode(postal_code)

    def clickEnrollSubmitButton(self):

        self.elementClick(self._submit_enroll, locatorType='id')

    def enrollCourse(self, num='', exp='', cvv='', postal_code=''):
        self.clickOnEnrollButton()
        self.webScroll('down')
        self.enterCreditCardInformation(num, exp, cvv, postal_code)
        self.elementClick(self._agree_checkmark)
        self.clickEnrollSubmitButton()

    def selectAuthor(self, authorName):
        self.elementClick(locator=self._author_btn, locatorType='xpath')
        self.elementClick(locator=self._author_dropdown + self._exact_author.format(authorName), locatorType='xpath')



    def verifyEnrollFailed(self):
        messageElement = self.waitForElement(locator=self._enroll_error_message, locatorType='xpath')
        result = self.isElementDisplayed(element=messageElement)
        return result
        # result = self.isEnabled(locator=self._submit_enroll, locatorType='id', info='enroll button')
        # return not result

    def verifySelectingOfAuthor(self, authorNeedToBeSelected):
        messageElement = self.waitForElement(locator=self._selected_author.format(authorNeedToBeSelected), locatorType='xpath')
        result = self.isElementDisplayed(element=messageElement)
        return result



