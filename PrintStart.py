#Print Start from 1 

def Series(No):
    s = ""
    for i in range(1,No+1):
        s += str(i) + " "
    return s

def main():
    Value = int(input("Enter a Num : "))

    Res = Series(Value)
    print(Res)

if __name__ == "__main__":
    main()