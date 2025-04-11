import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    def test_net_salary_calculation(self):
        emp = Employee("Pooja", "IT", "Engineer", 50000, 5000, 2000)
        self.assertEqual(emp.net_salary, 47000)

    def test_to_dict_and_from_dict(self):
        emp = Employee("Deepa", "HR", "Manager", 60000, 6000, 3000)
        emp_dict = emp.to_dict()
        restored = Employee.from_dict(emp_dict)
        self.assertEqual(restored.name, "Deepa")
        self.assertEqual(restored.net_salary, 57000)
        self.assertEqual(restored.id, emp.id)

