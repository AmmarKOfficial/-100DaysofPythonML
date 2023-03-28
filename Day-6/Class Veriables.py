# Class Veriables

class Employee:
    raise_amount = 1.04
    
    def __init__(self, first, last, pay):  # Constructors 
        self.first = first;
        self.last = last;
        self.pay = pay;
        self.email = first + '.' + last + '@company.com'
    
    def display(self):
        print(f" Employee Name is {self.first} {self.last} with salary {self.pay} and email:{self.email}")
    
    def apply_raise(self):
        self.pay = int(self.pay* self.raise_amount)
        
        
emp_1 = Employee('Ammar', 'Khan', 50000);
emp_2 = Employee('Sheharyar', 'Khan', 51000);

emp_1.raise_amount = 1.05     # Only change veriable value for specific object
print(emp_1.raise_amount) 
print(emp_2.raise_amount)
print(Employee.raise_amount)
