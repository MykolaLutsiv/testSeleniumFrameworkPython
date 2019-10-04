import time
from pages.courses.register_courses_page import RegisterCoursesPage
from utilities.teststatus import TestStatus
import unittest
import pytest
from ddt import data, unpack, ddt

@pytest.mark.usefixtures('one_time_setUp', 'setUp')
@ddt
class RegisterCoursesTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def ClassSeUp(self, one_time_setUp):
        self.rc = RegisterCoursesPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    @data(('Mac Linux Command Line Basics', '4149 4391 0221 3042', '0922', '038', '48400'),
          ('TestNG Complete Bootcamp - Novice To Ninja', '4149 4391 0221 3042', '0922', '038', '48400'))
    @unpack
    def test_invalidEnrollment(self, courseName, ccNum, ccExp, ccCvv, zip):
        self.rc.enterCourseName(courseName)
        self.rc.selectCourseToEnroll(courseName)
        self.rc.enrollCourse(num=ccNum, exp=ccExp, cvv=ccCvv, postal_code=zip)
        result = self.rc.verifyEnrollFailed()
        self.ts.markFinal('test_invalidEnrollment', result, 'Verification invalid Enrollment')
        self.rc.getElement(locator='.navbar-brand', locatorType='css').click()
