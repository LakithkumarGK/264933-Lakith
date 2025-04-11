from employee_manager import EmployeeManager
from storage import Storage

#displaying employee details
def display_employees(employees):
    if not employees:
        print("No employees found.")
    for e in employees:
        print(f"{e.id} - {e.name}, Department: {e.department}, Designation: {e.designation}, "
              f"Gross Salary: {e.gross_salary}, Tax: {e.tax}, Bonus: {e.bonus}, Net Salary: {e.net_salary}")
 
def main():
    manager = EmployeeManager()
    storage = Storage()
 
    # Loading data from the file
    saved_data = storage.load_from_file()
    manager.load_employees(saved_data)
 
    while True:
        print("\nEmployee Management CLI")
        print("1. Add Employee\n2. View All Employees\n3. Search by ID\n4. Delete Employee\n5. Exit")
        choice = input("Enter your choice: ")
 
        if choice == '1':
            name = input("Enter Name: ")
            department = input("Enter Department: ")
            designation = input("Enter Designation: ")
            gross_salary = float(input("Gross Salary: "))
            tax = float(input("Tax: "))
            bonus = float(input("Bonus: "))
            employee = manager.add_employee(name, department, designation, gross_salary, tax, bonus)
            storage.save_to_file(manager.to_dict_list())
            print(f"Employee added with ID: {employee.id}")
 
        elif choice == '2':
            display_employees(manager.get_all_employees())
 
        elif choice == '3':
            emp_id = input("Enter Employee ID: ")
            employee = manager.search_by_employee_id(emp_id)
            if employee:
                print(f"{employee.id} - {employee.name}, Department: {employee.department}, "
                      f"Designation: {employee.designation}, Gross Salary: {employee.gross_salary}, "
                      f"Tax: {employee.tax}, Bonus: {employee.bonus}, Net Salary: {employee.net_salary}")
            else:
                print("Employee not found.")
 
        elif choice == '4':
            emp_id = input("Enter Employee ID: ")
            if manager.delete_employee(emp_id):
                storage.save_to_file(manager.to_dict_list())
                print("Employee deleted.")
            else:
                print("Employee not found.")
 
        elif choice == '5':
            print("Exiting application. Goodbye!")
            break
 
        else:
            print("Invalid choice!")
 
if __name__ == "__main__":
    main()