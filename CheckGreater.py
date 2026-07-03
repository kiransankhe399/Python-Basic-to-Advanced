#Function to check greater number

def ChkGreater(No1, No2):
    if No1>No2:
        return No1
    else:
        return No2

def main():
    input1 = int(input("Enter first number :"))
    input2 = int(input("Enter second number :"))
    Res = ChkGreater(input1,input2)
    print("Greater number is:", Res)

if __name__ == "__main__":
    main()