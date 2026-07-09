# Program to add digits of a number

def Add(No):
    Sum = 0
    while No != 0:
        Digit = No % 10
        Sum = Sum + Digit
        No = No // 10
    return Sum

def main():
    Value = int(input("Enter a number: "))
    Ret = Add(Value)
    print("Addition of digits is:", Ret)

if __name__ == "__main__":
    main()