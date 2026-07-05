# Divisible of number using lambda

DivisibleNum = lambda No : No%5 == 0

def main():
    Value = int(input("Enter first number:"))

    Ret = DivisibleNum(Value)
    if (Ret == True):
        print(f"Number {Value} is Divisible and {Ret}")
    else:
        print(f"Number {Value} is Not Divisible")

if __name__ == "__main__":
    main()
