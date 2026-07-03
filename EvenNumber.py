#Print all even number

def EvenNum(No):
    EvenList = []

    for i in range(1, No+1):
        if i% 2 == 0:
            EvenList.append(i)

    return EvenList

def main():
    Value = int(input("Enter a number:"))
    Res = EvenNum(Value)
    print("Even numbers are:", Res)

if __name__ == "__main__":
    main()