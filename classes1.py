"""
- Class is basically a group brand for creating instances

"""

class Employee:
    #Constructure to initialize the instances
    def __init__(self, first, last, salary):
        #This are the atributes of the class
        self.first = first
        self.last = last
        self.mail = first.lower() + '.' + last.lower() + '@gmail.com'
        self.salary = salary

    #Defining the methods of the class:
    def fullname(self):
        return f"{self.first} {self.last}"

#These are instances of the class Employee
#<__main__.Employee instance at 0x10a2a8dd0>
#<__main__.Employee instance at 0x10a2a8e18>
emp_1 = Employee("Manu", "Villate", 100000)
emp_2 = Employee("Fran", "Villate", 120000)

print(emp_1)
print(emp_2)
print(emp_1.mail)
# Calling the method from the instance
print(emp_1.fullname())
# Calling the method from the class
print(Employee.fullname(emp_1))
