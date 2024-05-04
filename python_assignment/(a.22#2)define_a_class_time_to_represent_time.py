# define a class time to represent time like 3hr 45min 20sec.
class Time:
    
    def __init__(self):
        self.hrs = 00
        self.min = 00
        self.sec = 00

    def set_time(self):
        self.hrs = 4
        self.min = 55
        self.sec = 60

    @property
    def display(self):
        return self.hrs, "hrs", self.min, "min", self.sec, "sec"


clock1 = Time()
clock1.set_time()
print(clock1.display)

