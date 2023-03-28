# Class Methods and Static Methonds

class Employee:
    num_of_emps = 0
    raise_amount = 1.04
    
    def __init__(self, first, last, pay):  # Constructors 
        self.first = first;
        self.last = last;
        self.pay = pay;
        self.email = first + '.' + last + '@company.com'
    
    def display(self):
        print(f"Employee Name is {self.first} {self.last} with salary {self.pay} and email:{self.email}")
    
    def apply_raise(self):
        self.pay = int(self.pay* self.raise_amount)
    
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount
        
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)
    
    @staticmethod
    def is_workday(day):
        if(day.weekday() == 5 or day.weekday() == 6):
            return False
        return True
        
emp_1 = Employee('Ammar', 'Khan', 50000);
emp_2 = Employee('Sheharyar', 'Khan', 51000);

Employee.set_raise_amt(1.05)

#print(emp_1.raise_amount) 
#print(emp_2.raise_amount)
#print(Employee.raise_amount)

new_str_1 = 'Jhon-Doe-70000'

new_emp_1 = Employee.from_string(new_str_1)
print(new_emp_1.display())

# Static methods doesn't pass anything to class

import datetime
my_date = datetime.date(2023,3, 4)

print(Employee.is_workday(my_date))