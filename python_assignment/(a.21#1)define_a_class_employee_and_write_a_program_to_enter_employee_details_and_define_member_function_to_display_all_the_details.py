# class employee and write a program to enter employee details and define member function to display all the details.
class Employee:
    # constructor
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    # instance member function

    def display(self):
        print(self.name, self.age, self.salary)


t1 = Employee("sk", 18, 3500)
t1.display()