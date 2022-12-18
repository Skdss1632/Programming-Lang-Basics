# define a class time to represent time like 3hr 45min 20sec.
class Time:
    def __init__(self):
        self.hrs = 00
        self.min = 00
        self.sec = 00

    def set_hrs(self):
        self.hrs = 4
        self.min = 55
        self.sec = 60

    def display(self):
        print(self.hrs, "hrs", self.min, "min", self.sec, "sec")


t1 = Time()
t1.set_hrs()
t1.display()

