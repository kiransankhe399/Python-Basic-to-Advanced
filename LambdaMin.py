# Minimum of number

MinNum = lambda No1, No2 : No1 > No2 

def main():
    Value1 = int(input("Enter first number:"))
    Value2 = int(input("Enter second number:"))

    Ret = MinNum(Value1, Value2)
    if (Ret == False):
        print(f"Min of {Value1} & {Value2} is : {Value1}")
    else:
        print(f"Min of {Value1} & {Value2} is : {Value2}")

if __name__ == "__main__":
    main()
