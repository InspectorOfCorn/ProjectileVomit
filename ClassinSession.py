


class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + "@company.com"

    def fullname(self):
        return '{} {}' .format(self.first, self.last)
#Classes are blueprints for creating instances and each unique employee we create with our calss they each become instances

emp_1 = Employee('Test', 'User', 50000)
emp_2 = Employee('Bilal', 'Omar', 200000)

print(Employee.fullname(emp_1))
# print(emp_2.fullname())
# Remember () after function 