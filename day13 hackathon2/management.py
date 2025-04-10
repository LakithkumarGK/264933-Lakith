import json

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def get_details(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"

class Employee(Person):
    def __init__(self, name, age, gender, emp_id, department, salary):
        super().__init__(name, age, gender)
        self.emp_id = emp_id
        self.department = department
        self.salary = salary

    def is_eligible_for_bonus(self):
        return self.salary < 50000

    @classmethod
    def from_string(cls, data_string):
        name, age, gender, emp_id, department, salary = data_string.split(',')
        return cls(name, int(age), gender, emp_id, department, float(salary))

    @staticmethod
    def bonus_policy():
        print("Bonus Policy: Employees with a salary less than ₹50,000 are eligible for a bonus.")

class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def get_average_salary(self):
        if not self.employees:
            return 0.0
        return sum(emp.salary for emp in self.employees) / len(self.employees)

    def save_to_json(self, filename="employees.json"):
        employees_data = [{
            'name': emp.name,
            'age': emp.age,
            'gender': emp.gender,
            'emp_id': emp.emp_id,
            'department': emp.department,
            'salary': emp.salary
        } for emp in self.employees]
        with open(filename, 'w') as f:
            json.dump(employees_data, f, indent=10)

    def load_from_json(self, filename="employees.json"):
        with open(filename, 'r') as f:
            data = json.load(f)
        for emp_data in data:
            employee = Employee(**emp_data)
            self.add_employee(employee)

if __name__ == "__main__":
    # strings for employee
    data_strings = [
        "Lakith,35,Male,E101,HR,45000",
        "Janu,29,Female,E102,IT,60000",
        "Kiran,42,Male,E103,HR,48000",
        "Sara,30,Female,E104,IT,50000",
        "Teja,40,Male,E105,Finance,52000"
    ]

    
    employees = [Employee.from_string(s) for s in data_strings]

 
    hr_department = Department("HR")
    it_department = Department("IT")
    finance_department = Department("Finance")

    # +employees to departments
    for emp in employees:
        if emp.department == "HR":
            hr_department.add_employee(emp)
        elif emp.department == "IT":
            it_department.add_employee(emp)
        elif emp.department == "Finance":
            finance_department.add_employee(emp)


    Employee.bonus_policy()

    # Employee Details
    print("\nEmployee Details:")
    for emp in employees:
        print(emp.get_details())

     #Average 
    print("\nAverage Salaries by Department:")
    for dept in [hr_department, it_department, finance_department]:
        print(f"{dept.name}: ₹{dept.get_average_salary():.2f}")

    
    hr_department.save_to_json()
    #finance_department.save_to_json()
    #it_department.save_to_json()

    # Load Data from JSON and verify
    print("\n Loaded Data from JSON:")
    loaded_department = Department("HR")
    loaded_department.load_from_json()
    for emp in loaded_department.employees:
        print(emp.get_details())
        
        
      