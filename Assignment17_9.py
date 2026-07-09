#program to print number of digit

def Number(No):
    Ret = len(str(No))
    return Ret

def main():
    Value = int(input("Enter a number : "))
    Return = Number(Value)
    print(Return)

if __name__ == "__main__":
    main()