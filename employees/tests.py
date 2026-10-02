from django.test import TestCase
from .models import Department, Employee


class EmployeeTestCase(TestCase):

    def setUp(self):
        department = Department.objects.create(name="IT")

        Employee.objects.create(
            name="Test Employee",
            email="test@gmail.com",
            phone="9999999999",
            designation="Python Developer",
            salary=35000,
            joining_date="2026-10-02",
            department=department
        )

    def test_employee_created(self):
        employee = Employee.objects.get(email="test@gmail.com")
        self.assertEqual(employee.name, "Test Employee")
# Create your tests here.
