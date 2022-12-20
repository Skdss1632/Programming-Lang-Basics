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
#     @classmethod
#     def set_raise_amt(cls, amount):
#         cls.raise_amount = amount
#
#
# emp_1 = Employee('corey', 'schafer', 50000)
# emp_2 = Employee('test', 'user', 60000)
#  doubt:...
#
# emp_1.set_raise_amt(1.05)
#
# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)

# .......................................................................................................................

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
#     @classmethod
#     def set_raise_amt(cls, amount):
#         cls.raise_amount = amount
#
#     @classmethod
#     def from_string(cls, emp_str):
#         first, last, pay = emp_str.split('-')
#         return cls(first, last, pay)
#
#
# emp_1 = Employee('corey', 'schafer', 50000)
# emp_2 = Employee('test', 'user', 60000)
#  doubt:...
# emp_1.set_raise_amt(1.05)

# emp_str_1 = 'john-doe-70000'
# emp_str_2 = 'steve-smith-30000'
# emp_str_3 = 'jane-doe-90000'
#
# new_emp_1 = Employee.from_string(emp_str_1)
#
# print(new_emp_1.email)
# print(new_emp_1.pay)

# .......................................................................................................................

# staticmethod examples are given below,static methods do not take the instance or class methods as the first argument:--

# class Employee:
#
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
#     @classmethod
#     def set_raise_amt(cls, amount):
#         cls.raise_amount = amount
#
#     @classmethod
#     def from_string(cls, emp_str):
#         first, last, pay = emp_str.split('-')
#         return cls(first, last, pay)
#
#     @staticmethod
#     def is_working(day):
#         if day.weekday() == 5 or day.weekday() == 6:
#             return False
#         return True
#
#
# emp_1 = Employee('corey', 'schafer', 50000)
# emp_2 = Employee('test', 'user', 60000)
#
# import datetime
# my_date = datetime.date(2016, 7, 10)
# print(Employee.is_working(my_date))

# end..................................................................