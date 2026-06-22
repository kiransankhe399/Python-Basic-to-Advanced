print("-------------Function Parameter---------------------------------")


def Multi(No1,No2):  #Function with parameter
    Ans=  No1 * No2
    return Ans

def main():       #Function with no parameter
    print("Enter first number:")
    Value1 = int(input())

    print("Enter second number")
    Value2 = int(input())

    Res = Multi(Value1,Value2)
    print("Multiplication is:", Res)

if __name__ == "__main__":
    main()