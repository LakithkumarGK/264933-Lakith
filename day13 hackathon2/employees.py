from management import Employee, Department, save_to_json, load_from_json
 
# -----------------------

# Sample Main Execution

# -----------------------
 
data_strings = [

    "Lakith,35,Male,E101,HR,45000",
    "Janu,29,Female,E102,IT,60000",
    "Kiran,42,Male,E103,HR,48000",
    "Sara,30,Female,E104,IT,50000",
    "Teja,40,Male,E105,Finance,52000"

]
 
# Create Employee objects

employees = [Employee.from_string(s) for s in data_strings]
 
# Create Departments and assign employees

departments = {}

for emp in employees:

    if emp.department not in departments: # getattr(emp, 'department')

        departments[emp.department] = Department(emp.department)

    departments[emp.department].add_employee(emp)
 
# Print Details

Employee.bonus_policy()

print("\nEmployee Details:")

for emp in employees:

    print(emp.get_details())
 
# Print Department Average Salaries

print("\nAverage Salaries by Department:")

for dept_name, dept in departments.items():

    print(f"{dept_name}: ₹{dept.get_average_salary():.2f}")
 
# Save Data

save_to_json(employees)
 
# Load and verify

print("\n📂 Loaded Data from JSON:")

loaded_emps = load_from_json() # Should take data from json, create employee objects and return the list 

                               # loaded_emps should look like employees created before

for emp in loaded_emps:

    print(emp.get_details())
 