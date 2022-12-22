# class Employee:
#
#     def __init__(self, first, last):
#         self.first = first
#         self.last = last
#         self.email = first + '.' + last + '@email.com'
#
#     def fullname(self):
#         return '{} {}'.format(self.first, self.last)
#
#
# emp_1 = Employee('john', 'smith')
#
# print(emp_1.first)
# print(emp_1.email)
# print(emp_1.fullname())

# ........................................................................................................................

# without using property decorators

# class Employee:
#
#     def __init__(self, first, last):
#         self.first = first
#         self.last = last
#
#     def email(self):
#         return '{}.{}@gmail.com'.format(self.first, self.last)
#
#     def fullname(self):
#         return '{} {}'.format(self.first, self.last)
#
#
# emp_1 = Employee('john', 'smith')
#
# print(emp_1.first)
# print(emp_1.email())
# print(emp_1.fullname())

# ........................................................................................................................

# after using property dectorators below:--

# class Employee:
#
#     def __init__(self, first, last):
#         self.first = first
#         self.last = last
#
#     @property
#     def email(self):
#         return '{}.{}@gmail.com'.format(self.first, self.last)
#
#     @property
#     def fullname(self):
#         return '{} {}'.format(self.first, self.last)
#
#
# emp_1 = Employee('john', 'smith')
#
# print(emp_1.first)
# print(emp_1.email)
# print(emp_1.fullname)

# .........................................................................................................................

# using deletor below:--

# class Employee:
#
#     def __init__(self, first, last):
#         self.first = first
#         self.last = last
#
#     @property
#     def email(self):
#         return '{}.{}@gmail.com'.format(self.first, self.last)
#
#     @property
#     def fullname(self):
#         return '{} {}'.format(self.first, self.last)
#
#     @fullname.setter
#     def fullname(self, name):
#         first, last = name.split(' ')
#         self.first = first
#         self.last = last
#
#     @fullname.deleter
#     def fullname(self):
#         print("delete name")
#         self.first = None
#         self.last = None
#
#
# emp_1 = Employee('john', 'smith')
#
# emp_1.fullname = ('corey schafer')
#
# print(emp_1.first)
# print(emp_1.email)
# print(emp_1.fullname)
#
# del emp_1.fullname

# .......................................................................................................................

# using getter below:--

# class Employee:
#
#     def __init__(self, first, last):
#         self.first = first
#         self.last = last
#
#     @property
#     def email(self):
#         return '{}.{}@gmail.com'.format(self.first, self.last)
#
#     @property
#     def fullname(self):
#         return '{} {}'.format(self.first, self.last)
#
#     @fullname.getter
#     def fullname(self):
#         return self.last
#
#
# emp_1 = Employee('john', 'smith')
#
#
# print(emp_1.first)
# print(emp_1.email)
# print(emp_1.fullname)

# ..........................................................................................................................

# using setter below:--

# class Employee:
#
#     def __init__(self, first, last):
#         self.first = first
#         self.last = last
#
#     @property
#     def email(self):
#         return '{}.{}@gmail.com'.format(self.first, self.last)
#
#     @property
#     def fullname(self):
#         return '{} {}'.format(self.first, self.last)
#
#     @fullname.setter
#     def fullname(self, name):
#         first, last = name.split(' ')
#         self.first = first
#         self.last = last
#
#
# emp_1 = Employee('john', 'smith')
#
# emp_1.fullname = 'corey schafer'
#
# print(emp_1.first)
# print(emp_1.email)
# print(emp_1.fullname)

# END...................................................................................................................






