class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def display(self):
        print("Employee ID:", self.emp_id)
        print("Name:", self.name)
        print("Salary:", self.salary)
        print("--------------------")


employees = []

n = int(input("Enter number of employees: "))

for i in range(n):
    print("\nEnter details of employee", i + 1)

    emp_id = input("Enter Employee ID: ")
    name = input("Enter Name: ")
    salary = float(input("Enter Salary: "))

    e = Employee(emp_id, name, salary)
    employees.append(e)

print("\nEmployee Details")
print("====================")

for e in employees:
    e.display()
