from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import os
from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import logging
import utilities.custom_logger as cl
from base.webdriverfactory import WebDriverFactory

class SeleniumDriver():

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    def getTitle(self):
        return self.driver.title

    def getByType(self, locatorType):
        locatorType = locatorType.lower()

        if locatorType == 'id':
            return By.ID
        elif locatorType == 'xpath':
            return By.XPATH
        elif locatorType == 'css':
            return By.CSS_SELECTOR
        elif locatorType == 'class':
            return By.CLASS_NAME
        elif locatorType == 'link':
            return By.LINK_TEXT
        elif locatorType == 'name':
            return By.NAME
        else:
            self.log.error(f'Not found locatorType: {locatorType}')
        return False

    def getElement(self, locator, locatorType='id'):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            self.log.info('Element Found')
        except:
            self.log.error('Element not Found')
        return element

    def elementClick(self, locator='', locatorType='id', element=None):
        try:
            if locator:
                element = self.getElement(locator, locatorType)
            element.click()
            self.log.info(f'Click on element with locator -> {locator} and type of locator -> {locatorType}')
        except:
            self.log.error(f'Cannot click on element with locator -> {locator} and type of locator -> {locatorType}')
            print_stack()

    def sendKeys(self, data, locator='', locatorType='id', element=None):
        try:
            if locator:
                element = self.getElement(locator, locatorType)
            element.clear()
            element.send_keys(data)
            self.log.info(f'Send {data} on element with locator -> {locator} and type of locator -> {locatorType}')
        except:
            self.log.error(f'Cannot send data on element with locator -> {locator} and type of locator -> {locatorType}')
            print_stack()

    def getElementList(self, locator, locatorType='id'):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_elements(byType, locator)
            self.log.info(f'Element list Found with {byType}:::{locator}')
        except:
            self.log.error(f'Element not Found with {byType}:::{locator}')

        return element

    def getText(self, locator='', locatorType='id', element=None, info=''):
        try:
            if locator:
                self.log.debug('In locator condition')
                element = self.getElement(locator, locatorType)
            text = element.text
            self.log.debug(f'Fater findind element text, size is: {str(len(text))}')
            if len(text) == 0:
                text = element.get_attribute('innerText')
            if len(text) != 0:
                self.log.info('Getting text on element :: ' + info)
                self.log.info(f'The text is :: "{text}"')
        except:
            self.log.error(f'Failed to get text on element :: {info}')
            print_stack()
            text = None

    def takeScreens(self, message=''):
        fileName = message + str(round(time.time()*1000)) + '.png'
        screenDirectory = "C:\\drive\\testing\\automation\\LetsKodeit\\screenshots\\"
        currentDirectory = os.path.dirname(__file__)
        relativeFileName = screenDirectory + fileName
        destinationFile = os.path.join(currentDirectory, relativeFileName)
        destinationDirectory = os.path.join(currentDirectory, screenDirectory)


        try:
            if not os.path.exists(destinationDirectory):
                os.makedirs(destinationDirectory)
            self.driver.save_screenshot(destinationFile)
            self.log.info(f'saved in {destinationFile}')
        except NotADirectoryError:
            self.log.error('### Exceptions Occured')
            print_stack()

    def windowSize(self, driver):
        height = driver.execute_script('return window.innerHeight;')

        width = driver.execute_script('return window.innerWidth;')
        self.log.info(f'Height: {height}px')
        self.log.info(f'Width: {width}px')

    # def isElementPresent(self, locator, locatorType='id'):
    #     try:
    #         element = self.getElement(locator, locatorType)
    #         if element is not None:
    #             self.log.info("Element Found - > " + locator)
    #             return True
    #         else:
    #             self.log.info("Element not found - > " + locator)
    #             return False
    #     except:
    #         self.log.info("Element not found - > " + locator)
    #         return False

    def isElementDisplayed(self, locator="", locatorType="id", element=None):
        """
        NEW METHOD
        Check if element is displayed
        Either provide element or a combination of locator and locatorType
        """
        isDisplayed = False
        try:
            if locator:  # This means if locator is not empty
                element = self.getElement(locator, locatorType)
            if element is not None:
                isDisplayed = element.is_displayed()
                self.log.info("Element is displayed with locator: " + locator +
                              " locatorType: " + locatorType)
            else:
                self.log.info("Element not displayed with locator: " + locator +
                              " locatorType: " + locatorType)
            return isDisplayed
        except:
            print("Element not found")
            return False

    def switchToFrame(self, id="", name="", index=None):
        """
        Switch to iframe using element locator inside iframe

        Parameters:
            1. Required:
                None
            2. Optional:
                1. id    - id of the iframe
                2. name  - name of the iframe
                3. index - index of the iframe
        Returns:
            None
        Exception:
            None
        """
        if id:
            self.driver.switch_to.frame(id)
        elif name:
            self.driver.switch_to.frame(name)
        else:
            self.driver.switch_to.frame(index)


    def switchToDefaultContent(self):
        """
        Switch to default content

        Parameters:
            None
        Returns:
            None
        Exception:
            None
        """
        self.driver.switch_to.default_content()

    def getElementAttributeValue(self, attribute, element=None, locator="", locatorType="id"):
        """
        Get value of the attribute of element

        Parameters:
            1. Required:
                1. attribute - attribute whose value to find

            2. Optional:
                1. element   - Element whose attribute need to find
                2. locator   - Locator of the element
                3. locatorType - Locator Type to find the element

        Returns:
            Value of the attribute
        Exception:
            None
        """
        if locator:
            element = self.getElement(locator=locator, locatorType=locatorType)
        value = element.get_attribute(attribute)
        return value

    def isEnabled(self, locator, locatorType="id", info=""):
        """
        Check if element is enabled

        Parameters:
            1. Required:
                1. locator - Locator of the element to check
            2. Optional:
                1. locatorType - Type of the locator(id(default), xpath, css, class, linkText)
                2. info - Information about the element, label/name of the element
        Returns:
            boolean
        Exception:
            None
        """
        element = self.getElement(locator, locatorType=locatorType)
        enabled = False
        try:
            attributeValue = self.getElementAttributeValue(element=element, attribute="disabled")
            if attributeValue is not None:
                enabled = element.is_enabled()
            else:
                value = self.getElementAttributeValue(element=element, attribute="class")
                self.log.info("Attribute value From Application Web UI --> :: " + value)
                enabled = not ("disabled" in value)
            if enabled:
                self.log.info("Element :: '" + info + "' is enabled")
            else:
                self.log.info("Element :: '" + info + "' is not enabled")
        except:
            self.log.error("Element :: '" + info + "' state could not be found")
        return enabled

    def elementPresenceCheck(self, locator, locatorType='id'):
        try:
            elementList = self.getElementList(locator, locatorType)
            if len(elementList) > 0:
                self.log.info("Element Found with locator -> " + locator)
                return True
            else:
                self.log.error("Element not found - > " + locator)
                return False
        except:
            self.log.error("Element not found - > " + locator)
            return False


    def waitForElement(self, locator, locatorType='id', timeout=10, poll_frequency=0.5):

        element = None
        try:
            byType = self.getByType(locatorType)
            print("Waiting for maximum :: " + str(timeout) + " :: seconds for element to be clickable")
            wait = WebDriverWait(self.driver, 10, poll_frequency=1, ignored_exceptions=[NoSuchElementException,
                                                                                  ElementNotVisibleException,
                                                                                  ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((byType, locator)))

            print('Element appeared on the web page')
        except:
            print('Element not appeared on the web page')
            print_stack()
        return element

    def webScroll(self, direction="up"):
        """
        NEW METHOD
        """
        if direction == "up":
            # Scroll Up
            self.driver.execute_script("window.scrollBy(0, -1000);")

        if direction == "down":
            # Scroll Down
            self.driver.execute_script("window.scrollBy(0, 1000);")

