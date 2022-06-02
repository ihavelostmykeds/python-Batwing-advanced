import unittest
from unittest import mock

from employee import Employee


class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.employeeTest = Employee('Alex', 'Zasanskyi', 100)

    def test_email(self):
        self.assertEqual(self.employeeTest.email, 'Alex.Zasanskyi@email.com')

    def test_fullname(self):
        self.assertEqual(self.employeeTest.fullname, 'Alex Zasanskyi')

    def test_apply_raise(self):
        self.employeeTest.apply_raise()
        self.assertEqual(self.employeeTest.pay, 105)

    @mock.patch('employee.requests.get')
    def test_monthly_schedule(self, mock_request):
        month = 'May'
        mock_request.return_value.ok = True
        mock_request.return_value.text = f'http://company.com/{self.employeeTest.last}/{month}'
        self.assertEqual(self.employeeTest.monthly_schedule(month),
                         f'http://company.com/{self.employeeTest.last}/{month}')
