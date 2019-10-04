from pages.home.navigaion_page import NavigationPage
from pages.home.login_page import LoginPage
import unittest
import pytest

from utilities.teststatus import TestStatus

@pytest.mark.usefixtures('one_time_setUp', 'setUp')
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def ClassSetUp(self, one_time_setUp, setUp):
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)
        self.navigation = NavigationPage(self.driver)

    def setUp(self):
       self.navigation.clickLogo()


    @pytest.mark.run(order=2)
    def test_validLogin(self):
        self.lp.login('lutsiv96@mailinator.com', '123123123')
        result1 = self.lp.verifyTitle()
        self.ts.mark(result1, ' Title Verification ')
        result2 = self.lp.verifyLoginSuccessful()
        self.ts.markFinal('test_validLogin', result2, 'Login Verification')

    @pytest.mark.run(order=1)
    def test_invalidLogin(self):
        self.lp.logout()
        self.lp.login('fakaaaaaaaaaaaar@mailinator.com', password='z123123123')
        result = self.lp.verifyLoginFailed()
        self.ts.mark(result, ' Login Faile Verification')
