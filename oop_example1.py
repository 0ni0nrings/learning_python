class Employee:
    def __init__(self, first, last, pay):
        self.first = first # property/attributes
        self.last = last
        self.email = self.first + '.' + self.last + '@bank.com'
        self.pay = pay

    def fullname(self): # method
        return 'f{self.first} {self.last}'

    def annual_raise(self):
        return self.pay * 1.5

employee1 = Employee('taylor', 'swift', 50000)
employee2 = Employee('dua', 'lipa', 60000)

print(employee1.fullname())
print(employee2.fullname())
print(employee1.email) # didn't pass as parameter in class
print(employee2.email)
print(employee1.pay)
print(employee2.pay)
print(employee1.annual_raise())
print(employee2.annual_raise())
