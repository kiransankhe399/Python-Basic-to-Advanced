
class Arithmatic():
    
    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0

    def Accept(self):
        self.Value1 = int(input("Enter first number : "))
        self.Value2 = int(input("Enter second number : "))

    def Addition(self):
        self.Add = self.Value1 + self.Value2
        print("Addition is is :", self.Add)

    def Substraction(self):
        self.Sub = self.Value1 - self.Value2
        print("Substraction is is :", self.Sub)
    
    def Multiplication(self):
        self.Mul = self.Value1 * self.Value2
        print("Multiplication is is :", self.Mul)

    def Division(self):
        if self.Value1 == 0:
            print("Division : Cannot be done Division by zero ")
        else:
            self.Div = self.Value1 % self.Value2
            print("Division is is :", self.Div)

obj1 = Arithmatic()

obj1.Accept()
obj1.Addition()
obj1.Substraction()
obj1.Multiplication()
obj1.Division()