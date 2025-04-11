from employee import Employee
 
class EmployeeManager:
    def __init__(self):
        self.employees = []
 
    #Adding employee
    def add_employee(self, name, department, designation, gross_salary, tax, bonus):
        employee = Employee(name, department, designation, gross_salary, tax, bonus)
        self.employees.append(employee)
        return employee
 
    #All employee data
    def get_all_employees(self):
        return self.employees
    
    #Searching employee
    def search_by_employee_id(self, employee_id):
        return next((e for e in self.employees if e.id == employee_id), None)

    #Deleting employeing
    def delete_employee(self, employee_id):
        employee = self.search_by_employee_id(employee_id)
        if employee:
            self.employees.remove(employee)
            return True
        return False
 
    def load_employees(self, employee_dicts):
        self.employees = [Employee.from_dict(d) for d in employee_dicts]
 
    def to_dict_list(self):
        return [e.to_dict() for e in self.employees]