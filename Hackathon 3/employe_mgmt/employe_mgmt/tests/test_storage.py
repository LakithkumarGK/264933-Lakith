import unittest
import os
import pickle
from storage import Storage
from employee import Employee

class TestStorage(unittest.TestCase):
    def setUp(self):
        self.test_file = r"C:\Users\Administrator\Desktop\coading\Hackathon 3\employe_mgmt.pkl"

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_save_and_load_employee_dicts(self):
        emp = Employee("Arun", "Engineering", "Lead", 80000, 8000, 4000)
        emp_dict_list = [emp.to_dict()]
        
        # Save using static method
        Storage.save_to_file(emp_dict_list, filename=self.test_file)

        # Load using static method
        loaded = Storage.load_from_file(filename=self.test_file)

        self.assertEqual(len(loaded), 1)
        self.assertEqual(loaded[0]["name"], "Arun")
        self.assertEqual(loaded[0]["net_salary"], emp.net_salary)

if __name__ == "__main__":
    unittest.main()
