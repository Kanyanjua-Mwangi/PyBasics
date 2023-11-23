
class Employee:


    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + last + '@' + 'wakulima.com'

    @property
    def email(self):
        return '{} {}email.com'.format(self.first, self.last)
   
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last
    
emp1 = Employee('Jackson', 'James', 80000)
emp1.first = 'Mike'

print(emp1.first)
print(emp1.last)
print(emp1.email)
print(emp1.fullname())