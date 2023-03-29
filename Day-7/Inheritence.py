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
       
#######################
        
class Developer(Employee):  # Inherited from Employee
    raise_amt = 1.5;
    
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        # super will call the main class construsctor function and pass
        # the given attributes as similar to Employee.__init__(self, first, last, pay)
        self.prog_lang = prog_lang;
        
#######################
        
class Manager(Employee):
    
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
            
    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
            
    def remove_employee(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
            
    def print_emps(self):
        for emps in self.employees:
            print(f"--> {emps.first}")
            
##########################
        
dev_1 = Developer('Ammar', 'Khan', 50000, 'Python')
dev_1.raise_pay()
dev_2 = Employee('Kaleem', 'Ullah', 60000)
dev_2.raise_pay()

#print(dev_1.prog_lang)

mgr1 = Manager('Ali', 'Mustafa', 80000, [dev_1])
print(mgr1.email)
mgr1.add_employee(dev_2)
mgr1.remove_employee(dev_1)
mgr1.print_emps()

