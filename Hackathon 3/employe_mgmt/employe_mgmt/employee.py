import uuid
 
class Employee:
    def __init__(self, name, department, designation, gross_salary, tax, bonus, employee_id=None):
        self.id = employee_id if employee_id else str(uuid.uuid4())
        self.name = name          
        self.department = department
        self.designation = designation
        self.gross_salary = gross_salary
        self.tax = tax
        self.bonus = bonus
        self.net_salary = gross_salary - tax + bonus
 
    #serializes Employee object into a dictionary
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "department": self.department,
            "designation": self.designation,
            "gross_salary": self.gross_salary,
            "tax": self.tax,
            "bonus": self.bonus,
            "net_salary": self.net_salary
        }
 
    #restores Employee object from a dictionary 
    @staticmethod
    def from_dict(data):
        return Employee(
            name=data["name"],
            department=data["department"],
            designation=data["designation"],
            gross_salary=data["gross_salary"],
            tax=data["tax"],
            bonus=data["bonus"],
            employee_id=data["id"]
        )
   