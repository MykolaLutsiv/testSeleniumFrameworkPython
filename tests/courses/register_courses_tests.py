import time

from selenium import webdriver
from pages.home.login_page import LoginPage
from pages.courses.register_courses_page import RegisterCoursesPage
from utilities.teststatus import TestStatus
import unittest
import pytest

@pytest.mark.usefixtures('one_time_setUp', 'setUp')
class RegisterCoursesTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def ClassSeUp(self, one_time_setUp):
        self.rc = RegisterCoursesPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    def test_invalidEnrollment(self):
        self.rc.enterCourseName('Rest API')
        self.rc.selectCourseToEnroll("Rest API Automation With Rest Assured")
        self.rc.enrollCourse(num='4149 4391 0221 3042', exp='0922', cvv='038', postal_code='48400')
        result = self.rc.verifyEnrollFailed()
        self.ts.markFinal('test_invalidEnrollment', result, 'Verification invalid Enrollment')

