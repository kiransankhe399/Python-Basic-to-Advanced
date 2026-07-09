#program to get addition of factors

def Fact(No):
    Res = 0
    for i in range(1, No):
        if No % i == 0:      
            Res = Res + i   
    return Res

def main():
    Value = int(input("Enter a Number: "))
    Ret = Fact(Value)
    print("Sum of factors is:", Ret)

if __name__ == "__main__":
    main()