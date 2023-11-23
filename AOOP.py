class Employee:

    payraiseamount = 1.66
    number_of_emps = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + last + '@' + 'wakulima.com'

        Employee.number_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def pay_rise(self):
        self.pay = (self.pay * self.payraiseamount)

    def __repr__(self):
        return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

    def __add__(self, other):
        return self.pay + other.pay    

    @classmethod
    def set_raise_amnt(cls, amount):
        cls.payraiseamount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay,)
    
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

class Developer(Employee):
    raise_amnt = 1.22

    def __init__(self, first, last, pay, company):
        super().__init__(first, last, pay)
        self.company = company

    

class Manager(Employee):
    def __init__(self, first, last, pay, employees = None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
    

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for employees in self.employees:
           print(self.employees.first)  

   
            
            





        
emp1 = Developer('Nicholas', 'Jackson', 69000, 'Chelsea')
emp2 = Developer('Juan', 'Mata', 68000, 'Spain')

print(emp1.email)
print(emp2.email)

print(emp1.fullname())
print(emp2.fullname())
print(Employee.fullname(emp1))
print(Employee.fullname(emp2))

emp1.pay_rise()
emp2.pay_rise()

print(emp1.pay)
print(emp2.pay)

print(Employee.__dict__)
print(Employee.number_of_emps)

print(Employee.payraiseamount)
print(emp1.payraiseamount)
print(emp2.payraiseamount)

emp_str_1 = 'Samson-Gusto-90000'
emp_str_2 = 'Daktari-Mkubwa-96000'
emp_str_3 = 'Ole-Gunner-85000'


new_emp_1 = Employee.from_string(emp_str_1)
new_emp_2 = Employee.from_string(emp_str_2)
new_emp_3 = Employee.from_string(emp_str_3)

print(new_emp_1.payraiseamount)
print(new_emp_2.pay)
print(new_emp_3.email)

import datetime
mydate = datetime.date(2023, 5, 10)

print(Employee.is_workday(mydate))

print(emp1.company)

mgr1 = Manager('Sue', "Smith", 900000, [emp1])

print(mgr1.email)
mgr1.add_emp(emp2)
mgr1.add_emp(new_emp_1)

mgr1.print_emps()

