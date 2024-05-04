# single inheritance

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
#         return f'{self.first}{self.last}'
#
#     def apply_raise(self):
#         self.pay = int(self.pay * Employee.raise_amount)
#
#
# class Developer(Employee):
#     pass
#
#
# dev_1 = Developer('corey', 'schafer', 50000)
# dev_2 = Developer('test', 'user', 60000)
# print(dev_1.email)

# ..........................................................................................................................

# using help in single inheritance

# single inheritance
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
# class Developer(Employee):
#     pass
#
#
# dev_1 = Developer('corey', 'schafer', 50000)
# dev_2 = Developer('test', 'user', 60000)
#
# print(help(Developer))
# print(dev_1.email)
# print(dev_2.email)

# .........................................................................................................................

# changing value of raise amt of subclasses

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
#         return f'{self.first}{self.last}'
#
#     def apply_raise(self):
#         self.pay = int(self.pay * self.raise_amount)
#
#
# class Developer(Employee):
#     raise_amount = 1.10
#
#
# dev_1 = Developer('corey', 'schafer', 50000)
# dev_2 = Developer('test', 'user', 60000)
# print(dev_1.pay)
# dev_1.apply_raise()
# print(dev_1.pay)

# ..........................................................................................................................

# using super in child or subclass

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
#         return f'{self.first}{self.last}'
#
#     def apply_raise(self):
#         self.pay = int(self.pay * self.raise_amount)
#
#
# class Developer(Employee):
#     raise_amount = 1.10
#
#     def __init__(self, first, last, pay, prog_lang):
#         super().__init__(first, last, pay)
#         self.prog_lang = prog_lang
#
#
# dev_1 = Developer('corey', 'schafer', 50000, 'python')
# dev_2 = Developer('test', 'user', 60000, 'java')
# print(dev_1.pay)
# dev_1.apply_raise()
# print(dev_1.pay)
# print(dev_1.prog_lang)

# ..........................................................................................................................
# creating another subclass called manager

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
#         return f'{self.first}{self.last}'
#
#     def apply_raise(self):
#         self.pay = int(self.pay * self.raise_amount)
#
#
# class Developer(Employee):
#     raise_amount = 1.10
#
#     def __init__(self, first, last, pay, prog_lang):
#         super().__init__(first, last, pay)
#         self.prog_lang = prog_lang
#
#
# class Manager(Employee):
#     def __init__(self, first, last, pay, employees=None):
#         super().__init__(first, last, pay)
#         if employees is None:
#             self.employees = []
#         else:
#             self.employees = employees
#
#     def add_emp(self, emp):
#         if emp not in self.employees:
#             self.employees.append(emp)
#
#     def remove_emp(self, emp):
#         if emp in self.employees:
#             self.employees.remove(emp)
#
#     def print_emps(self):
#         for emp in self.employees:
#             print('-->', emp.fullname())
#
#
# dev_1 = Developer('corey', 'schafer', 50000, 'python')
# dev_2 = Developer('test', 'user', 60000, 'java')
#
# mgr_1 = Manager('sue', 'smith', 90000, [dev_1])
# print(mgr_1.print_emps())
# print(mgr_1.email)
# print(mgr_1.first)
# print(mgr_1.last)
# print(mgr_1.pay)
# mgr_1.add_emp(dev_2)
# print(mgr_1.print_emps())
#
#
# # print(dev_1.pay)
# # dev_1.apply_raise()
# # print(dev_1.pay)
# # print(dev_1.prog_lang)

# end...................................................................................................................

















