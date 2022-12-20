# class Employee:
#     raise_amount = 1.04
#
#     def __init__(self, first, last, pay):
#         self.first = first
#         self.last = last
#         self.pay = pay
#         self.email = first + '.' + last + '@company.com'
#
#     def fullname(self):
#         return '{} {}'.format(self.first, self.last)
#
#     def apply_raise(self):
#         self.pay = int(self.pay * Employee.raise_amount)
#
#
# emp_1 = Employee('corey', 'schafer', 50000)
# emp_2 = Employee('test', 'user', 60000)
# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)

# .........................

# class Employee:
#     raise_amount = 1.04
#
#     def __init__(self, first, last, pay):
#         self.first = first
#         self.last = last
#         self.pay = pay
#         self.email = first + '.' + last + '@company.com'
#
#     def fullname(self):
#         return '{} {}'.format(self.first, self.last)
#
#     def apply_raise(self):
#       self.pay = int(self.pay * Employee.raise_amount)
# emp_1 = Employee('corey', 'schafer', 50000)
# emp_2 = Employee('test', 'user', 60000)
# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)

# ...................................

# class Employee:
#
#     raise_amount = 1.04
#
#     def __init__(self, first, last, pay):
#         self.first = first
#         self.last = last
#         self.pay = pay
#         self.email = first + '.' + last + '@company.com'
#
#     def fullname(self):
#         return '{} {}'.format(self.first, self.last)
#
#     def apply_raise(self):
#         self.pay = int(self.pay * Employee.raise_amount)
#
#
# emp_1 = Employee('corey', 'schafer', 50000)
# emp_2 = Employee('test', 'user', 60000)
# print(emp_1.__dict__)
# # after applying dict on class name not getting expected result:-
# print(Employee.__dict__)

# .........................................................................................

# class Employee:
#
#     raise_amount = 1.04
#
#     def __init__(self, first, last, pay):
#         self.first = first
#         self.last = last
#         self.pay = pay
#         self.email = first + '.' + last + '@company.com'
#
#     def fullname(self):
#         return '{} {}'.format(self.first, self.last)
#
#     def apply_raise(self):
#         self.pay = int(self.pay * Employee.raise_amount)
#
#
# emp_1 = Employee('corey', 'schafer', 50000)
# emp_2 = Employee('test', 'user', 60000)
# print(emp_1.__dict__)
# # after applying dict on class name not getting expected result:-
# print(Employee.__dict__)

# ...............................................................................

# class Employee:
#
#     raise_amount = 1.04
#
#     def __init__(self, first, last, pay):
#         self.first = first
#         self.last = last
#         self.pay = pay
#         self.email = first + '.' + last + '@company.com'
#
#     def fullname(self):
#         return '{} {}'.format(self.first, self.last)
#
#     def apply_raise(self):
#         self.pay = int(self.pay * Employee.raise_amount)
#
#
# emp_1 = Employee('corey', 'schafer', 50000)
# emp_2 = Employee('test', 'user', 60000)
# # raising employee salary amount it changes the amount for class and all of the instances
# Employee.raise_amount = 1.05
# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)

# ..................................................................

# class Employee:
#
#     raise_amount = 1.04
#
#     def __init__(self, first, last, pay):
#         self.first = first
#         self.last = last
#         self.pay = pay
#         self.email = first + '.' + last + '@company.com'
#
#     def fullname(self):
#         return '{} {}'.format(self.first, self.last)
#
#     def apply_raise(self):
#         self.pay = int(self.pay * Employee.raise_amount)
#
#
# emp_1 = Employee('corey', 'schafer', 50000)
# emp_2 = Employee('test', 'user', 60000)
# # raising salary amount for employee 1 only
# emp_1.raise_amount = 1.05
# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)

# ....................................................................

# class Employee:
#
#     raise_amount = 1.04
#
#     def __init__(self, first, last, pay):
#         self.first = first
#         self.last = last
#         self.pay = pay
#         self.email = first + '.' + last + '@company.com'
#
#     def fullname(self):
#         return '{} {}'.format(self.first, self.last)
#
#     def apply_raise(self):
#         self.pay = int(self.pay * Employee.raise_amount)
#
#
# emp_1 = Employee('corey', 'schafer', 50000)
# emp_2 = Employee('test', 'user', 60000)
# # raising salary amount for employee 1 only
# emp_1.raise_amount = 1.05
# print(emp_1.__dict__)
# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)

# ................................................................

# class Employee:
#     no_of_emp = 0
#     raise_amount = 1.04
#
#     def __init__(self, first, last, pay):
#         self.first = first
#         self.last = last
#         self.pay = pay
#         self.email = first + '.' + last + '@company.com'
#         Employee.no_of_emp += 1
#
#     def fullname(self):
#         return '{} {}'.format(self.first, self.last)
#
#     def apply_raise(self):
#         self.pay = int(self.pay * Employee.raise_amount)
#
#
# print(Employee.no_of_emp)
# emp_1 = Employee('corey', 'schafer', 50000)
# emp_2 = Employee('test', 'user', 60000)
# print(Employee.no_of_emp)


# end..............................
