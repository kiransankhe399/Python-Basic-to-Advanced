
class Circle():
    PI = 3.14
    
    def __init__(self):
        self.Radius = 0.0
        self.Area = 0.0
        self.Circumference = 0.0

    def Accept(self):
        self.Radius = int(input("Enter radius of a circle : "))

    def CalcArea(self):
        self.ResArea = self.PI * self.Radius * self.Radius

    def CalcCircumference(self):
        self.ResCircum = 2* self.PI * self.Radius

    def Display(self):
        print("Radius of Cirle is :", self.Radius)
        print("Area of Circle is :", self.ResArea)
        print("Circumference is :", self.ResCircum)



obj1 = Circle()

obj1.Accept()
obj1.CalcArea()
obj1.CalcCircumference()
obj1.Display()