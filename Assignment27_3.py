
class Numbers():
    
    def __init__(self,value):
        self.Value = value 

    def CheckPrime(self):
        print("------- Check Prime--------------")

        if self.Value <= 1:
            return False

        for i in range(2, self.Value):
            if self.Value % i == 0:
                return False
        return True

    def CheckPerfect(self):
        print("-------Check Perfect--------------")
        sum = 0
        for i in range(1, self.Value):
            if self.Value % i == 0:
                sum += i

        return sum == self.Value

    def Factors(self):
        print("-------Check Factor--------------")
        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                print(i, end=" ")
        print()

    def SumFactors(self):
        print("-------Sum of Factors--------------")
        sum = 0
        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                sum += i

        return sum

obj1 = Numbers(int(input("Enter a Number : ")))
print("Perfect:", obj1.CheckPerfect())
print("Prime:", obj1.CheckPrime())
obj1.Factors()
print("Sum of Factors:", obj1.SumFactors())
