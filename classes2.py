"""
- Class is basically a group brand for creating instances
- Basic concepts:
    class
    method
    instances
- Class variables/Class atributes
- Instance variables/Instance atributes
"""


class Employee:
    # Class variable/atributes of the class
    raise_amount = 1.04
    num_of_emps = 0

    # Constructure to initialize the instances
    def __init__(self, first, last, salary):
        # This are the atributes of the class
        self.first = first
        self.last = last
        self.mail = first.lower() + '.' + last.lower() + '@gmail.com'
        self.salary = salary

        Employee.num_of_emps += 1

    # Defining the methods of the class:
    def fullname(self):
        return f"{self.first} {self.last}"

    def apply_raise(self):
        self.salary = int(self.salary * self.raise_amount)


# These are instances of the class Employee
# <__main__.Employee instance at 0x10a2a8dd0>
# <__main__.Employee instance at 0x10a2a8e18>
emp_1 = Employee("Manu", "Villate", 100000)
emp_2 = Employee("Fran", "Villate", 120000)
emp_3 = Employee("Jose", "Villate", 140000)

print(emp_1)
print(emp_2)
print(emp_1.mail)
# Calling the method fullname from the instance
print(emp_1.fullname())
# Calling the method fullname from the class
print(Employee.fullname(emp_1))
# Calling the method apply_raise
print(emp_1.salary)
emp_1.apply_raise()
print(emp_1.salary)

# Printing the Class variable and the instance variable
emp_1.raise_amount = 1.1
print(Employee.raise_amount)
print(emp_1.raise_amount)

# Printing the namespace
print(emp_1.__dict__)
print(Employee.__dict__)

# Printing the number of employees
print(Employee.num_of_emps)
