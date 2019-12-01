class Staff:
    company = "bank.com"
    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary
        # self.email = first + "." + last + "@bank.com"
    
    def email(self):
        # return (f"{self.first}.{self.last}@bank.com")
        return self.first + "." + self.last + "@bank.com" 

    def annual_raise(self):
        return self.salary * 1.5    

emp1 = Staff('taylor', 'swift', 10000)
print(emp1.first)
print(emp1.email())
print(emp1.annual_raise()) 

