
class Demo():
    Value =10
    def __init__(self, no1,no2):
        self.No1 = no1
        self.No2 = no2

    def Fun(self):
        print("Inside instance method named as fun.")
        print(self.No1)
        print(self.No2)

    def Gun(self):
        print("Inside instance method named as gun.")
        print(self.No1)
        print(self.No2)

obj1 = Demo(11,12)
obj2 = Demo(51,101)
obj1.Fun()
obj2.Fun()
obj1.Gun()
obj2.Gun()

