#program to factorial

def Fact(No):
    Res = 1
    for i in range(1, No + 1):
        Res = Res * i
    return Res

def main():
    Value = int(input("Enter a Number: "))
    Ret = Fact(Value)
    print("Factorial is:", Ret)

if __name__ == "__main__":
    main()