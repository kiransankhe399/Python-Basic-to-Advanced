#Reverse print for num for input no.

def Reverse(No):
    s = ""
    for i in range(No, 0, -1):
        s += str(i) + " "
    return s

def main():
    Value = int(input("Enter a Num : "))

    Res = Reverse(Value)
    print(Res)

if __name__ == "__main__":
    main()