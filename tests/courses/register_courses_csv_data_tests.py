import time
from utilities.read_data import getCSVData
from pages.home.navigaion_page import NavigationPage
# from pages.courses.register_courses_page import RegisterCoursesPage
from utilities.teststatus import TestStatus
import unittest
import pytest
from pages.courses import register_courses_page
from ddt import data, unpack, ddt

@pytest.mark.usefixtures('one_time_setUp', 'setUp')
@ddt
class RegisterCoursesCSVDataTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetUp(self, one_time_setUp, setUp):
        self.rc = register_courses_page.RegisterCoursesPage(self.driver)
        self.ts = TestStatus(self.driver)
        self.navigation = NavigationPage(self.driver)

    def setUp(self):
       self.navigation.clickLogo()

    @pytest.mark.run(order=3)
    @data(*getCSVData('C:\\drive\\testing\\automation\\LetsKodeit\\courses_test_data.csv'))
    # @data(('Mac Linux Command Line Basics', '4149 4391 0221 3042', '0922', '038', '48400'),
    #       ('TestNG Complete Bootcamp - Novice To Ninja', '4149 4391 0221 3042', '0922', '038', '48400'))
    @unpack
    def test_invalidEnrollment(self, courseName, ccNum, ccExp, ccCvv, zip):
        self.rc.enterCourseName(courseName)
        self.rc.selectCourseToEnroll(courseName)
        self.rc.enrollCourse(num=ccNum, exp=ccExp, cvv=ccCvv, postal_code=zip)
        result = self.rc.verifyEnrollFailed()
        self.ts.markFinal('test_invalidEnrollment', result, 'Verification invalid Enrollment')
        self.rc.getElement(locator='.navbar-brand', locatorType='css').click()

    @pytest.mark.run(order=4)
    @data(('Hemil Patel', 'Hemil Patel'),("Let's Kode It", "Let's Kode It"))
    @unpack
    def test_selecting_of_author(self,authorName, authorNeedToBeSelected ):
        self.rc.selectAuthor(authorName)
        time.sleep(1)
        result = self.rc.verifySelectingOfAuthor(authorNeedToBeSelected)
        self.ts.markFinal('test_invalidEnrollment', result, 'verifyOfSelectedAothor')
        time.sleep(1)