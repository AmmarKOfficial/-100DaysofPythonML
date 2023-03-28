# Python Object-Oriented Programming

class Employee:
    
    def __init__(self, first, last, pay):  # Constructors 
        self.first = first;
        self.last = last;
        self.pay = pay;
        self.email = first + '.' + last + '@company.com'
    
    def display(self):
        print(f" Employee Name is {self.first} {self.last} with salary {self.pay} and email:{self.email}")
    
    def name(self):
        print(self.first)

# Class is a Blueprint for instances/objects

emp_1 = Employee('Ammar', 'Khan', 50000);
emp_2 = Employee('Sheharyar', 'Khan', 51000);

print(emp_2.display())
print(emp_1.display())

print(emp_2.name())