#Addition of number using lambda

AddNum = lambda No1, No2 : No1 + No2

def main():
    Value1 = int(input("Enter first number:"))

    Value2 = int(input("Enter second number:"))

    Ret = AddNum(Value1, Value2)
    print(f"Addition of {Value1},{Value2} is {Ret}")

if __name__ == "__main__":
    main()
