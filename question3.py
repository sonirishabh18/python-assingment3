class Employee:

    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

e1 = Employee(101, "Rishabh", 50000)

print("Employee ID:", e1.emp_id)
print("Name:", e1.name)
print("Salary:", e1.salary)
