#Print all odd number

def OddNum(No):
    OddList = []

    for i in range(1, No+1):
        if i% 2 != 0:
            OddList.append(i)

    return OddList

def main():
    Value = int(input("Enter a number:"))
    Res = OddNum(Value)
    print("Odd numbers are:", Res)

if __name__ == "__main__":
    main()