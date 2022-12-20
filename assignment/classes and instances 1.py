# classes and instance.....

# class Employee:
#     def __init__(self, first, last, pay):
#         self.first = first
#         self.last = last
#         self.pay = pay
#         self.email = first + '.' + last + '@company.com'
#
#
# emp_1 = Employee('corey', 'schafer', 50000)
# emp_2 = Employee('test', 'user', 60000)
# print(emp_1.email)
# print(emp_2.email)
# print('{} {}'.format(emp_1.first, emp_2.last))

# ........

# class Employee:
#     def __init__(self, first, last, pay):
#         self.first = first
#         self.last = last
#         self.pay = pay
#         self.email = first + '.' + last + '@company.com'
#
#     def fullname(self):
#         return '{} {}'.format(self.first, self.last)
#
#
# emp_1 = Employee('corey', 'schafer', 50000)
# emp_2 = Employee('test', 'user', 60000)

# print(emp_1.email)
# print(emp_2.email)
# print(emp_2.fullname())
# print(Employee.fullname(emp_1))

# .......

# class Employee:
#     def __init__(self, first, last, pay):
#         self.first = first
#         self.last = last
#         self.pay = pay
#         self.email = first + '.' + last + '@company.com'
#
#     def fullname():
#         return '{} {}'.format(self.first, self.last)
#
#
# emp_1 = Employee('corey', 'schafer', 50000)
# emp_2 = Employee('test', 'user', 60000)

# print(emp_1.email)
# print(emp_2.email)
# automatically passing emp_2 in full name instance function we need to pass self for expected result
# print(emp_2.fullname())



