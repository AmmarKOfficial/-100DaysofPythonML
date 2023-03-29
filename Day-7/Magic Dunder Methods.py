# (Magic/Dunder) Megic

# __init__
# __str__
# __repr__

# Inheritance

class Employee:
    raise_amt= 1.04
    
    def __init__(self, first, last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@email.com'
        
    def display(self):
        print(f"The Employee {self.first} {self.last} has {self.pay} and email:{self.email}")
        
    def raise_pay(self):
        self.pay = int(self.pay * self.raise_amt)
        
    def __repr__(self):
       return f"The Employee {self.first} {self.last} has {self.pay} and email:{self.email}"
     
    def __str__(self):
        return '{} - {}'.format(self.first, self.email)
#######################
        
dev_1 = Employee('Ammar', 'Khan', 50000)
dev_2 = Employee('Kaleem', 'Ullah', 60000)

print(dev_1.__repr__())
print(dev_1.__str__())





