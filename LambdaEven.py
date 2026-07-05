# Even of number using lambda

EvenNum = lambda No : No%2 == 0

def main():
    Value = int(input("Enter first number:"))

    Ret = EvenNum(Value)
    if (Ret == True):
        print(f"Number {Value} is Even and : {Ret}")
    else:
        print(f"Number {Value} is not Even")




if __name__ == "__main__":
    main()
