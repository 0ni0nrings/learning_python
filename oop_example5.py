class Employee:
    def __init__ (self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        self.email = first + '.' + last + '@company.com'
        pass

class Developer(Employee):
    def __init__(self, first, last, age, language):
        Employee.__init__(self, first, last, age)
        self.language = language

class Manager(Employee):
    def __init__(self, first, last, age, dept):
        Employee.__init__(self, first, last, age)
        self.dept = dept

Sam = Developer('Sam', 'Wilson', 21, 'Java')
Robin = Developer('Robin', 'Williams', 63, 'Fortran')
Marge = Manager('Marge', 'Simpson', 47, 'Cafe')
Homer = Manager('Homer', 'Simpson', 48, 'Bar')

print(Sam.age)
print(Marge.age)
print(Homer.dept)
print(Robin.language)
print(Sam.email)
print(Homer.email)


