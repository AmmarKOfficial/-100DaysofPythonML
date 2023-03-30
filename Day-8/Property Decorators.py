# Property Decotators

class Employee:
    
    def __init__(self, first, last):
        self.first = first
        self.last = last
        
    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)
    
    # I cant change the full name manually but will satter do it
    
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last
        
    @fullname.deleter  # Will delete name and set them to none
    def fullname(self):
        print('Delete Name')
        self.first = None
        self.last = None
        
emp_1 = Employee('Jhon', 'Smith')

emp_1.first = 'Ammar' # Email will still remain same that an issue
emp_1.last = 'Khan'

emp_1.fullname = 'Sheharyar Khan' # This command will work because of setter and update all the veriable

print(emp_1.email)
print(emp_1.fullname)

del emp_1.fullname

print(emp_1.email)
print(emp_1.fullname)