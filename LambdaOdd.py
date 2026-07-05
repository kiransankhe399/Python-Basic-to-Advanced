# Odd of number using lambda

OddNum = lambda No : No%2 != 0

def main():
    Value = int(input("Enter first number:"))

    Ret = OddNum(Value)
    if (Ret == True):
        print(f"Number {Value} is odd and False")
    else:
        print(f"Number {Value} is Not odd")


if __name__ == "__main__":
    main()
